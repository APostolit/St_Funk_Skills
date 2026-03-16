# Создать
# pip freeze > requirements.txt
# Установить библиотеки
# pip install -r requirements.txt

import streamlit as st

# Сделать доступной всю ширину страницы
st.set_page_config(layout="wide")
st.set_page_config(initial_sidebar_state="collapsed")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")

# Глава 1
g_1 = st.Page(page="pages/glava_1/g_1.py", title="📕Start")
# Глава 2
g_2 = st.Page(page="pages/glava_2/g_2.py", title="📕Start")
# Глава 3
# g_3 = st.Page(page="pages/glava_3/g_3.py", title="📕Листинги Главы 3")
# Глава 4
# g_4 = st.Page(page="pages/glava_4/g_4.py", title="📕Листинги Главы 4")

# Глава 5
# g_5 = st.Page(page="pages/glava_5/g_5.py", title="📕Листинги главы 5")

# Глава 6
# g_6 = st.Page(page="pages/glava_6/g_6.py", title="📕Листинги главы 6")

# Создание навигатора страниц (главное меню)
pages = {
    "Reading - Entry 2": [g_1],
    "Reading - Entry 3": [g_2],
    # "Глава 3": [g_3],
    # "Глава 4": [g_4],
    # "Глава 5": [g_5],
    # "Глава 6": [g_6],
    }
pg = st.navigation(pages=pages, position="top", expanded=False)
st.header("👩🏻‍💻Personal Edexcel Awards and Certificates")
# Запуск навигатора страниц
pg.run()

# streamlit run app_start.py
