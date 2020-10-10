# python-crawling-class

## 1. 웹 크롤링 기본

- 크롤링 사이트:  https://www.tripadvisor.co.kr/Restaurants-g294197-Seoul.html

- 참고 소스코드: [주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/01_tripadvisor_crawling_class.ipynb)

  

#### 크롤링 절차

1. 사이트의 html을 읽어들이기: requests.get(url) 사용
2. 텍스트 형태의 데이터를 html 태그별로 구분하여 파싱하기 : BeutifulSoup
3. 특정 태그값만 찾기 : findAll, find
4. 필요한 데이터값 정제하기
  - 광고 상품 제거하기
5. 데이터프레임 형태로 만들기







## 2. 여러 웹 페이지 웹 크롤링

- 크롤링 사이트:  [https://www.coupang.com](https://www.coupang.com/)
- 참고 소스코드:  [주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/02_coupang_class.ipynb)



#### 크롤링 절차

1. 사이트의 html을 읽어들이기: requests.get(url) 사용
   - 헤더 설정: http://www.useragentstring.com/
   - url 주소(GET 방식) 형식을 이해하기

2. 텍스트 형태의 데이터를 html 태그별로 구분하여 파싱하기 : BeutifulSoup

3. 특정 태그값만 찾기 : findAll, find

4. 필요한 데이터값 정제하기
   - 광고 상품 제거하기

5. 데이터 저장하기
   - csv 형식으로 저장하기







## 3. 동적 웹 크롤링, selenium

- 크롤링 사이트:  https://www.tripadvisor.co.kr/Restaurants-g294197-Seoul.html
- 참고 소스코드: [[주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/03_tripadvisor_image_crawling_by_selenium_class.ipynb)]



#### 사전준비

- selenium(동적으로 화면을 업데이트하는 패키지) 설치

  - pip install selenium

- 크롬 웹드라이버 설치

  

#### 크롤링 절차

1. 브라우저를 직접 실행해서 사이트의 html을 읽어들이기

   - options.headless = True (크롬을 백그라운드에서 실행)

2. 크롬창을 직접 오픈해서 html 페이지를 받아옴

3. 테스트 형태의 데이터를 html 태그별로 구분하여 파싱하기  : BeutifulSoup

4. 특정 태그값 찾기  : findAll, find필요한 데이터값 정제하기

5. 이미지 데이터 저장하기

   - 폴더에 이미지 데이터 다운로드 받기








## 4. 파일 다운로드 받기, GET방식, POST 방식의 이해

- 크롤링 사이트:  [http://marketdata.krx.co.kr](http://marketdata.krx.co.kr/)
- 참고 소스코드: [주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/04_%ED%95%9C%EA%B5%AD%EA%B1%B0%EB%9E%98%EC%86%8C_class.ipynb)



#### 크롤링 절차

1. 브라우저 > 검사 > 네트워크 탭 실행
2. 다운로드 받을 파일 선택
3. request 정보 값 설정
4. response 값 저장
5. 두번째 request를 첫번째 response값을 활용하여 설정
6. response 데이터를 엑셀로 저장(byte를 excel로 변환)







## 5. OpenAPI 활용, Youtube API

- 크롤링 사이트:  [http://marketdata.krx.co.kr](http://marketdata.krx.co.kr/)
- 참고 소스코드: [주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/05_youtube_api.ipynb)



#### 사전준비

- Youtube AI KEY 발급
- google api, oauth2client설치

```
    pip install google-api-python-client
    pip install oauth2client
```



#### 크롤링 절차

1. URL build
2. search() 실행
3. response 파싱
   - json 파싱
4. 엑셀에 데이터 저장







## 6. OpenAPI 활용, 공공데이터

- 크롤링 사이트:  https://www.data.go.kr/
- 참고 소스코드: [주피터노트북](https://github.com/zzhining/python-crawling-class/blob/master/06_%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A7%A4%EB%A7%A4%20%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_class.ipynb)



#### 사전준비

- 공공데이터포털 회원가입
- '아파트매매 실거래자료'검색
- OPEN API에서 XML 형태로 제공하는 항목 선택
- 활용 신청 > 기타
- 마이페이지 > 일반 인증키(UTF-8), End Point, hwp 문서 확인



#### 크롤링 절차

1. URL request
2. response 데이터 파싱(json)
3. csv 형태로 저장









## 7. 미니프로젝트



### 1) 파일 업로드 주소

https://drive.google.com/drive/folders/1m31dQLt6MP4G8S4KBHOIOj91hyJGDLRO?usp=sharing

 ##### 파일명 형태: ㅇㅇ분석_이름

       네이버주가분석_홍길동.ipynb    
       네이버주가분석_홍길동.pptx



### 2) 업데이트 파일
* 파이썬 소스코드(.py or ipynb)   : 예:    네이버주가분석_홍길동.ipynb  
* 보고서(자유양식)                         : 예:    네이버주가분석_홍길동.pptx
      - 포함내용: 크롤링한 사이트 url
          - 어려웠던 점
      - 새로 시도해본 내용 등

 
