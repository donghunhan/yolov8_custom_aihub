# Yolov8_AI_HUB를 활용한 노지작물(고추) dataset object detection(local)
## 저는 anaconda 환경 python 3.8.19(20)에서 실행하였습니다.
### 데이터 파일은 너무커서 안올렸습니다 링크따라서 다운로드 하시면됩니다.

사용 데이터 : https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=147

![alt text](readmeimage\image.png)

(원천데이터)

![alt text](readmeimage\image-1.png)

(라벨링 데이터)

![alt text](readmeimage\image-2.png)

(다운로드 파일)
# 다운로드파일 git bash로 열어주기 or Vs code에서 터미널-터미널분할-git bash 실행
![alt text](readmeimage\image-3.png)

tar -xvf aaa.tar -> AI Hub데이터들은 tar파일로 분할 압축 되어있다 이렇게 풀면 part 파일이 생성되는데 분할이 되어있으면

파일이 2개로 나눠져 있으므로 하나의 파일로 합쳐줘야한다

![alt text](readmeimage\image-4.png)

cat AI_HUBpart파일.zip.part* > backup.tgz 같은걸로 합쳐줘야한다. -> 이걸 반디집으로 압축해제 해주면됌

![alt text](readmeimage\image-5.png)
폴더가 생기고 안에 들어가보면 
![alt text](readmeimage\image-6.png)
구성이 되어있다. 이걸 전부 반복한다음 압축해제해서 파일을 모아두자

### 파일 구성을 다하였으면 label폴더의 구성이 json 형식이다 이걸 yolo형식의 label로 변경할 필요가 있다.
![alt text](readmeimage\image-7.png)

![alt text](readmeimage\image-8.png)
![alt text](readmeimage\image-9.png)

여기서는 질병인지 아닌지만 구분할려고 type의 0과 1만을 활용하고 json 파일의 주목 객체의 bbox 좌표(points)들을 
yolov8형태의 형식으로 나눌 필요가 있다. 
제공되는 [json_to_txt](json_to_txt.py)를 사용하면 쉽게 바꿀수 있다.(경로지정은 필수)

이미지 파일들은 yolo_images 폴더안에(good,wlfqud,wmdrkd) 으로 만들고
라벨 파일들은 yolo_labels 폴더안에(good,wlfqud,wmdrkd) 으로 만들어준다
![alt text](readmeimage\image10.png)

또한 동일폴더에 train\images(labels), valid\images(labels), test\images(labels) 의폴더 총 6개를 만들어준다

![alt text](readmeimage\image11.png)

이후 폴더내에 data.yaml파일을 하나만든다

data.yaml 구성//

train: C:\Users\dounghun\Desktop\gochu_yolo\train\images < 학습 이미지 경로

val: C:\Users\dounghun\Desktop\gochu_yolo\valid\images   < 검증 이미지 경로

test: C:\Users\dounghun\Desktop\gochu_yolo\test\images   < 테스트 이미지 경로

nc: 2 (클래스 수)

names: (클래스 이름)

0: good

1: wlfqud //여기까지 data.yaml구성


이후 yolov8_gochu.ipynb 파일을 하나씩 실행시켜준다