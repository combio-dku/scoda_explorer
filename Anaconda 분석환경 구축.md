# Anaconda 분석 환경 구축
## Anaconda 설치 및 실행
1. [여기](https://www.anaconda.com/download/success)에서 Anaconda individual edition을 다운 받습니다. (OS에 맞는 적당한 것을 다운 받되 Windows나 Mac의 경우 64-Bit Graphical Installer를 추천합니다.)
3. 다운받은 설치파일을 실행시켜 Anaconda을 설치합니다. (동의를 한번하고 Next 버튼을 몇번 누르고 Install 버튼을 누르면 됩니다.)
5. 설치가 완료되면 Windows의 경우 시작 메뉴에, Mac의 경우 응용 프로그램(Applications)에 "Anaconda Navigator" 가 생깁니다.
7. "Anaconda Navigator"를 실행하면 창이 하나 뜨고 "JupyterLab"과 "Jupyter Notebook" 패널이 보입니다.
8. "JupyterLab"과 "Jupyter Notebook" 둘 중 하나를 클릭하면 터미털 창이 먼저 하나 뜨고 이 후 브라우저기 뜨면서 주피터 창이 열리는데 그러면 사용 준비가 된 것입니다.

![image](https://github.com/user-attachments/assets/0f4d9cfb-14cf-4711-84d5-f2b442ee3582)

- Anaconda Navigator 창 상단 중앙에 보면 "base (root)"라는 Drop down 메뉴가 보이는데 현재 "base" conda 환경에서 실행 중이라는 의미입니다.
- "base" conda 환경에는 기본적인 python package들이 깔려 있어 이 환경에서 python을 사용해도 무방합니다.

## Conda 환경 만들기
- "base" 환경에는 보통 최신의 python 버전이 깔려 있는데 (호환성 문제 등으로) 원하는 python 버전이 있거나 R을 사용하고자 한다면 새로 conda 환경을 만들어 사용해야 합니다.
- Conda 환경의 생성은 Anaconda Navigator에서도 좌측 메뉴에서 Environment를 선택하여 할 수 있지만 이보다는 터미널에서 conda command를 이용하는 것이 보다 편리합니다.
- [여기](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)를 참고하여 conda 환경을 생성하고 필요한 패키지를 설치하여 사용하면 되는데 터미널 열기는 Windows의 경우 시작 -> Anaconda (anaconda3) -> Anaconda Prompt 를 실행하여 터미널을 열면되고 Mac OS의 경우 응용 프로그램에서 Terminal (터미널)을 실행시키면 됩니다.

## R을 사용하기 위한 Conda 환경 만들기
Anaconda Navigator에서도 좌측 메뉴에서 Environment를 선택하여 R을 사용하기 위한 conda 환경을 생성할 수 있지만 R 버전이 맞지않을 수 있어 터미널에서 conda command를 이용하는 것이 좋습니다. 만약 원하는 R버전이 R4.4라면 다음과 같이 진행하면 됩니다.

1. 위의 설명을 참고하여 터미널을 엽니다. (Command propt 앞에 (base)라고 나와야 합니다. 그래야 conda command를 사용할 수 있습니다.)
2. 터미널에서 먼저 다음의 명령으로 환경을 새로 하나 만듧니다. `conda create -n r_env` (여기서 r_env는 새로 만들어지는 환경의 이름입니다.)
3. (선택 사항) 만약 원하는 파이썬 버전이 있을 경우 `conda create -n r_env python=3.10`의 형태로 실행 합니다.
4. 다음의 명령으로 새로만든 환경을 활성화 합니다. `conda activate r_env`
5. 그러면 Command prompt 앞에 `(base)`가 `(r_env)`로 변경 됩니다.
6. 다음의 명령으로 주피터 노트북을 설치 합니다. `conda install notebook`
7. 다음의 명령으로 R을 설치합니다. `conda install -c conda-forge r-base`. (원하는 R버전이 있다면 뒤에 '=버전번호'를 붙이면 됩니다. 예를 들어 R4.1.2를 사용하고 싶다면 `conda install -c conda-forge r-base=4.1.2`을 실행하면 됩니다.)
8. 주피터 노트북에서 R을 사용하려면 다음의 명령을 실행합니다. `conda install -c conda-forge r-essentials`
9. 이제 Command prompt에서 `jupyter notebook` 명령을 실행하면 브라우저에서 주피터가 열리고 노트북 열 때 R커널을 선택하여 노트북에서 R 명령을 사용할 수 있습니다. 
