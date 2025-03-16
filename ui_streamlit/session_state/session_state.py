import streamlit as st

#         SESSION STATE EAMPLE ALSO IN MULTIPAGE.PY FILE .WHERE DATA IS PASSING THROUGH DIFFERETN PAGES 

# "session" means whatever is going on in ur browser and "state" means whatever u have stored in ur variables to do work for later. you can say so that session_state use for "storing information" . 
# you can keep track of variables and objects during a user's session through something called Session State. 
# session_state is like an object shows in {} curly bracket 
st.session_state
# answer will be this 
{}
# --------------------------------------------------

# st.write(st.session_state)

# # With magic:
# st.session_state
# --------------------------------------------------

# Session State can also be cleared by going to Settings → Clear Cache, followed by Rerunning the app.
# --------------------------------------------------

# we are checking if session state has a_counter variable if not then assign the value 
# same for boolean value then we will print session_state it will integrate both valuues in session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0 

if 'boolean' not in st.session_state:
    st.session_state.boolean = False

st.write(st.session_state)       

# answer wil be this 
# {
# "a_counter":0,
# "boolean":false
# }


# ---------------------------
# now both the values has stored in session_state so u can access them 

st.write("bollean is: ", st.session_state.boolean)
st.write("a_counter is: " , st.session_state["a_counter"])

# answer will be this 
# bollean is: False

# a_counter is: 0

# ---------------------
# to access all the keys in session_state
for the_key in st.session_state.keys():
    st.write(the_key)
# answer will be     
# a_counter

# boolean

# to acess all the values in session_state:
for the_value in st.session_state.values():
    st.write(the_value)
# /answer will be     
# 0
# False    

# -------------------
# get the session_state as pair 
for item in st.session_state.items():
    item
# ans will be like this 
# ('a_counter', 0)

# ('boolean', False)

# -----------------
# before and after pressing buttons 
button = st.button ("Update State")
st.write ("Before pressing button ")
st.write(st.session_state)

# after pressing button 

if button :
    st.session_state["a_counter"] += 1 
    st.session_state.boolean = not st.session_state.boolean
    "after pressing buton" , st.session_state

# --------------------    

# Deleting all data from session state by accessing all keys from it 

for key in list(st.session_state.keys()):  
    del st.session_state[key]  


# -------------------------------
# WIDGET: A widget is a small application or component of an interface that enables a user to perform a function or access a service. Think of it as a building block that you can add to a larger system!

# how to conect my widget to my session state object
number = st.slider("A number" , 1 , 10 , key="slider")

# --------------------
# buff will hold the second column object. The name "buff" (short for "buffer", I imagine) suggests that this column is probably intended to create some visual space or separation between the other two columns.
# col1 , buff , col2 = st.columns([1,0.5,3])

# option_names = ['a' ,'b' , 'c']
# option = col1.radio("Pick an option" , option_names , key="radio_option")
# next = st.button("Next Option")


# if next:
#     if st.session_state["radio_option"] == 'a':
#         st.session_state.radio_option = 'b'

#     elif st.session_state["radio_option"] == 'b':
#         st.session_state.radio_option = "c"
    
#     else:
#         st.session_state[radio_option] = 'a'







