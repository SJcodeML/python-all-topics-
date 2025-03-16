# import streamlit as st  

# # Define the pages for your app  
# def home_page():  
#     st.title("Home Page")  
#     st.write("Welcome to the home page!")  

# def about_page():  
#     st.title("About Page")  
#     st.write("This page provides information about the app.")  

# def contact_page():  
#     st.title("Contact Page")  
#     st.write("Here you can find contact details.")  

# def hidden_page():  
#     st.title("Hidden Page")  
#     st.write("This is a page not shown in the navigation menu.")  

# # Create a dictionary of page functions  
# pages = {  
#     "Home": home_page,  
#     "About": about_page,  
#     "Contact": contact_page,  
# }  

# # Hide the default navigation  
# st.navigation(position="hidden")  

# # Create a custom navigation menu  
# st.sidebar.header("Custom Navigation")  
# selected_page = st.sidebar.selectbox("Select a page", options=pages.keys())  

# # Add an option to navigate to the hidden page  
# if st.sidebar.button("Go to Hidden Page"):  
#     hidden_page()  

# # Call the selected page function  
# page_function = pages[selected_page]  
# page_function()  

















import streamlit as st  

# Define the pages for your app  
def home_page():  
    st.title("Home Page")  
    st.write("Welcome to the home page!")  

def about_page():  
    st.title("About Page")  
    st.write("This page provides information about the app.")  

def contact_page():  
    st.title("Contact Page")  
    st.write("Here you can find contact details.")  

def hidden_page():  
    st.title("Hidden Page")  
    st.write("This page is not shown in the navigation menu.")  

# Create a dictionary that maps page titles to functions  
pages = {  
    "Home": home_page,  
    "About": about_page,  
    "Contact": contact_page,  
    # The hidden page is not included  
}  

# Create sections for navigation  
sections = {  
    "Main": list(pages.keys()),  # Include only the visible pages  
}  

# Hide default navigation by passing sections to st.navigation  
st.navigation(pages=sections, position="hidden")  

# Create custom navigation in the sidebar  
st.sidebar.header("Custom Navigation")  
selected_page = st.sidebar.selectbox("Select a page", options=list(pages.keys()))  

# Add an option to navigate to the hidden page  
if st.sidebar.button("Go to Hidden Page"):  
    hidden_page()  

# Call the selected page function based on user selection  
pages[selected_page]()  