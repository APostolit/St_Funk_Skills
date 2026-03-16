import streamlit as st
import pandas as pd
from tornado.web import Finish


def run_1_1():
    with st.container(width=500):
        st.markdown('#### 🐍 Complete the following tasks')
        # task_1=task_2=task_3=task_4=task_5=task_6=task_7=task_8=task_9=task_10=task_11=None
        # task_12 = task_13 = task_14 = task_15 = task_16 = task_17 = task_18 = task_19 = task_20 = None
        # task_21 = None

    tab1, tab2, tab3, tab4 = st.tabs(["1️⃣ Text 1", "2️⃣ Text 2", "3️⃣ Text 3", "4️⃣ Text 4"])

    # Вкладка 1
    with tab1:
        st.markdown("**Answer ALL Questions**", text_alignment="center")
        st.markdown("**Read Text 1 then answer Questions 1 to 5**")
        st.markdown("**Text 1**")
        with st.container(height=730, width=600, border=True):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image('images/sport.png', width=150)
            with col2:
                with st.container(horizontal_alignment="center"):
                    st.markdown(body="**KIPLEY SPORTS CENTRE**", text_alignment="center")
                    st.text("Gibso Road")
                    st.text("00006 326576")
                st.divider()
            with st.container(horizontal_alignment="center"):
                st.text("Do you want to get fit and meet new people?")
                st.text("Come and join our new sports centre.")
                st.text("We have activities for all ages.")
            with st.container():
                st.text("Opening hours:")
                st.write("- Monday to Friday 8am - 10 pm")
                st.write("- Saturday and Sunday 8am - 12 noon")
                st.text("What we offer:")
                st.write("- lots of exciting classes")
                st.write("- climbing wall")
                st.write("- gym with modern machines")
                st.write("- swimming pool.")
                st.text("For more information, please call the sports centre and speak to the office manager.")

        with st.container(border=True,  width=400):
            st.markdown(body="**Put a tick ✅ in the correct box**")
            with st.container(horizontal_alignment="center", border=True, width=300):
                task_1 = st.radio(label='1. The text uses:', index=None,
                                  options=['A - bullet points',
                                           'B - paragraphs',
                                           'C - numbered points'])
            with st.container(horizontal_alignment="center", border=True, width=300):
                task_2 = st.radio(label='2. Kipley Sports Centre is closed:', index=None,
                                  options=['A - Monday evening',
                                           'B - Thursday morning',
                                           'C - Sunday afternoon'])
            with st.container(horizontal_alignment="center", border=True, width=400):
                st.write("3. 'Do you want to get fit and meet new people?'")
                task_3 = st.radio(label='The punctuation at the end of the line is:', index=None,
                                  options=['A - a question mark',
                                           'B - a full stop',
                                           'C - an exclamation mark'])
            with st.container(horizontal_alignment="center", border=True, width=400):
                task_4 = st.radio(label='4. The word that comes last in alphabetical order is:', index=None,
                                  options=['A - exciting',
                                           'B - modern',
                                           'C - climbing'])
            with st.container(horizontal_alignment="center", border=True, width=400):
                st.write("5. Who do you speak to for more information?")
                task_5 = st.text_area(label='Write your answer on the line .', value=None, height=50,
                                       key=5, placeholder='Input text')

    # Вкладка 2
    with tab2:
        st.markdown("**Read Text 2 then answer Questions 6 to 10**")
        st.markdown("**Text 2**")
        with st.container(width=580, height=330, border=True):
            st.text('Hi Roland')
            st.text('My family has moved into a new home with a large garden.')
            st.text('I would like you to see the new house. We are having a party on Saturday evening at 7 pm.'
                    ' It is not far from where you live. Are you free to join us?')
            st.text('On Saturday, I am working in the morning. In the afternoon I am going to the '
                    'hairdressers and then to the supermarket. I am home around 5 pm. Please come '
                    'early and help me cook some food for the party.')
            st.text('Message me and let me know.')
            st.text('Mel')
        with st.container(border=True, width=500):
            st.markdown(body="**Put a tick ✅ in the correct box**")
            with st.container(horizontal_alignment="center", border=True, width=300):
                task_6 = st.radio(label='6. The text tells you why Mel:', index=None,
                                  options=['A - wants her friend to visit',
                                           'B - needs a bigger garden',
                                           'C - enjoys going to parties'])
            with st.container(horizontal_alignment="center", border=True, width=300):
                task_7 = st.radio(label='7. The text uses:', index=None,
                                  options=['A - bullet points',
                                           'B - paragraphs',
                                           'C - lists'])
            with st.container(horizontal_alignment="center", border=True, width=300):
                st.write("8. 'see the new house.'")
                task_8 = st.radio(label="The word that is a verb is:", index=None,
                                  options=['A - house',
                                           'B - see',
                                           'C - new'])
            with st.container(horizontal_alignment="center", border=True, width=300):
                task_9 = st.radio(label="9. What will Mel do on Saturday morning?", index=None,
                                  options=['A - buy some food',
                                           'B - get a hair cut',
                                           'C - go to work'])
            with st.container(horizontal_alignment="center", border=True, width=400):
                st.write("10. Put the list of words in alphabetical order.")
                st.write("The first one has been done for you.")

                df = pd.DataFrame(
                    {
                        "Word": ["moved", "food", "garden", "party"],
                        "Number":[0, 0, 0, 0],
                    }
                )
                task_10 = st.data_editor(df, width="stretch", hide_index=True,
                                         column_config={
                                            "Word": st.column_config.NumberColumn(disabled=True),
                                            "Number": st.column_config.NumberColumn(min_value=0, max_value=4),
                                             },)

    # Вкладка 3
    with tab3:
        st.markdown("**Look at Text 3 then answer Questions 11 to 15**")
        st.markdown("**Text 3**")
        with st.container(height=600, border=True):
            st.image('images/image_1.png')

        st.markdown(body="**Put a tick ✅ in the correct box**")
        with st.container(horizontal_alignment="center", border=True, width=200):
            task_11 = st.radio(label='11. The images are:', index=None,
                              options=['A - signs',
                                       'B - lists',
                                       'C - maps'])
        with st.container(horizontal_alignment="center", border=True, width=350):
            task_12 = st.radio(label='12. The image that tells people to wear glasses is:', index=None,
                              options=['A - Image В',
                                       'B - Image С',
                                       'C - Image D'])
        with st.container(horizontal_alignment="center", border=True, width=200):
            task_13 = st.radio(label='13. Image С is giving:', index=None,
                              options=['A - an invitation',
                                       'B - a warning',
                                       'C - directions'])
        with st.container(horizontal_alignment="center", border=True, width=300):
            task_14 = st.radio(label='14. Which image tells you not to cycle?', index=None,
                              options=['A - Image A',
                                       'B - Image В',
                                       'C - Image C'])
        with st.container(horizontal_alignment="center", border=True, width=300):
            st.write("15. 'Staff only'")
            task_15 = st.radio(label="The word 'Staff' in Image В is:", index=None,
                               options=['A - a pronoun',
                                        'B - an adjective',
                                        'C - a noun'])
    with tab4:
        st.markdown("**Read Text 4 then answer Questions 16 to 21**")
        st.markdown("**Text 4**")
        with st.container(width=450, height=480, border=True):
            st.markdown(body="**DO YOU WANT TO IMPROVE YOUR SLEEP?**", text_alignment="center")
            st.markdown(body="**Here is som e advice to help you.**", text_alignment="center")
            st.text('Tips:')
            st.text('1. go to bed_____________the same time every day')
            st.text('2. do not look at your mobile phone before going to sleep')
            st.text('3. take some exercise during the day.')
            st.text('Your bedroom:')
            st.text('1. have curtains or blinds so the room is dark')
            st.text('2. make sure the room is not too hot or too cold')
            st.text('3. the room should be as quiet as possible.')
            st.markdown(body="Sleep well and have more energy!", text_alignment="center")

        st.markdown(body="**Put a tick ✅ in the correct box**")

        with st.container(horizontal_alignment="center", border=True, width=200):
            task_16 = st.radio(label='16. The text is a:', index=None,
                               options=['A - poster',
                                        'B - letter',
                                        'C - menu'])
        with st.container(horizontal_alignment="center", border=True, width=600):
            st.text('17. Fill in the gap with the correct word from the column on the right.')

            col3, col4 = st.columns([3, 1])
            with col3:
                st.text('1. go to bed ________ the same time every day')
            with col4:
                with st.container(horizontal_alignment="center"):
                    task_17 = st.radio(label='Words to choose:', index=None,
                                       options=['before',
                                                'after',
                                                'at'])
            if task_17=='before':
                st.text('1. go to bed _before_ the same time every day')
            elif task_17 == 'after':
                st.text('1. go to bed _after__ the same time every day')
            elif task_17 == 'at':
                st.text('1. go to bed ___at___ the same time every day')
            else:
                st.text('1. go to bed________ the same time every day')

        with st.container(horizontal_alignment="center", border=True, width=300):
            st.text('18. Sleep well and have more energy!')
            task_18 = st.radio(label='The punctuation at the end of the line is:', index=None,
                               options=['A - a',
                                        'B - an exclamation mark',
                                        'C - a full stop'])
        with st.container(horizontal_alignment="center", border=True, width=300):
            task_19 = st.radio(label='19. The numbered points in the text:', index=None,
                               options=['A - tell you how to sleep better',
                                        'B - describe curtains and blinds',
                                        'C - give advice on buying phones'])
        with st.container(horizontal_alignment="center", border=True, width=400):
            task_20 = st.radio(label='20. The word that comes last in alphabetical order is:', index=None,
                               options=['A - exercise',
                                        'B - quiet',
                                        'C - possible'])
        with st.container(horizontal_alignment="center", border=True, width=400):
            st.write("21. What do you have after a good sleep?")
            task_21 = None
            task_21 = st.text_area(label='Write your answer on the line .', value=None, height=50,
                                    key=21, placeholder='Input text')

        bt_finish = st.button(label='🏁 Complete the test', type='primary')
        ans_true=0
        ans_false = 0
        list_wrong = []

        if bt_finish:
            if task_1=='A - bullet points':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 1')

            if task_2=='C - Sunday afternoon':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 2')

            if task_3 == 'A - a question mark':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 3')

            if task_4 == 'B - modern':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 4')

            if task_5 == 'office manager' or task_5 == 'office manager.' \
                    or task_5 == 'the office manager' or task_5 == 'the office manager.':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 5')

            if task_6 == 'A - wants her friend to visit':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 6')

            if task_7 == 'B - paragraphs':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 7')

            if task_8 == 'B - see':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 8')

            if task_9 == 'C - go to work':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 9')

            my_list = task_10['Number'].tolist()
            if my_list == [3, 1, 2, 4]:
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 10')

            if task_11 == 'A - signs':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 11')

            if task_12 == 'C - Image D':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 12')

            if task_13 == 'B - a warning':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 13')

            if task_14 == 'A - Image A':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 14')

            if task_15 == 'C - a noun':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 15')

            if task_16 == 'A - poster':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 16')

            if task_17 == 'at':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 17')

            if task_18 == 'B - an exclamation mark':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 18')

            if task_19 == 'A - tell you how to sleep better':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 19')

            if task_20 == 'B - quiet':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 20')

            if task_21 == 'more energy' or task_21 == 'more energy!' \
                    or task_21 == ' more energy' or task_21 == ' more energy!':
                ans_true += 1
            else:
                ans_false += 1
                list_wrong.append('Question 21')

            st.write('Correctly - ', ans_true)
            st.write('Wrongly - ', ans_false)

            if ans_true >= 16:
                st.markdown("**✅️ The test was passed! 👍**")
            else:
                st.markdown("**❌ The test failed 😭**")

            if list_wrong != []:
                st.markdown("**⚠️ Errors** ⚠️")
                st.text(list_wrong)

            # st.session_state['21'] = 'Input text'

if __name__ == '__main__':
    run_1_1()