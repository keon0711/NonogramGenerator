# NonogramGenerator
## 개요
기존에 존재하는 이미지 파일을 이용해 원하는 노노그램 퍼즐을 만들 수 있다.

이미지 파일을 Edge detection과 Thresholding 등의 이미지 프로세싱을 통해 2bit 이미지로 변환한다.

노노그램은 pygame을 통해 구현했다.


## 사용방법
1. image 폴더 안에 만들고 싶은 이미지 파일을 저장한다.
2. nonogram.py 파일에서 get_image() 함수로 해당 이미지를 선택한다.
```
get_image('원하는 파일 이름', 크기 비율, erosion 반복횟수)
```
3. 변환된 이미지를 통해 만들어진 노노그램은 푼다.


## 예시
원본이미지

![image](https://user-images.githubusercontent.com/110909423/195649370-61a33abc-857c-47b2-b449-32a183716451.png)

생성된 노노그램

![image](https://user-images.githubusercontent.com/110909423/195651807-5e427c1a-854a-491d-b715-9d4b98e17949.png)
