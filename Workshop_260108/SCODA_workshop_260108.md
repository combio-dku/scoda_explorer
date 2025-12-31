## SCODA Workshop 2026.01.08
# 단일세포 RNA-seq 데이터를 이용한 종양/조직 미세환경 분석과 치료 표적 발굴 (실습 자료)

## 사전 준비
- __개인 준비:__ &nbsp;&nbsp; 무선랜과 웹브라우저가 설치된 Laptop &nbsp; (Tablet도 가능은 한데 추천하지는 않습니다.)
- __사용 언어:__ &nbsp;&nbsp; python3 &nbsp; (Google Colab을 사용할 예정이라 뭔가 따로 설치할 필요는 없습니다.)
- __발표 자료:__ &nbsp;&nbsp; 따로 이메일로 송부 드립니다.
- __사전 지식:__
  - 생명과학/의학분야에 종사하시면서 단일세포 RNA-seq 기술이 어디에 어떻게 쓰이는지 대략적으로는 알아야 합니다.
  - Python이나 R 사용 경험이 있으면 더 좋습니다.
  - 단일세포 RNA-seq 데이터 분석관련 실습 워크샵같은 걸 수강한 경험이 있다면 제일 좋고요.
  - __추천 워크샵:__ 한국유전체학회 통계유전학 워크샵(매년 7월), 한국생명정보학회 BIML 워크샵 (매년 2월, 8월)

## 워크샵 진행 순서
1. &nbsp;&nbsp; 실습I: AnnData 포맷 소개 및 SCANPY 활용법 실습
2. &nbsp;&nbsp; SCODA를 이용한 단일세포 RNA-seq 분석 개요
3. &nbsp;&nbsp; 실습II: SCODA를 이용한 연구사례 I (3가지 암의 종양미세환경 프로파일링 및 표적발굴)
4. &nbsp;&nbsp; 실습III: SCODA를 이용한 연구사례 II (궤양성 대장염 조직미세환경 프로파일링 및 치료표적발굴)
5. &nbsp;&nbsp; 실습IV: KEGG Pathview 생성 및 pathway 변화 시각화 및 분석 실습 

## SCODA 간략 소개
- 워크샵 당일날 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다. [(SCODA 소개 발표자료)](https://github.com/combio-dku/scoda_explorer/blob/main/SCODA_pipeline_description.pdf)

## 실습 I: AnnData Format 소개 및 SCANPY 활용

1. (Ctrl +) [요기를 클릭](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_1_scanpy_practice_251228.ipynb)하여 실습용 주피터 노트북을 구글 Colab에서 연다.  
2. Colab 탭 우측 상단의 `연결` 버튼을 눌러 Colab 서버에 연결한다. (필요시, 구글계정으로 로그인한다.)
3. 열린 주피터 노트북에서 코드셀을 하나씩 실행하여 실습을 진행한다. 

## 실습 II & III: SCODA를 이용한 연구사례

1. __실습 II:__  실습용 주피터 노트북을 (Ctrl + 클릭하여) 구글 Colab에서 열고 실습을 진행한다.
   - [Breast Cancer dataset](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_2A_BC_251228.ipynb)
   - [NSCLC dataset](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_2B_NSCLC_251228.ipynb)
   - [PDAC dataset](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_2C_PDAC_251228.ipynb)
3. __실습 III:__ (Ctrl +) 실습용 주피터 노트북을 (Ctrl + 클릭하여) 구글 Colab에서 열고 실습을 진행한다.
   - [Colitis dataset (mm)](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_3A_Colitis_mm_251228.ipynb)
   - [Colitis dataset (hs)](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_3B_Colitis_hs_251228.ipynb)
   - [Brain dataset](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_3C_Brain_251228.ipynb)

## 실습 IV: KEGG Pathview 생성 및 pathway 변화 시각화 및 분석 실습

1. (Ctrl +) [요기를 클릭](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Workshop_260108/scoda_practice_workshop_4_KEGG_pathview_250810.ipynb)하여 실습용 주피터 노트북을 구글 Colab에서 연다. __(요건 R을 사용하는 주피터 노트북입니다.)__ 
2. Colab 탭 우측 상단의 `연결` 버튼을 눌러 Colab 서버에 연결한다. (필요시, 구글계정으로 로그인한다.)
3. 열린 주피터 노트북에서 코드셀을 하나씩 실행하여 실습을 진행한다. (이때 Step 0의 패키지 설치도 수행해야 하는데 설치 시간이 10~15분 정도 소요됨.)

- __참고 사이트:__  [KEGG_Pathview_Gen_for_SCODA](https://github.com/combio-dku/KEGGPathviewGen4SCODA) 

<div align="center">
  <img src="https://github.com/combio-dku/KEGGPathviewGen4SCODA/blob/main/images/KEGG_pathview_UC_mac.png" style="width:90%;"/>
</div>
    
## SCODA pipeline 사용해보기

1. [사용할 데이터](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing)를 다운 받는다. 
2. [SCODA 데모 페이지](https://mlbi-lab.net)에 접속한다. 
3. Mandatory Input 부분에서 ....
   1. 라디오버튼 중 `Compressed 10x_mtx file sets + (optional) meta_data.csv`를 선택한다.
   2. `파일선택` 버튼을 누르고 다운 받은 파일을 선택한다.
   3. `Species`는 Human으로 `Tumor cell Identification` 은 그대로 놔둔다.
   4. `Submit` 버튼을 눌러 SCODA가 업로드한 데이터를 처리하도록 한다.
   5. 그러면 Progress 창이 뜨고 SCODA 실행 내역이 나타난다. (처리 완료까지 5~10분 소요)
   6. SCODA의 처리가 완료되어 아래 쪽에 `Download Result` 버튼이 나오면 이를 클릭하여 SCODA 결과 파일을 다운 받는다. 
   7. 다운 받은 SCODA 결과 파일을 제공된 주피터 노트북에서 열어 위 실습내용을 응용하여 데이터 마이닝을 수행한다.
  
- __참고 사항:__ Optional Input 첫번째인 Optional analysis config file을 따로 입력하지 않을 경우 파이프라인이 Tissue를 자동으로 선택하는데, 이 경우 잘못된 Tissue가 선택되면 세포 유형식별이 부정확할 수 있습니다. 이 경우, Default Configuration 링크를 클릭하여 analysis_config.py 파일을 다운 받고 TISSUE 변수를 'Breast'로 변경한 후 이를 데이터 파일 업로드시 Optional analysis config file 입력창에 넣어 같이 업로드 하면 보다 정확한 결과를 얻을 수 있습니다. [analysis_config.py 예제 파일](https://github.com/combio-dku/scoda_explorer/blob/main/Workshop/analysis_config_breast.py) 참고

## 참고 논문 (SCODA 활용 사례)
1. SCODA를 이용한 자가면역질환(궤양성 대장염) 연구: [Integrative analysis of single-cell RNA-seq and gut microbiome metabarcoding data elucidates macrophage dysfunction in mice with DSS-induced ulcerative colitis](https://www.nature.com/articles/s42003-024-06409-w). 
2. SCODA를 이용한 TNBC 연구: [A Retrospective View of the Triple-Negative Breast Cancer Microenvironment: Novel Markers, Interactions, and Mechanisms of Tumor-Associated Components Using Public Single-Cell RNA-Seq Datasets](https://www.mdpi.com/2072-6694/16/6/1173#)
