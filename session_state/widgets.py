import streamlit as st

# buff will hold the second column object. The name "buff" (short for "buffer", I imagine) suggests that this column is probably intended to create some visual space or separation between the other two columns.
col1 , buff , col2 = st.columns([1,0.5,3])

option_name = ['d' ,'e' , 'f']
option = col1.radio("Pick an option" , option_name , key="radio_option")
# next = st.button("Next Option")


# if next:
#     if st.session_state["radio_option"] == 'd':
#         st.session_state.radio_option = 'e'

#     elif st.session_state["radio_option"] == 'e':
#         st.session_state.radio_option = "f"
    
#     else:
#         st.session_state.radio_option = 'd'



st.session_state

if option == 'd':
    col2.write("You picked 'a' , smile ")
elif option == 'e':
    col2.write("you picked 'b' , heart")
else:
    col2.write("you picked 'c' , heartbreak")        



