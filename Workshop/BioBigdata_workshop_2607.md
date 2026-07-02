## 범부처통합바이오헬스협회 (KOTHEA) 바이오전문인력양성 과정: 
# 바이오 빅데이터 분석 Workshop
- __교육 대상:__ &nbsp;&nbsp; 생명과학/의학분야 학부 졸업생, 대학원생, 관련분야 연구원 (범부처통합바이오헬스협회 바이오전문인력양성 과정 수강생)
- __교육 목표:__ &nbsp;&nbsp; 기계학습과 인공신경망 모형을 바이오 빅데이터 분석에 활용하기 위한 이론과 실습을 제공하고 소규모 프로젝트의 수행을 통해 실제 데이터 분석에 스스로 활용할 수 있도록 한다

## 사전 준비
- __개인 준비:__ &nbsp;&nbsp; 무선랜과 웹브라우저가 설치된 Laptop (Tablet도 가능은 한데 추천하지는 않습니다), __Google 계정__
- __사용 언어:__ &nbsp;&nbsp; python3 &nbsp; (Google Colab을 사용할 예정이라 뭔가 따로 설치할 필요는 없습니다.)
- __발표 자료:__ &nbsp;&nbsp; 따로 이메일로 송부 드립니다.
- __사전 지식:__
  - __필수:__ 생명과학/생화학에 대한 기본 지식(관련/유사 학과 전공자)
  - __필수:__ Python coding 문법, 함수정의 및 다양한 자료 구조에 대한 기초 지식
  - __권장:__ 학부 비전공자 수준의 통계학 (기초 통계량과 통계검정 등)
  - __권장:__ 학부 비전공자 수준의 선형대수 (벡터 행렬) 

## 실습 자료
1. &nbsp;&nbsp; [실습 1A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_1A_python_pandas_visualization_practice.ipynb): Python, pandas bridge practice 및 데이터 시각화
2. &nbsp;&nbsp; [실습 1B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_1B_stats_dimred_clustering_imputation_practice.ipynb): 통계검정, 상관분석, 차원축소, 군집화, 결측치 처리
3. &nbsp;&nbsp; [실습 2A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_2A_regression_practice.ipynb): 항암제 반응성 예측 (유전자 반현량 기반) 
4. &nbsp;&nbsp; [실습 2B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_2B_regression_practice_with_mutation.ipynb): 항암제 반응성 예측 (유전자 반현량 + 변이 정보 기반) 
5. &nbsp;&nbsp; [실습 3A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_3A_classification_practice_cancerseek.ipynb): 혈액 바이오마커 기반 암진단 및 암종판별 
6. &nbsp;&nbsp; [실습 3B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_3B_classification_practice_tcga_brca.ipynb): 유방암 수용체 상태 판별 (유전자 발현량 기반)
7. &nbsp;&nbsp; [실습 4A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_4A_ANN_classifier_cancerseek.ipynb): 혈액 바이오마커 기반 암진단 및 암종판별을 위한 인공 신경망 응용
8. &nbsp;&nbsp; [실습 4B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_4B_ANN_regressor_ccle_ctrpv2.ipynb): 항암제 반응성 예측을 위한 인공 신경망 응용 (유전자 발현량 + 변이 정보 기반)
9. &nbsp;&nbsp; [실습 5A 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_5A_qm9_smiles_representation_learning.ipynb): Transformer 모형을 이용한 작은 분자 표현 학습 (SMILES code 기반)
10. &nbsp;&nbsp; [실습 5B 주피터 노트북](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/bio_bigdata_workshop_5B_ANN_regressor_ccle_ctrpv2_with_embedding.ipynb): 분자 임베딩을 이용한 항암제 반응성 예측

## 사용할 데이터 셋
1. &nbsp;&nbsp; [__CCLE:__](https://depmap.org/portal/) 800종 이상의 암세포주 유전자 발현량 데이터 
1. &nbsp;&nbsp; [__CTRP-v2:__](https://portals.broadinstitute.org/ctrp.v2/) 800종 이상의 암세포주 대상 500종 이상의 저분자 항암제의 반응성 측정 데이터 
2. &nbsp;&nbsp; [__CancerSEEK data:__](https://www.science.org/doi/10.1126/science.aar3247) 1000명 이상의 암환자와 800명 이상의 정상인에 대한 39개 혈액 바이오마커 측정 데이터
3. &nbsp;&nbsp; [__TCGA-BRCA cohort:__](http://firebrowse.org/?cohort=BRCA) 1000명 이상의 유방암 환자에 대한 유전자 발현량, SNP 목록 등 조직 정보 + 임상정보 
4. &nbsp;&nbsp; [__Quantum Machine 9 (QM9):__](https://www.kaggle.com/datasets/zaharch/quantum-machine-9-aka-qm9) 13만종 이상의 저분자 화합물에 대한 SMILES code 및 분자 특성 측정 데이터 
