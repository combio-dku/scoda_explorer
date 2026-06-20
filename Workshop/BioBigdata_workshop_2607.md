## 범부처통합바이오헬스협회 바이오전문인력양성 과정: 
# 바이오 빅데이터 분석
- __교육 목표:__ &nbsp;&nbsp; 기계학습과 인공신경망 모형을 바이오 빅데이터 분석에 활용하기 위한 이론과 실습을 제공하고 소규모 프로젝트의 수행을 통해 수강생들이 이를 실제 데이터 분석에 스스로 활용할 수 있도록 한다
- __교육 대상:__ &nbsp;&nbsp; 생명과학/의학분야 학부 졸업생, 대학원생, 관련분야 연구원.

## 사전 준비
- __개인 준비:__ &nbsp;&nbsp; 무선랜과 웹브라우저가 설치된 Laptop &nbsp; (Tablet도 가능은 한데 추천하지는 않습니다.)
- __사용 언어:__ &nbsp;&nbsp; python3 &nbsp; (Google Colab을 사용할 예정이라 뭔가 따로 설치할 필요는 없습니다.)
- __발표 자료:__ &nbsp;&nbsp; 따로 이메일로 송부 드립니다.
- __사전 지식:__
  - __필수:__ 생명과학/생화학에 대한 기본 지식(관련/유사 학과 전공자)
  - __필수:__ Python coding 문법, 함수정의 및 다양한 자료 구조에 대한 기초 지식
  - __권장:__ 학부 비전공자 수준의 통계학 (기초 통계량과 통계검정 등)
  - __권장:__ 학부 비전공자 수준의 선형대수 (벡터 행렬) 

## 실습 자료
1. &nbsp;&nbsp; Python, pandas bridge practice [실습 1 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_1_python_pandas_bridge_practice.ipynb)
2. &nbsp;&nbsp; 항암제 반응성 예측 (유전자 반현량 기반) [실습 2A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_2A_regression_practice.ipynb)
3. &nbsp;&nbsp; 항암제 반응성 예측 (유전자 반현량 + 변이 정보 기반) [실습 2B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_2B_regression_practice_with_mutation.ipynb)
4. &nbsp;&nbsp; 혈액 바이오마커 기반 암진단 및 암종판별 [실습 3A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_3A_classification_practice_cancerseek.ipynb)
5. &nbsp;&nbsp; 유방암 수용체 상태 판별 (유전자 반현량 기반) [실습 3B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_3B_classification_practice_tcga_brca.ipynb)
6. &nbsp;&nbsp; 혈액 바이오마커 기반 암진단 및 암종판별을 위한 인공 신경망 응용 [실습 4A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_4A_ANN_classifier_cancerseek.ipynb) 
7. &nbsp;&nbsp; 항암제 반응성 예측을 위한 인공 신경망 응용 (유전자 반현량 + 변이 정보 기반) [실습 4B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_4B_ANN_regressor_ccle_ctrpv2.ipynb)
8. &nbsp;&nbsp; Transformer 모형을 이용한 작은 분자 표현 학습 (SMILES code 기반) [실습 5A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_5A_qm9_smiles_representation_learning.ipynb)
9. &nbsp;&nbsp; 분자 임베딩을 이용한 항암제 반응성 예측 [실습 5B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_5B_ANN_regressor_ccle_ctrpv2_with_embedding.ipynb)

## 사용할 데이터 셋
1. &nbsp;&nbsp; [__CCLE:__](https://depmap.org/portal/) 암세포주 유전자 발현량 데이터 
1. &nbsp;&nbsp; __CTRP-v2:__ 암세포주 대상 항암제 반응설 측정 데이터 [https://depmap.org/portal/](https://portals.broadinstitute.org/ctrp.v2/)
2. &nbsp;&nbsp; __CancerSEEK data:__ 39개 혈액 바이오마커 측정 데이터  https://www.science.org/doi/10.1126/science.aar3247
3. &nbsp;&nbsp; __TCGA-BRCA cohort:__ Gene/Transcript expression, mutation profiles, CNVs ... for 1092 cancer tissue and 120 adjacent normal. http://firebrowse.org/?cohort=BRCA 
4. &nbsp;&nbsp; __Quantum Machine 9 (QM9):__ 133,885 저분자 화합물에 대한 SMILES code 및 분자 특성 측정 데이터 https://www.kaggle.com/datasets/zaharch/quantum-machine-9-aka-qm9


