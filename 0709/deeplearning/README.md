## 방법1) Local 개발환경 셋팅

#### 텐서플로우 설치
 * command에서 실행 시: pip install tensorflow
 * 주피터노트북에서 실행 시: conda install tensorflow

#### 텐서플로우 버전체크
 import tensorflow as tf
 print(tf.__version__)
 >>2.2.0

#### keras 설치
 * command에서 실행 시: pip install keras
 * 주피터노트북에서 실행 시: conda install keras
 
#### 윈도우에서 설치시, 추가 설치
 1) 구글에서 'tensorflow install' 검색 
 2) https://www.tensorflow.org/install/pip?hl=ko 
 3) vc_redist.x64.exe 다운로드
     Windows 7 이상(64비트)(Python 3만 해당)   
     Visual Studio 2015, 2017 및 2019용 Microsoft Visual C++ 재배포 가능 패키지


## 방법2) colab 실행(클라우드 기반)
  https://colab.research.google.com/
