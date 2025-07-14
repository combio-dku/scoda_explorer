# SCODA로 분석하는 단일세포 RNA-seq 데이터
## 사전 준비
- __개인 준비:__ &nbsp;&nbsp; 무선랜과 웹브라우저가 설치된 Laptop &nbsp; (Tablet도 가능은 한데 추천하지는 않습니다.)
- __사용 언어:__ &nbsp;&nbsp; python3 &nbsp; (Google Colab을 사용할 예정이라 뭔가 따로 설치할 필요는 없습니다.)
- __발표 자료:__ &nbsp;&nbsp; 따로 이메일로 송부 드립니다.
- __사전 지식:__
  - 생명과학/의학분야에 종사하시면서 단일세포 RNA-seq 기술이 어디에 어떻게 쓰이는지 대략적으로는 알아야 합니다.
  - Python이나 R 사용 경험이 있으면 더 좋습니다.

## 워크샵 진행 순서
1. &nbsp;&nbsp; SCODA를 이용한 단일세포 RNA-seq 분석 개요
3. &nbsp;&nbsp; AnnData 포맷 소개, SCANPY를 이용한 전처리, 세포유형식별 실습
5. &nbsp;&nbsp; CNV와 Ploidy 추정, 세포간 상호작용 분석
7. &nbsp;&nbsp; DEG 분석, 마커탐색, Gene Set Enrichment 분석

## SCODA 간략 소개
- 워크샵 당일날 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다. [(SCODA 소개 발표자료)](https://github.com/combio-dku/scoda_explorer/blob/main/SCODA_%EC%86%8C%EA%B0%9C_BRIC_%EA%B8%B0%EC%97%85%EA%B8%B0%EC%88%A0%EC%9B%A8%EB%B9%84%EB%82%98_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf)

## 실습 준비

1. Google Chrome을 열고 본인의 구글 계정으로 로그인한 후 Google drive에 접속한다.
2. (미리 SCODA로 처리한) [실습 데이터](https://drive.google.com/file/d/1OUWkbAcKE9nfA9YIapY346L-wkJq31zL/view?usp=drive_link)를 다운받는다.
3. 다운받은 실습용 데이터 파일(.tar.gz)을 Google drive의 적당한 폴더에 drag & drop하여 저장한다.
4. [요기](https://colab.research.google.com/drive/1f3PH8CqKp9tDZyRF5dG_GZS_o0DEjEmE)를 클릭하여 실습용 주피터 노트북을 구글 Colab에서 연다.  <a href="https://colab.research.google.com/drive/1f3PH8CqKp9tDZyRF5dG_GZS_o0DEjEmE" target="_blank">Open in Colab</a>

5. Colab 탭 우측 상단의 `연결` 버튼을 눌러 Colab 서버에 연결한다.
6. 좌측 맨아래 `파일` 아이콘을 눌러 파일 뷰어를 연다.
7. 다운받은 데이터 파일을 파일뷰어 영역에 drag & drop 하여 실습용 데이터 파일을 Colab 서버에 업로드한다.
8. 실습용 데이터 파일의 업로드가 완료되었으면 주피터 노트북의 설명에 따라 코드 셀을 하나씩 실행하여 실습을 진행한다.

- __참고 사항:__ 5에서 실습용 주피터노트북 파일을 더블클릭했는데 바로 Google Colab으로 연결되지 않을 경우, 자동 앱연결이 활성화되지 않은 것이므로 실습용 주피터파일을 마우스로 클릭한 후 오른쪽 버튼 클릭 -> 연결앱 클릭 -> 열리는 창에서 'Google Colab'을 검색하여 연결앱으로 설정하면 됩니다.

## 추가 실습: SCODA결과로부터 KEGG pathview 생성하여 확인하기

1. (미리 SCODA로 처리한) [실습용 데이터 파일](https://github.com/combio-dku/KEGGPathviewGen4SCODA/blob/main/data/example_human_brca_12k_results.h5ad.tar.gz)을 다운받는다. (위의 실습용 데이터와 다른 파일임. 우측 상단의 다운로드 버튼을 클릭.) ![image](https://github.com/user-attachments/assets/6292d5ef-40c1-4dcf-a34a-e7375ad41941)
2. [여기](https://colab.research.google.com/github/combio-dku/KEGGPathviewGen4SCODA/blob/main/example_kegg_pathview_gen_for_scoda.ipynb)를 클릭하여 실습용 주피터 노트북 파일을 Google Colab에서 연후 본인 계정의 Google drive에 저장한다 (파일 메뉴 -> Drive에 사본저장). (위의 실습용 주피터 노트북과 다른 R용 노트북임.)
6. Colab 탭 우측 상단의 `연결` 버튼을 눌러 Colab 서버에 연결한다. (Google 계정 로그인 필요)
4. 좌측 맨아래 `파일` 아이콘을 눌러 파일 뷰어를 연다.
5. 다운받은 데이터 파일을 파일뷰어 영역에 drag & drop 하여 실습용 데이터 파일을 Colab 서버에 업로드한다.
6. 실습용 데이터 파일의 업로드가 완료되었으면 주피터 노트북의 코드 셀을 하나씩 실행하여 실습을 진행한다. (이때 Step 0의 패키지 설치도 수행해야 한다.)

- __참고 사항:__ 위의 주피터 노트북과 실습용 데이터 파일은 [KEGG_Pathview_Gen_for_SCODA 페이지](https://github.com/combio-dku/KEGGPathviewGen4SCODA)에서 볼수 있습니다.

<div align="center">
  <img src="https://github.com/combio-dku/KEGGPathviewGen4SCODA/blob/main/images/KEGG_pathview_UC_mac.png" style="width:80%;"/>
</div>
    
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
  
- __참고 사항:__ Optional Input 첫번째인 Optional analysis config file을 따로 입력하지 않을 경우 파이프라인이 Tissue를 자동으로 선택하는데, 이 경우 잘못된 Tissue가 선택되면 세포 유형식별이 부정확할 수 있습니다. 이 경우, Default Configuration 링크를 클릭하여 analysis_config.py 파일을 다운 받고 TISSUE 변수를 'Breast'로 변경한 후 이를 데이터 파일 업로드시 Optional analysis config file 입력창에 넣어 같이 업로드 하면 보다 정확한 결과를 얻을 수 있습니다.  

## 참고 논문 (SCODA 활용 사례)
1. SCODA를 이용한 자가면역질환(궤양성 대장염) 연구: [Integrative analysis of single-cell RNA-seq and gut microbiome metabarcoding data elucidates macrophage dysfunction in mice with DSS-induced ulcerative colitis](https://www.nature.com/articles/s42003-024-06409-w).  SCODA로 분석한 데이터 다운로드: [요기 클릭](https://figshare.com/articles/dataset/SCODA_result_for_GSE264408/28235234)
2. SCODA를 이용한 TNBC 연구: [A Retrospective View of the Triple-Negative Breast Cancer Microenvironment: Novel Markers, Interactions, and Mechanisms of Tumor-Associated Components Using Public Single-Cell RNA-Seq Datasets](https://www.mdpi.com/2072-6694/16/6/1173#)
