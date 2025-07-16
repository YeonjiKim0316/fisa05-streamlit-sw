import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


# 텍스트를 입력받아서 해당 텍스트와 일치하는 이미즐 화면에 출력 

# 1. 입력을 받는 방법 (입력이 맞을 때만 정상 출략, 입력이 맞지 않을 때는 에러가 발생)
# ani_name = st.text_input('애니메이션 이름을 입력하세요')
# st.write(ani_name)
# st.image(img_list[ani_list.index(ani_name)])


# 2. 입력을 받는 방법 (key parameter를 사용해서 입력을 받는 방법)
st.text_input('애니메이션 이름을 입력하세요', key='ani_name')
st.write('입력한 애니메이션 이름:', st.session_state.ani_name)
if st.session_state.ani_name in ani_list:
    st.image(img_list[ani_list.index(st.session_state.ani_name)])