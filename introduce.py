import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('취업하고 싶은 기업 소개 👋')
st.write('C421062 주승민')

# 텍스트 출력
st.write('# 패러블 엔터테인먼트')
st.write('# PARABLE ENTERTAINMENT Inc.')

img1 = Image.open('C:/Users/admin/Pictures/parable.png')

col1,col2 = st.columns([2,3])
col1.image(img1)


tab1, tab2= st.tabs(['기업정보' , '소재지'])

with tab1:
    st.write('설립일 : 2017년 9월 4일')
    st.write('업종 : 데이터베이스 및 온라인정보 제공업')
    st.write('대표자 : 김영비')
    st.write('기업규모 : 중소기업')
    st.write('상장여부 : 비상장기업')
    st.write('직원 수 : 55명')
    st.write('자본금 : 1억 812만원')
    st.write('매출액 : 130억 3108만원')
    st.write('영업이익 : -5억 3035만원')
    st.write('당기순이익 : -6억 3244만원')
    st.write('자산총액 : 59억 9852만원')

    
with tab2:
    base_position =  [37.654166, 126.896906]

    map_data = pd.DataFrame(
        np.random.randn(5, 1) / [20, 20] + base_position , 
        columns=['lat', 'lon'])

    print(map_data)

    st.subheader('경기도 고양시 덕양구 삼송로 8, 6층 605호')
    st.map(map_data)

