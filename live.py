import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO(r"C:\Users\dounghun\Desktop\gochu_yolo\runs\detect\train\weights\best.pt")

# 웹캠 열기 (0은 기본 카메라)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break

    # YOLOv8을 사용하여 객체 감지
    results = model(frame)

    # 결과를 이미지에 반영 (YOLOv8에서는 results[0].plot() 사용)
    annotated_frame = results[0].plot()

    # 화면에 출력
    cv2.imshow("YOLO Real-time Detection", annotated_frame)

    # ESC 키(27번 키)를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
