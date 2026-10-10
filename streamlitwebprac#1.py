import streamlit as st

st.title("Learning What You Need to Learn")

uploaded_file = st.file_uploader("Choose a PNG", type="png")

if uploaded_file is not None:
    st.write("File uploaded...")
    df = st.image(uploaded_file)

    st.subheader("SABA")

task = st.text_input("Enter what you need to learn: "," ")

if st.button("Add Task: "):
    if task:
        st.session_state["task_list"].append(task)

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

for i, t in enumerate(st.session_state["task_list"]):
    st.write(f"{i + 1}. {t}")

for i, t in enumerate(st.session_state["task_list"]):
    if st.checkbox(f"{i + 1}. {t}"):
        st.session_state["task_list"].remove(t)

