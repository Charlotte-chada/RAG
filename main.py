import streamlit as st

# Function to show the main content
# from dotenv import load_dotenv
# load_dotenv()  # This loads the environment variables from .env file if present

def load_css():
    st.markdown("""
        <style>
            .css-1d391kg { padding: 0; margin: 0; } /* Adjust class name based on inspection */
        </style>
        """, unsafe_allow_html=True)
    
def main_content():
    st.image("banner.png", use_column_width=True)
    st.title("🔧Machine Failure Prediction App")
    st.markdown('**What Can This App Do?**')
    st.info('This app provides prediction of machine failure')
    st.markdown('**How to Use the App?**')
    st.warning('To use this app, follow these steps: 1. Navigate to the "Machine Failure Prediction" 2. Put the information about machine condition. 3. Proceed to predict the machine failure by clicking the button. 4. Try to talk with RAG model in "RAG Chat" ')

st.set_page_config(
    page_title="Welcome",
    page_icon="🏡",
    layout="wide",  # Change layout to wide
    initial_sidebar_state="collapsed"
)

if __name__ == "__main__":
    load_css()
    main_content()