# SCODA Workshop
- __일시:__ 2025년 1월 23일 (목) 09:30~17:30
- __장소:__ 동국대학교 법학관 2층 B260호 
- __주최:__ (주) 엠엘비아이랩
- __연사:__ 윤석현 교수 (단국대)
- __사용언어:__ python3
- __개별 준비물:__ 웹브라우저가 설치된 PC or Laptop (Tablet도 가능은 한데 추천하지는 않습니다. 브라우저에 따라 결과 파일 다운이 잘 않되는 경우가 있어서)
- __목적:__ SCODA 의 활용법 실습을 통해 단일세포 RNA-seq 데이터 분석 능력을 습득한다.
- __참가자 사전 지식:__
  - 생명과학/의학분야에 종사하시면서 단일세포 RNA-seq 기술이 어디에 어떻게 쓰이는지 대략적으로는 아시는 분.
  - Python이나 R 사용 경험이 있으면 더 좋습니다.
- [발표 자료](https://drive.google.com/file/d/1bMNvaSmhc1oNzGoVD0h1akBZqdL5xhKU/view?usp=sharing)
- 참고 논문1 (SCODA를 이용한 자가면역질환(만성 대장염) 연구): [Integrative analysis of single-cell RNA-seq and gut microbiome metabarcoding data elucidates macrophage dysfunction in mice with DSS-induced ulcerative colitis](https://www.nature.com/articles/s42003-024-06409-w)
- 참고 논문2 (SCODA를 이용한 TNBC 연구): [A Retrospective View of the Triple-Negative Breast Cancer Microenvironment: Novel Markers, Interactions, and Mechanisms of Tumor-Associated Components Using Public Single-Cell RNA-Seq Datasets](https://www.mdpi.com/2072-6694/16/6/1173#)

## 진행 순서
1. __10:30-12:00__  &nbsp;&nbsp; SCODA를 이용한 단일세포 RNA-seq 분석 개요
2. __12:00-13:00__  &nbsp;&nbsp; 점심 식사
3. __13:00-14:20__  &nbsp;&nbsp; AnnData 포맷 소개, SCANPY를 이용한 전처리, 세포유형식별 실습
4. __14:20-14:35__  &nbsp;&nbsp; Break
5. __14:35-15:55__  &nbsp;&nbsp; CNV와 Ploidy 추정, 세포간 상호작용 분석
6. __15:55-16:10__  &nbsp;&nbsp; Break
7. __16:10-17:30__  &nbsp;&nbsp; DEG 분석, 마커탐색, Gene Set Enrichment 분석

## 1. SCODA 간략 소개
- 워크샵 당일날 10분 정도 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다.


## 2. 데이터 준비, SCODA 실행, 주피터 사용하기 (파이썬 간략 소개) (1시간 10분)
1. 사용할 데이터 다운로드: [여기 클릭](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing) (5분)
2. 입력 데이터 포맷팅 소개 (5분)
3. 데이터 업로드 및 SCODA 실행 [SCODA pipeline homepage](https://mlbi-lab.net) (10분)
4. 구글 Colab에서 주피터 노트북 열기: [여기 클릭](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/scoda_viz_practice_workshop.ipynb) (5분)
5. 구글 Colab에 연결 하기 (5분)
6. 파이썬 데이터 구조 간략 소개 및 실습 (30분)
7. SCODA 결과 다운로드 (저장 경로 확인) (5분)
8. Colab서버에 결과 데이터 업로드 (5분)


## [SCODA pipeline](https://mlbi-lab.net) 활용법

1. 사용할 데이터를 다운 받는다. [여기 클릭](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing)
2. SCODA 데모 서버에 접속한다. [SCODA 서버 homepage](https://mlbi-lab.net)
3. Mandatory Input 부분에서 ....
   1. 라디오버튼 중 `Compressed 10x_mtx file sets + (optional) meta_data.csv`를 선택한다.
   2. `파일선택` 버튼을 누르고 다운 받은 파일을 선택한다.
   3. `Species`는 Human으로 `Tumor cell Identification` 은 그대로 놔둔다.
   4. `Submit` 버튼을 눌러 SCODA가 업로드한 데이터를 처리하도록 한다.
   5. 그러면 Progress 창이 뜨고 SCODA 실행 내역이 나타난다. (처리 완료까지 5~10분 소요)
   6. SCODA의 처리가 완료되어 아래 쪽에 `Download Result` 버튼이 나오면 이를 클릭하여 SCODA 결과 파일을 다운 받는다. 
   7. 다운 받은 SCODA 결과 파일을 제공된 주피터 노트북에서 열어 데이터 마이닝을 수행한다.

## 참고 사항
Cell-cell interaction, DEG 및 GSA/GSEA 결과 데이터의 구성

- cell-cell interaction 결과 (`uns['CCI_sample']`)
<img width="320" alt="CCI_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/65982226-cb15-434e-8116-00692e65ab74">

- DEG 결과 (`uns['DEG']`)
<img width="555" alt="DEG_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/8d092dcb-e127-4d13-9f27-4edceeae94a7">

- GSA/GSEA 결과 (`uns['GSA_up']`, `uns['GSA_down']`, `uns['GSEA']`)
<img width="555" alt="GSA_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/1d111fc8-ecaf-4f57-b0b9-94102b891498">


