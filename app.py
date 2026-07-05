import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="픽셀 도트 다마고치 프로", page_icon="🕹️", layout="centered")
st.title("🏡 마이룸 & 코스튬 다마고치 👾")

# 2. 데이터 정의 (캐릭터 10종, 상점 아이템)
CHARACTERS = {
    "알": {"name": "신비한 알", "icon": "🥚", "desc": "무엇이 태어날지 모르는 고요한 알입니다."},
    "유아기": {"name": "꼬물 도트", "icon": "👾", "desc": "갓 태어나 꼬물거리는 아기 도트입니다."},
    "성장_슬라임": {"name": "젤리 슬라임", "icon": "💧", "desc": "말랑말랑하고 호기심이 많은 슬라임입니다."},
    "성장_강아지": {"name": "코딩 댕댕이", "icon": "🐶", "desc": "에너지가 넘치고 장난치기를 좋아합니다."},
    "성숙_드래곤": {"name": "네온 드래곤", "icon": "🐲", "desc": "[전설] 푸른 불꽃을 뿜는 강력한 용입니다."},
    "성숙_유니콘": {"name": "사이버 유니콘", "icon": "🦄", "desc": "[환상] 무지개 빛을 발산하는 신비로운 동물입니다."},
    "성숙_로봇": {"name": "메카 제트", "icon": "🤖", "desc": "[기계] 완벽한 논리로 움직이는 최첨단 로봇입니다."},
    "성숙_고양이": {"name": "우주 식빵냥", "icon": "🐱", "desc": "[귀염] 우주선을 타고 온 시크한 고양이입니다."},
    "성숙_유령": {"name": "그림자 고스트", "icon": "👻", "desc": "[심야] 밤이 되면 장난을 치러 나타나는 유령입니다."},
    "성숙_외계인": {"name": "에일리언 삐뽀", "icon": "👽", "desc": "[미스터리] 먼 은하계에서 온 친절한 외계인입니다."}
}

ROOMS = {
    "기본 방": "#1E1E1E",
    "아늑한 핑크룸": "#4A2E35",
    "네온 사이버룸": "#112233",
    "황금 대저택": "#4A3B12"
}

COSTUMES = {
    "맨머리": "",
    "빨간 리본": "🎀",
    "신사 중절모": "🎩",
    "왕관": "👑",
    "헤드폰": "🎧"
}

# 3. 게임 상태 초기화
if "stage" not in st.session_state:
    st.session_state.stage = "알"
if "exp" not in st.session_state:
    st.session_state.exp = 0
if "hunger" not in st.session_state:
    st.session_state.hunger = 40
if "fun" not in st.session_state:
    st.session_state.fun = 60
if "coins" not in st.session_state:
    st.session_state.coins = 100       
if "status_msg" not in st.session_state:
    st.session_state.status_msg = "새로운 알이 배달되었습니다! 상호작용으로 돈을 벌고 진화시켜 보세요."

# 인벤토리 및 장착 상태
if "inventory" not in st.session_state:
    st.session_state.inventory = ["기본 방", "맨머리"]
if "current_room" not in st.session_state:
    st.session_state.current_room = "기본 방"
if "current_costume" not in st.session_state:
    st.session_state.current_costume = "맨머리"

# 4. 진화 체크 함수
def check_evolution():
    current = st.session_state.stage
    exp = st.session_state.exp
    if current == "알" and exp >= 20:
        st.session_state.stage = "유아기"
        st.session_state.status_msg = "🎉 알을 깨고 '꼬물 도트'가 태어났습니다! 코스튬 착용이 가능합니다!"
    elif current == "유아기" and exp >= 50:
        next_form = random.choice(["성장_슬라임", "성장_강아지"])
        st.session_state.stage = next_form
        st.session_state.status_msg = f"✨ '{CHARACTERS[next_form]['name']}'(으)로 성장했습니다!"
    elif current in ["성장_슬라임", "성장_강아지"] and exp >= 100:
        final_forms = ["성숙_드래곤", "성숙_유니콘", "성숙_로봇", "성숙_고양이", "성숙_유령", "성숙_외계인"]
        next_form = random.choice(final_forms)
        st.session_state.stage = next_form
        st.session_state.status_msg = f"👑 위대한 '{CHARACTERS[next_form]['name']}'(으)로 최종 진화했습니다!"

# 5. 행동 함수
def do_feed():
    reward = random.randint(5, 15)
    st.session_state.coins += reward
    if st.session_state.stage == "알":
        st.session_state.exp += 5
        st.session_state.status_msg = f"알을 정성껏 보살폈습니다. (+{reward}코인, EXP+5)"
    else:
        st.session_state.hunger = max(0, st.session_state.hunger - 25)
        st.session_state.exp += 10
        st.session_state.status_msg = f"맛있는 도트 사료를 주었습니다! (+{reward}코인, Hunger-25, EXP+10)"
    check_evolution()

def do_play():
    reward = random.randint(10, 25)
    st.session_state.coins += reward
    if st.session_state.stage == "알":
        st.session_state.exp += 2
        st.session_state.status_msg = f"알을 톡톡 두드렸습니다. (+{reward}코인, EXP+2)"
    else:
        st.session_state.fun = min(100, st.session_state.fun + 25)
        st.session_state.hunger = min(100, st.session_state.hunger + 10)
        st.session_state.exp += 15
        st.session_state.status_msg = f"미니게임을 플레이했습니다! (+{reward}코인, Fun+25, EXP+15)"
    check_evolution()

# 6. 사망 처리 및 메인 화면 구성
if st.session_state.hunger >= 100 or st.session_state.fun <= 0:
    st.error("💀 다마고치가 방치되어 별이 되었습니다... 💀")
    if st.button("다시 시작하기 (아이템은 유지됩니다)"):
        st.session_state.stage = "알"
        st.session_state.exp = 0
        st.session_state.hunger = 40
        st.session_state.fun = 60
        st.session_state.status_msg = "새로운 알과 함께 다시 시작합니다!"
        st.rerun()
else:
    tab1, tab2 = st.tabs(["🎮 다마고치 키우기", "🛒 마이룸 상점 & 옷장"])

    with tab1:
        st.subheader(f"💰 보유 코인: {st.session_state.coins} G")
        
        bg_color = ROOMS[st.session_state.current_room]
        costume_icon = COSTUMES[st.session_state.current_costume] if st.session_state.stage != "알" else ""
        char_icon = CHARACTERS[st.session_state.stage]["icon"]
        
        st.markdown(
            f"""
            <div style="background-color: {bg_color}; border: 5px solid #4CAF50; border-radius: 15px; padding: 40px; text-align: center; margin-bottom: 20px; min-height: 260px;">
                <div style="font-size: 45px; height: 45px; line-height: 45px; margin-bottom: -15px;">{costume_icon}</div>
                <div style="font-size: 90px; height: 100px; line-height: 100px;">{char_icon}</div>
                <h3 style="color: white; margin-top: 15px; margin-bottom: 5px;">{CHARACTERS[st.session_state.stage]['name']}</h3>
                <p style="color: #CCCCCC; font-size: 13px; margin: 0;">{CHARACTERS[st.session_state.stage]['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)
        col1.metric("📈 경험치 (EXP)", f"{st.session_state.exp} / 100")
        col2.metric("🍖 배고픔 (Hunger)", f"{st.session_state.hunger} / 100")
        col3.metric("🎯 기분 (Fun)", f"{st.session_state.fun} / 100")
        
        if st.session_state.stage != "알":
            st.progress(st.session_state.hunger / 100, text="배고픔도 (100이 되면 위험)")
            st.progress(st.session_state.fun / 100, text="기분 만족도 (0이 되면 위험)")

        st.info(st.session_state.status_msg)

        st.write("---")
        c1, c2 = st.columns(2)
        c1.button("🍖 밥 주기 (코인 벌기)", on_click=do_feed, use_container_width=True)
        c2.button("⚽ 놀아주기 (코인 많이 벌기)", on_click=do_play, use_container_width=True)

    with tab2:
        st.subheader("🛒 가구 및 코스튬 상점")
        st.write("아이템을 구매하면 자동으로 인벤토리에 추가되며, 아래 옷장에서 장착할 수 있습니다.")
        
        shop_items = {
            "아늑한 핑크룸": [50, "방"],
            "네온 사이버룸": [100, "방"],
            "황금 대저택": [300, "방"],
            "빨간 리본": [40, "코스튬"],
            "신사 중절모": [80, "코스튬"],
            "헤드폰": [120, "코스튬"],
            "왕관": [250, "코스튬"]
        }
        
        sc1, sc2 = st.columns(2)
        for idx, (item, info) in enumerate(shop_items.items()):
            target_col = sc1 if idx % 2 == 0 else sc2
            with target_col:
                if item in st.session_state.inventory:
                    st.button(f"✅ {item} (보유 중)", disabled=True, key=f"shop_{item}")
                else:
                    if st.button(f"🛒 {item} ({info[0]}G)", key=f"shop_{item}"):
                        if st.session_state.coins >= info[0]:
                            st.session_state.coins -= info[0]
                            st.session_state.inventory.append(item)
                            st.toast(f"🎉 {item} 구매 완료!")
                            st.rerun()
                        else:
                            st.error("코인이 부족합니다! 열심히 일해서 코인을 모으세요.")

        st.write("---")
        st.subheader("🎒 마이 옷장 & 인테리어")
        
        owned_rooms = [r for r in ROOMS.keys() if r in st.session_state.inventory]
        owned_costumes = [c for c in COSTUMES.keys() if c in st.session_state.inventory]
        
        selected_room = st.selectbox("집 배경 도배하기", owned_rooms, index=owned_rooms.index(st.session_state.current_room))
        if selected_room != st.session_state.current_room:
            st.session_state.current_room = selected_room
            st.rerun()
            
        selected_costume = st.selectbox("코스튬 모자 씌우기", owned_costumes, index=owned_costumes.index(st.session_state.current_costume))
        if selected_costume != st.session_state.current_costume:
            if st.session_state.stage == "알":
                st.warning("알 상태에서는 코스튬을 착용할 수 없습니다! 부화한 후에 입혀주세요.")
            else:
                st.session_state.current_costume = selected_costume
                st.rerun()
