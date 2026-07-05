import streamlit as st
import time

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="나의 귀여운 다마고치", page_icon="👾")
st.title("👾 나만의 랜선 다마고치")

# 2. 다마고치 초기 상태 설정 (session_state 사용)
if "hp" not in st.session_state:
    st.session_state.hp = 50       # 체력
if "hunger" not in st.session_state:
    st.session_state.hunger = 50   # 배고픔 (0이 되면 배부름, 100이면 굶어 죽음)
if "status" not in st.session_state:
    st.session_state.status = "평온함 😐"

# 3. 상태 업데이트 함수들
def feed():
    if st.session_state.hunger > 0:
        st.session_state.hunger = max(0, st.session_state.hunger - 20)
        st.session_state.hp = min(100, st.session_state.hp + 5)
        st.session_state.status = "냠냠 맛있다! 😋"
    else:
        st.session_state.status = "배가 너무 불러요! 🤮"

def play():
    if st.session_state.hunger < 90:
        st.session_state.hunger = min(100, st.session_state.hunger + 15)
        st.session_state.hp = min(100, st.session_state.hp + 10)
        st.session_state.status = "신나게 놀았어요! 텐션 업! 🤩"
    else:
        st.session_state.status = "배고파서 놀 힘이 없어요... 😢"

def sleep():
    st.session_state.hp = min(100, st.session_state.hp + 30)
    st.session_state.hunger = min(100, st.session_state.hunger + 10)
    st.session_state.status = "쿨쿨 잠을 잤습니다 😴"

# 4. 생사 확인 로직
if st.session_state.hunger >= 100 or st.session_state.hp <= 0:
    st.error("💀 다마고치가 무지개 다리를 건넜습니다... 💀")
    if st.button("다시 키우기"):
        st.session_state.hp = 50
        st.session_state.hunger = 50
        st.session_state.status = "부활했습니다! 🥚"
        st.rerun()
else:
    # 5. 화면 레이아웃 구상
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="❤️ 체력 (HP)", value=f"{st.session_state.hp} / 100")
    with col2:
        st.metric(label="🍖 배고픔 (Hunger)", value=f"{st.session_state.hunger} / 100")
    
    # 진행 바(Progress Bar)로 시각화
    st.progress(st.session_state.hp / 100)
    
    st.subheader(f"현재 다마고치 상태: {st.session_state.status}")
    
    # 6. 상호작용 버튼
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🍖 밥 주기", on_click=feed)
    with c2:
        st.button("⚽ 놀아주기", on_click=play)
    with c3:
        st.button("💤 재우기", on_click=sleep)
