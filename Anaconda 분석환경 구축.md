# Anaconda 분석 환경 구축
## Anaconda 설치 및 실행
1. &nbsp;&nbsp; [여기](https://www.anaconda.com/download/success)에서 Anaconda individual edition을 다운 받습니다. (OS에 맞는 적당한 것을 다운 받되 Windows나 Mac의 경우 64-Bit Graphical Installer를 추천합니다.)
3. &nbsp;&nbsp; 다운받은 설치파일을 실행시켜 Anaconda을 설치합니다. (동의를 한번하고 Next 버튼을 몇번 누르고 Install 버튼을 누르면 됩니다.)
5. &nbsp;&nbsp; 설치가 완료되면 Windows의 경우 시작 메뉴에, Mac의 경우 응용 프로그램(Applications)에 "Anaconda Navigator" 가 생깁니다.
7. &nbsp;&nbsp; "Anaconda Navigator"를 실행하면 창이 하나 뜨고 "JupyterLab"과 "Jupyter Notebook" 패널이 보입니다.
8. "JupyterLab"과 "Jupyter Notebook" 둘 중 하나를 클릭하면 터미털 창이 먼저 하나 뜨고 이 후 브라우저기 뜨면서 주피터 창이 열리는데 그러면 사용 준비가 된 것입니다.

![image](https://github.com/user-attachments/assets/1b0dcf77-fbd0-4e1f-8459-a5467f935c3c)

- 참고로 터미널 창을 확인해 보면 Command propt 앞에 "(base)"라는 글자가 보이는데 이는 Conda 환경 이름으로 현재 "base" conda 환경에서 실행되고 있음을 나타냅니다.
- "base" conda 환경에는 기본적인 python package들이 깔려 있어 이 환경에서 python을 사용해도 무방합니다.
- 다만 다양한 conda 환경을 만들어 사용하고자 한다면 [여기]()를 참고하여 conda 환경을 생성하고 필요한 패키지를 설치하여 사용하면 됩니다.
- 

## SCODA 간략 소개
- 워크샵 당일날 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다. [(SCODA 소개 발표자료)](https://github.com/combio-dku/scoda_explorer/blob/main/SCODA_%EC%86%8C%EA%B0%9C_BRIC_%EA%B8%B0%EC%97%85%EA%B8%B0%EC%88%A0%EC%9B%A8%EB%B9%84%EB%82%98_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf)

## 실습 준비

1. Google Chrome을 열고 본인의 구글 계정으로 로그인한 후 Google drive에 접속한다.
2. (미리 SCODA로 처리한) [실습 데이터](https://drive.google.com/file/d/1OUWkbAcKE9nfA9YIapY346L-wkJq31zL/view?usp=drive_link)를 다운받는다.
3. [실습용 주피터 노트북](https://drive.google.com/file/d/1f3PH8CqKp9tDZyRF5dG_GZS_o0DEjEmE/view?usp=drive_link)을 다운받는다.
4. 다운받은 실습용 데이터 파일(.tar.gz)과 실습용 주피터노트북 파일(.ipynb)을 Google drive의 적당한 폴더에 drag & drop하여 저장한다.
5. Google drive에서, 업로드한 실습용 주피터노트북 파일을 더블클릭하면 Google Colab에서 자동으로 열린다.
6. Colab 탭 우측 상단의 `연결` 버튼을 눌러 Colab 서버에 연결한다.
7. 좌측 맨아래 `파일` 아이콘을 눌러 파일 뷰어를 연다.
8. 다운받은 데이터 파일을 파일뷰어 영역에 drag & drop 하여 실습용 데이터 파일을 Colab 서버에 업로드한다.
9. 실습용 데이터 파일의 업로드가 완료되었으면 주피터 노트북의 설명에 따라 코드 셀을 하나씩 실행하여 실습을 진행한다.

