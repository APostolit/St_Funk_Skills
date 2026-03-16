col3, col4 = st.columns([3, 1])
            with col3:
                st.text('go to bed________ the same time every day')
            with col4:
                with st.container(horizontal_alignment="center"):
                    st.markdown(body="**Words to choose**", text_alignment="center")
                    st.markdown(body="before", text_alignment="center")
                    st.markdown(body="after", text_alignment="center")
                    st.markdown(body="at", text_alignment="center")