# Only the st.form_submit_button has a callback in forms. Other widgets inside a form are not allowed to have callbacks. submit button he callbacks lay sakte h uske ilawa koi form nhi lay sakti 

# on_change and on_click events are only supported on input type widgets.

# ek dafa widget ki value define karne k baad dobara use modify karna allowed nhi h 
# e.g slider = st.slider(
#     label='My Slider', min_value=1,
#     max_value=10, value=5, key='my_slider')

# st.session_state.my_slider = 7




# Setting the widget state via the Session State API and using the value parameter in the widget declaration is not recommended, and will throw a warning on the first run. For example:
# pehle value ko set karna then again use value pass karna means value parameter dobara use nhi kar sakte ek bar jub apne value startong m define kardi h 
# st.session_state.my_slider = 7

# slider = st.slider(
#     label='Choose a Value', min_value=1,
#     max_value=10, value=5, key='my_slider')



# Setting the state of button-like widgets: st.button, st.download_button, and st.file_uploader via the Session State API is not allowed. Such type of widgets are by default False and have ephemeral True states which are only valid for a single run. For example:

# if 'my_button' not in st.session_state:
#     st.session_state.my_button = True

# st.button('My button', key='my_button')

# In simple words, when using button-like widgets in Streamlit (like the `st.button`, `st.download_button`, and `st.file_uploader`), you can't save their states (like whether they are clicked or not) using the Session State API. Instead, these widgets automatically start as "not pressed" (or `False`) and their status only lasts for that single run of the app. Once the app reloads, their state resets, and they don't remember what happened before. 

# If you have further questions or need more details, feel free to ask!

# button ki default value not pressed hoti u can not change it in to pressed(true) agar set hogi bhi to sirf ek run k lia other wise wo wapas state pay ajaegi . so better not to change 


# Throws an exception!