import os
import json

def convert_to_yolo(json_path, output_dir):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    image_width = data["description"]["width"]
    image_height = data["description"]["height"]
    label = data["description"]["type"]  # YOLO 첫 번째 라벨
    
    yolo_annotations = []
    for obj in data["annotations"]["points"]:
        xtl, ytl, xbr, ybr = obj["xtl"], obj["ytl"], obj["xbr"], obj["ybr"]
        
        # YOLO 형식 변환 (x_center, y_center, width, height)
        x_center = (xtl + xbr) / 2 / image_width
        y_center = (ytl + ybr) / 2 / image_height
        bbox_width = (xbr - xtl) / image_width
        bbox_height = (ybr - ytl) / image_height
        
        yolo_annotations.append(f"{label} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")
    
    # 파일명에서 확장자를 제외하고 '.txt'로 저장 (모든 이미지 확장자 제거)
    file_name_without_ext = os.path.splitext(os.path.basename(json_path))[0]
    # 이미지 파일 확장자 처리 (확장자 .jpg, .jpeg, .png, 등 모두 처리)
    if file_name_without_ext.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_name_without_ext = file_name_without_ext.rsplit('.', 1)[0]

    output_file = os.path.join(output_dir, file_name_without_ext + ".txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(yolo_annotations))

def process_json_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            convert_to_yolo(os.path.join(input_dir, filename), output_dir)
    print("변환 완료!")

# 사용 예시 (폴더 경로 설정 필요)
input_directory = r"C:\Users\dounghun\Desktop\gochu_yolo\01.data\2.Validation\labeling\01.gochu\1.질병"
output_directory = "1wlfqud"
process_json_files(input_directory, output_directory)
