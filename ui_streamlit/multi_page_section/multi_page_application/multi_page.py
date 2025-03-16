import streamlit as st

#   MUST VISIT THIS LINK IT HAS MANY MORE FEATURE  https://github.com/SJcodeML/Multipage_application_using_streamlit_/tree/main/Streamlit_multipage_app


# you have to make main homepage in that u need to write config code 
# st.set_page_config(
#     page_title="multipgae application",
#     page_icon ="🎨"
# )

# st.title ("Main page")
# st.sidebar.success("select a page above ")

# now this will be the main page . for making more pages u need to make a folder pages/then make diferent files these will be your pages . 
# python will arrange pages alphabatically except home page . to reduce this effect u need to set 2_pagename _page_name . then it will accordingly set pages 
# for setting emoji for your page do it in the file window icon and colon as we have done in 2_🎇_project page on the ledt.
# using session state example in both pages 

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""


# my_input = st.text_input("Input a text here ", st.session_state["my_input"])

# submit =  st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("you have entered" , my_input)


#  This code is from docs https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()



# ------ these are pages -------------------
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

# ------this is default page after login user will come here 
dashboard = st.Page("reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page("reports/alerts.py", title="System alerts", icon=":material/notification_important:")
search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")
# --------------------------------------

# this is setting navigation with heading and the only user who logged in only can access the pages
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()


