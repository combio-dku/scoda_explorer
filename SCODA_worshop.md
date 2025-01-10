# SCODA Workshop
- __일시:__ &nbsp;&nbsp; 2025년 1월 23일 (목) 09:30~17:30
- __장소:__ &nbsp;&nbsp; 동국대학교 법학관 2층 B260호 
- __주최:__ &nbsp;&nbsp; (주) 엠엘비아이랩
- __연사:__ &nbsp;&nbsp; 윤석현 교수 (단국대)
- __목적:__ &nbsp;&nbsp; SCODA 의 활용법 실습을 통해 단일세포 RNA-seq 데이터 분석 능력을 습득한다.
<br></br>
- __개인 준비:__ &nbsp;&nbsp; 무선랜과 웹브라우저가 설치된 Laptop (Tablet도 가능은 한데 추천하지는 않습니다.)
- __사용 언어:__ &nbsp;&nbsp; python3
- __사전 지식:__
  - 생명과학/의학분야에 종사하시면서 단일세포 RNA-seq 기술이 어디에 어떻게 쓰이는지 대략적으로는 아시는 분.
  - Python이나 R 사용 경험이 있으면 더 좋습니다.
<br></br>
- [__발표 자료 다운로드__](https://shorturl.at/LTkOL)


## 워크샵 진행 순서
1. &nbsp;&nbsp;__10:30-12:00__  &nbsp;&nbsp; SCODA를 이용한 단일세포 RNA-seq 분석 개요
2. &nbsp;&nbsp;__12:00-13:00__  &nbsp;&nbsp; 점심 식사
3. &nbsp;&nbsp;__13:00-14:20__  &nbsp;&nbsp; AnnData 포맷 소개, SCANPY를 이용한 전처리, 세포유형식별 실습
4. &nbsp;&nbsp;__14:20-14:35__  &nbsp;&nbsp; Break
5. &nbsp;&nbsp;__14:35-15:55__  &nbsp;&nbsp; CNV와 Ploidy 추정, 세포간 상호작용 분석
6. &nbsp;&nbsp;__15:55-16:10__  &nbsp;&nbsp; Break
7. &nbsp;&nbsp;__16:10-17:30__  &nbsp;&nbsp; DEG 분석, 마커탐색, Gene Set Enrichment 분석

## SCODA 간략 소개
- 워크샵 당일날 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다.

## 실습 준비

1. (미리 SCODA로 처리한) [실습 데이터](https://shorturl.at/Rzq8K)를 다운받는다.
2. [실습용 주피터 노트북](https://shorturl.at/bduMm)을 다운받는디.
3. Google Chrome을 열고 본인의 구글 계정으로 로그인한 후 본인의 Google drive에 접속한다.
4. 다운받은 실습용 데이터 파일(.tar.gz)과 실습용 주피터노트북 파일(.ipynb)을 Google drive의 적당한 폴더에 저장한다.
5. Google drive에서, 업로드한 실용용 주피터노트북 파일을 더블클릭하면 Google Colab에서 자동으로 열린다.
6. Google Colab에서 실습용 주피터 노트북이 열렸으면 실습 준비 끝.

- 5에서 실용용 주피터노트북 파일을 더블클릭했는데 바로 Google Colab으로 연결되지 않을 경우, 자동 앱연결이 활성화되지 않은 것이므로 실습용 주피터파일을 마우스로 클릭한 후 오른쪽 버든 -> 연결앱 클릭 -> 열리는 창에서 Google Colab을 검색하여 설정하면 됩니다.

## 추가 실습: SCODA결과로부터 KEGG pathview 생성하여 확인하기

1. (미리 SCODA로 처리한) [실습용 데이터 파일](https://github.com/combio-dku/KEGGPathviewGen4SCODA/blob/main/data/example_human_brca_12k_results.h5ad.tar.gz)을 다운받는다.
2. [여기](https://colab.research.google.com/github/combio-dku/KEGGPathviewGen4SCODA/blob/main/example_kegg_pathview_gen_for_scoda.ipynb)를 클릭하여 실습용 주피터 노트북 파일을 Google Colab에서 연다.
3. Colab 탭 우측 상단의 '연결' 버튼을 눌러 Colab 서버에 연결한다.
4. 좌측 맨아래 '파일' 아이콘을 눌러 파일 뷰어를 연다.
5. 다운받은 데이터 파일을 파일뷰어 영역에 drag & drop 하여 실습용 데이터 파일을 Colab 서버에 업로드한다.
6. 실습용 데이터 파일의 업로드가 완료되었으면 주피터 노트북의 코드 셀을 하나씩 실행하여 실습을 진행한다. (이때 Step 0의 패키지 설치도 수행해야 한다.)

- 참고로 위의 주피터 노트북과 실습용 데이터 파일은 [KEGG_Pathview_Gen_for_SCODA 페이지](https://github.com/combio-dku/KEGGPathviewGen4SCODA)에서 볼수 있다.
    
## SCODA pipeline 사용해보기

1. [사용할 데이터](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing)를 다운 받는다. 
2. [SCODA 데모 서버 홈페이지](https://mlbi-lab.net)에 접속한다. 
3. Mandatory Input 부분에서 ....
   1. 라디오버튼 중 `Compressed 10x_mtx file sets + (optional) meta_data.csv`를 선택한다.
   2. `파일선택` 버튼을 누르고 다운 받은 파일을 선택한다.
   3. `Species`는 Human으로 `Tumor cell Identification` 은 그대로 놔둔다.
   4. `Submit` 버튼을 눌러 SCODA가 업로드한 데이터를 처리하도록 한다.
   5. 그러면 Progress 창이 뜨고 SCODA 실행 내역이 나타난다. (처리 완료까지 5~10분 소요)
   6. SCODA의 처리가 완료되어 아래 쪽에 `Download Result` 버튼이 나오면 이를 클릭하여 SCODA 결과 파일을 다운 받는다. 
   7. 다운 받은 SCODA 결과 파일을 제공된 주피터 노트북에서 열어 데이터 마이닝을 수행한다.

## 참고 논문
1. (SCODA를 이용한 자가면역질환(만성 대장염) 연구): [Integrative analysis of single-cell RNA-seq and gut microbiome metabarcoding data elucidates macrophage dysfunction in mice with DSS-induced ulcerative colitis](https://www.nature.com/articles/s42003-024-06409-w)
2. (SCODA를 이용한 TNBC 연구): [A Retrospective View of the Triple-Negative Breast Cancer Microenvironment: Novel Markers, Interactions, and Mechanisms of Tumor-Associated Components Using Public Single-Cell RNA-Seq Datasets](https://www.mdpi.com/2072-6694/16/6/1173#)
