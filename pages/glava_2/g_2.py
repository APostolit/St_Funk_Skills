# https://python-code-online.pages.dev/ru/
import streamlit as st
import fun_g2

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Set 36", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
# st.header("👩🏻‍💻Next")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

