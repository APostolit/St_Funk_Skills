import streamlit as st
import fun_g3

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

