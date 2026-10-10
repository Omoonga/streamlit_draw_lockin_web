import streamlit as st

st.image("streamlitweb#1/assets/Drip_Goku.png")
st.title("KNOWLEDGE GAP 📖")
st.subheader("This is for the errors that you can not explain.")
st.write("""
    - Spend time learning them:
      - YouTube
      - Books
      - Mentors
""")

# --- TASK LIST ---
task1 = st.text_input("Enter what you can't explain: "," ")

if st.button("Add Task: "):
    if task1:
        st.session_state["task1_list"].append(task1)

if "task1_list" not in st.session_state:
    st.session_state["task1_list"] = []

for i1, t1 in enumerate(st.session_state["task1_list"]):
    st.header(f"{i1 + 1}. {t1}")

st.write("=" * 88)

for i1, t1 in enumerate(st.session_state["task1_list"]):
    st.write("_" * 20)
    if st.checkbox(f"{i1 + 1}. {t1}"):
        st.session_state["task1_list"].remove(t1)

st.image("streamlitweb#1/assets/yep.jpg")
