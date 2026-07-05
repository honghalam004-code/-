# 1. 스트림릿 라이브러리 설치 (이미 설치했다면 건너뛰어도 됨)
pip install streamlit

# 2. 깃허브 배포를 위한 패키지 목록 파일 생성
echo "streamlit" > requirements.txt

# 3. 내 컴퓨터에서 다마고치 실행하기
streamlit run app.py
