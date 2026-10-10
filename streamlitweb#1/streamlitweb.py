import streamlit as st

# --- PAGE SETUP --- 
home_page = st.Page(
    page = "views/home.py",
    title = "WELCOME",
    icon = ":material/home:",
    default = True,
)

knowledge_page = st.Page(
    page = "views/knowledge.py",
    title = "Knowledge Gap",
    icon = ":material/book:",
)

execution_page = st.Page(
    page = "views/execution.py",
    title = "Execution Gap",
    icon = ":material/construction:",
)

perception_page = st.Page(
    page = "views/perception.py",
    title = "Perception Gap",
    icon = ":material/eye_tracking:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[home_page, knowledge_page, execution_page, perception_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Home": [home_page],
        "Gaps": [knowledge_page, execution_page, perception_page],
    }
)

# --- SHARED ON ALL PAGES ---
# st.logo()
st.sidebar.text("SABA")

# --- RUN NAVIGATION ---
pg.run()