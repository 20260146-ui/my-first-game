##Week 11 실습

#오늘 한 것
PyInstaller 설치 및 빌드: 파이썬 파일을 실행 파일(.exe)로 만드는 과정을 진행함.
resource_path() 함수 추가: 빌드 후 이미지와 사운드 경로가 깨지는 문제를 해결하기 위해 함수를 도입함.
--add-data 옵션으로 에셋 포함: assets 폴더를 실행 파일 안에 강제로 포함시키는 빌드 옵션을 적용함.
.exe 실행 확인: 빌드된 파일에서 이미지가 나오지 않는 문제를 디버깅하고 최종적으로 정상 작동 확인.

#resource_path() 를 써야 하는 이유
PyInstaller로 빌드한 실행 파일은 실행 시 내부 파일들을 임시 폴더(_MEIPASS)에 풀어서 사용함.
일반적인 상대 경로(assets/images/...)를 쓰면 프로그램이 실제 파일이 위치한 이 임시 경로를 찾지 못해 에셋을 불러올 수 없음. 따라서 실행 시점의 환경에 맞춰 정확한 절대 경로를 반환해 주는 resource_path() 처리가 필수적임.

#빌드 명령어
pyinstaller --version
pyinstaller --onefile --windowed --add-data "assets;assets" --name=MyGame "FEVER BREAK.py"

#AI 활용 내역
-실행 파일 빌드 에러 해결: Script file 'FEVER BREAK' does not exist 에러 발생 시 확장자(.py) -누락과 경로 설정(cd ..) 문제를 AI와 대화하며 해결함.
-리소스 경로 최적화: 빌드 후 이미지가 단색 사각형으로만 나오는 문제를 해결하기 위해 resource_path 함수를 코드 내 load_block_images 등에 적용하는 방법을 가이드받음.
-빌드 옵션 상담: --windowed 옵션 사용 시 에러 확인이 어려운 점을 파악하고, 디버깅을 위해 콘솔을 띄우는 법과 --add-data 사용법을 교육받음. 이후 제대로 된 파일을 실행하는 법을 깨달음.
