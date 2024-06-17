import streamlit as st

st.title('MOQUITTO DALLA PARTITA')
st.subheader('Raw data')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.markdown("Una bella prova di **Markdown**")
st.sidebar.markdown("# Main page 🎈")