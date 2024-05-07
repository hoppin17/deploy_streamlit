import streamlit as st
import pandas as pd
import numpy as np

st.title('누가누가 잘 어울릴까? 👀')
st.markdown("""---""")


df = pd.read_csv('5.5_viz_dataset.csv')
df_main_main = pd.read_csv('main_actor_cross.csv', index_col='Unnamed: 0')
df_main_sub = pd.read_csv('main_sub.csv', index_col='Unnamed: 0')

df_main_main_see = pd.read_csv('main_actor_cross_see.csv', index_col='Unnamed: 0')
df_main_sub_see = pd.read_csv('main_sub_see.csv', index_col='Unnamed: 0')


st.dataframe(df)

tab1, tab2 = st.tabs(["주연-주연", "주연-조연"])



with tab1:
    st.markdown(f'# 주연간의 관계를 알려드릴게요!')
    st.markdown('')
    actor_1 = st.selectbox(
        '첫 번째 배우를 선택하세요.',
        df_main_main.columns.tolist(),
        key='select__mainactor_1'  # 고유한 키(key) 할당
    )

    valid_options = df_main_main.loc[actor_1][df_main_main.loc[actor_1] != 0].index.tolist()
    # A = list(df[df['actor_main_name'].str.contains('actor_1')]['영화명'])
    # st.markdown(f'#### {actor_1}의 대표작은 {A} 입니다!')



    actor_2 = st.selectbox(
        '두 번째 배우를 선택하세요.',
        valid_options,
        #df_main_main.columns.tolist(),
        key='select_mainactor_2'  # 고유한 키(key) 할당
    )
    # B = 
    # st.markdown(f'#### {actor_2}의 대표작은 {A} 입니다!')

    st.write("  ")
    st.markdown(f'### 몇번이나 같이 출연했을까요? {df_main_main.loc[actor_1, actor_2]}번 같이 나왔습니다.')

    st.markdown(f'### 둘의 성적은? {df_main_main_see.loc[actor_1, actor_2]}명 입니다!')


with tab2:
    st.markdown(f'# 주연-조연간의 관계를 알려드릴게요!')
    #st.dataframe(df_main_main)
    st.markdown('')

    actor_1 = st.selectbox(
        '주연 배우를 선택하세요.',
        df_main_sub.index.tolist(),
        key='select_subactor_1'  # 고유한 키(key) 할당
    )
    
    valid_options = df_main_sub.loc[actor_1][df_main_sub.loc[actor_1] != 0].index.tolist()

    actor_2 = st.selectbox(
        '조연 배우를 선택하세요.',
        valid_options,
        #df_main_sub.columns.tolist(),
        key='select_subactor_2'  # 고유한 키(key) 할당
    )
    
    st.write("  ")
    st.markdown(f'### 몇번이나 같이 나왔을까요? {df_main_sub.loc[actor_1, actor_2]}번 같이 나왔습니다.')

    st.markdown(f'### 둘의 성적은? {df_main_sub_see.loc[actor_1, actor_2]}명 입니다!')
