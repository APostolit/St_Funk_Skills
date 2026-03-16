import streamlit as st
import fun_g1

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Set 35", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "Select",
        ("Set 35", ),
        index=None,
        placeholder="Select a task..."
    )

# Контейнер
cont = st.container(width=800)

with cont:
    # st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор код ✍🏻')
    if options is None:
        st.write('The test is not selected')
        st.image("Skills.png", width=350)
    elif options == "Set 35":
        st.subheader("👩🏻‍💻Reading - Entry 2. Set 35")
        st.divider()  # Разделитель
        fun_g1.run_1_1()
