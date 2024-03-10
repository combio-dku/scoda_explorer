# SCODA Workshop
- __일시:__ 3월 22일 (금) 13:00~16:00
- __장소:__ 온라인 (zoom 링크는 추후 이메일 공지 드립니다)
- __주최:__ (주) 엠엘비아이랩
- __연사:__ 윤석현 대표
- __사용언어:__ python3
- __개별 준비물:__ 웹브라우저가 설치된 PC or Laptop or Tablet
- __목적:__ SCODA 의 활용법 실습을 통해 단일세포 RNA-seq 데이터 분석 능력을 갖춘다.
- __참가자 사전 지식:__
  - 생명과학/의학분야에 종사하시면서 단일세포 RNA-seq 기술이 어디에 어떻게 쓰이는지 대략적으로는 아시는 분.
  - Python이나 R 사용 경험이 있으면 더 좋습니다.
- [BRIC 웨비나 발표자료](https://github.com/combio-dku/scoda_explorer/blob/main/BRIC_%EA%B8%B0%EC%97%85%EA%B8%B0%EC%88%A0%EC%9B%A8%EB%B9%84%EB%82%98_%EC%97%A0%EC%97%98%EB%B9%84%EC%95%84%EC%9D%B4%EB%9E%A9_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_v02e.pdf)


## 진행 순서
1. SCODA 간략 소개 (10분)
2. 데이터 준비 및 SCODA 실행, 주피터노트북/파이썬 간략 소개 및 실습 (1시간 10분)
3. SCODA 결과의 데이터 마이닝 (1시간 45분)
- 필요시 중간에 10분 정도 break time을 갖겠습니다.


## 1. SCODA 간략 소개
- 워크샵 당일날 10분 정도 간략하게 SCODA에 대한 소개를 드리겠지만 사전에 시간이 되신 다면 [BRIC 기업기술 웨비나: SCODA 소개](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz)를 미리 보시고 오시면 더 좋습니다.


## 2. 데이터 준비, SCODA 실행, 주피터 사용하기 (파이썬 간략 소개) (1시간 10분)
1. 사용할 데이터 다운로드: [여기 클릭](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing) (5분)
2. 입력 데이터 포맷팅 소개 (5분)
3. 데이터 업로드 및 SCODA 실행 [SCODA pipeline homepage](https://mlbi-lab.net) (10분)
4. 구글 Colab에서 주피터 노트북 열기: [여기클릭](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/scoda_viz_practice_workshop.ipynb) (5분)
5. 구글 Colab에 연결 하기 (5분)
6. 파이썬 데이터 구조 간략 소개 및 실습 (30분)
7. SCODA 결과 다운로드 (저장 경로 확인) (5분)
8. Colab서버에 결과 데이터 업로드 (5분)


## 3. SCODA 결과 들춰보기 (1시간 45분)
1. 주피터 노트북에서 SCODA 결과 파일 불러오기 (10분)
2. anndata format 간략 소개 (5분)
3. SCODA 결과 항목들 확인 (15분)
4. Celltype annotation 결과 확인 (15분)
5. CNV 추정 결과 및 암세포 식별 결과 확인 (15분)
6. Cell-cell interaction 추정 결과 확인 (15분)
7. DEG 결과 확인 및 마커 탐색 하기 (15분)
8. GSA/GSEA 결과 확인  (15분)


## 미리 준비해두면 좋습니다. 🙏
워크샵 당일날 30명의 인원이 동시에 SCODA 서버에 접속하여 SCODA를 실행하면 서버에 무리가 갈 수 있어서 만약 시간이 되신 다면 아래 절차에 따라 미리 SCODA 결과 파일을 얻어서 워크샵에서 사용하시면 좀 더 시간 save가 될듯 합니다. (SCODA 서버는 24시간 켜져 있습니다.)

1. 사용할 데이터를 다운 받는다. [여기 클릭](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing)
2. SCODA 서버에 접속한다. [SCODA 서버 homepage](https://mlbi-lab.net)
3. Mandatory Input 부분에서 ....
   1. 라디오버튼 중 `Compressed 10x_mtx file sets + (optional) meta_data.csv`를 선택한다.
   2. `파일선택` 버튼을 누르고 다운 받은 파일을 선택한다.
   3. `Species`는 Human으로 `Tumor cell Identification` 은 그대로 놔둔다.
   4. `Submit` 버튼을 눌러 SCODA가 업로드한 데이터를 처리하도록 한다.
   5. 그러면 Progress 창이 뜨고 SCODA 실행 내역이 나타난다. (처리 완료까지 5~10분 소요)
   6. SCODA의 처리가 완료되면 아래 쪽에 `Download Result` 버튼이 나오면 이를 클릭하여 SCODA 결과 파일을 다운 받는다. 
   7. 다운 받은 SCODA 결과 파일을 저장해 두었다가 워크샵날 데이터 마이닝 때 사용한다. 👍


## 참고 사항
Cell-cell interaction, DEG 및 GSA/GSEA 결과 데이터의 구성
- cell-cell interaction 결과 (`uns['CCI_sample']`)
<img width="320" alt="CCI_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/65982226-cb15-434e-8116-00692e65ab74">

- DEG 결과 (`uns['DEG']`)
<img width="555" alt="DEG_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/8d092dcb-e127-4d13-9f27-4edceeae94a7">

- GSA/GSEA 결과 (`uns['GSA_up']`, `uns['GSA_down']`, `uns['GSEA']`)
<img width="555" alt="GSA_result_structure" src="https://github.com/combio-dku/scoda_explorer/assets/82195405/1d111fc8-ecaf-4f57-b0b9-94102b891498">

