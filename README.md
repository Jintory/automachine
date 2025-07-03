![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=200&section=header&text=Automachine&fontSize=70)

<h1 align="center">🤖 Automachine</h1>
<p align="center">Python CaptchaCracker 보안문자 인식 모델</p>

---
## CaptchaCracker
CaptchaCracker is an open source Python library that provides functions to create and apply deep learning models for Captcha Image recognition. You can create a deep learning model that recognizes numbers in the Captcha Image as shown below and outputs a string of numbers, or you can try the model yourself.

CaptchaCracker는 Captcha Image 인식을 위한 딥 러닝 모델 생성 기능과 적용 기능을 제공하는 오픈소스 파이썬 라이브러리입니다. 아래와 같은 Captcha Image의 숫자를 인식해 숫자 문자열을 출력하는 딥 러닝 모델을 만들거나 모델을 직접 사용해볼 수 있습니다.

### Input
![target (1)](https://github.com/user-attachments/assets/57e5c032-d05c-45ef-9180-e82f5f596b29)
### Output
```
729057
```

## 진행 과정
- 자동방지를 뚫기 위한 사이트의 Sample Data 수집 (100여개 정도)
- 수집한 Sample Data를 학습할 수 있도록 파일명 변경
- 머신러닝을 통한 Sample Data 반복학습
- 학습 결과 파일을 통해 실제 사이트 자동방지 문자 인식

## 테스트를 위한 준비 과정
- CaptchaCracker 모듈
- numpy(ver 1.19.5), tensorflow(ver 2.5.0) 모듈
- ver 3.9 이하의 Python (3.9.7 추천)
- 학습할 Sample Data

### Installation
```
pip install CaptchaCracker
```

### Dependency
```
pip install numpy==1.19.5 tensorflow==2.5.0
```
