# Go for the documentation and anpther video , link :https://www.youtube.com/watch?v=LLdB0kTs0gI&t=5s

# HOW CALLBACKS WORKS?

# callback is what u can change the session_state(stored value) on some change or click  
# WE can use callbacks via on_change and on_click parameters
# args (tuple) - List of arguments to be passed to the callback function
# kwargs (dict) - Named arguments to be passed to the callback function
# on-chane and on_click accepts a function name as an input argument 
#  this function is an example of call backs 

# on_change :on every button python rerun the code from top to bottom but we say to python that before runnong the code run this what i have written (extra code)

                              
# Widgets which support the on_change event:                             Widgets which support the on_click event:

                                                                                #     st.button
                                                                                #     st.download_button
                                                                                #    st.form_submit_button
# st.checkbox
# st.color_picker
# st.date_input
# st.data_editor
# st.file_uploader
# st.multiselect
# st.number_input
# st.radio
# st.select_slider
# st.selectbox
# st.slider
# st.text_area
# st.text_input
# st.time_input
# st.toggle


# Onchange function take s a fucntion name tha tells what to do after the change .
import streamlit as st
st.title("Session State Basics")

# 'st.session_state object :' ,st.session_state

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

col1 , buff , col2 = st.columns([2,1,2])

with col1 :
    pounds = st.number_input("Pounds" , key="lbs",
    on_change = lbs_to_kg )

with col2 :
    kilogram = st.number_input(
       " Kiolgrams" ,key="kg", 
       on_change = kg_to_lbs
    )    





# import streamlit as st  

# st.title("Session State Basics")  

# # Initialize session state keys if they don't exist  
# if 'lbs' not in st.session_state:  
#     st.session_state.lbs = 0.0  # Default value for pounds  

# if 'kg' not in st.session_state:  
#     st.session_state.kg = 0.0  # Default value for kilograms  

# def lbs_to_kg():  
#     if "lbs" in st.session_state and st.session_state.lbs is not None:  
#         st.session_state.kg = st.session_state.lbs / 2.2046  

# def kg_to_lbs():  
#     if "kg" in st.session_state and st.session_state.kg is not None:  
#         st.session_state.lbs = st.session_state.kg * 2.2046  

# # Create columns for input  
# col1, buff, col2 = st.columns([2, 1, 2])  

# with col1:  
#     pounds = st.number_input("Pounds", key="lbs", on_change=lbs_to_kg)  

# with col2:  
#     kilogram = st.number_input("Kilograms", key="kg", on_change=kg_to_lbs)  

# # Display the session state for reference  
# st.write('Session State:', st.session_state)  












