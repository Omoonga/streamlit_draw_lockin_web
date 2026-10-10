import streamlit as st

left, mid, right = st.columns(3, vertical_alignment="center")
with mid:
    st.image("streamlitweb#1/assets/what.jpg", width=250)

st.title("EXECUTION GAP 🛠️")
st.subheader("If you can explain it, THEN PRACTICE IT!!!")
st.write("""
    - PRACTICE PAGES (MANY‼️)
      - 'I really want to get better at this...😭': THEN DO IT ALREADY
      - Repetitions w/ Feedback
      - ACTUALLY PRACTICE MAN 
        - 5 min, 10 min, 20, 5 hours, IT DON'T MATTER
""")

# --- TASK LIST ---
task2 = st.text_input("Enter what you need to practice: "," ")

if st.button("Add Task: "):
    if task2:
        st.session_state["task2_list"].append(task2)

if "task2_list" not in st.session_state:
    st.session_state["task2_list"] = []

for i2, t2 in enumerate(st.session_state["task2_list"]):
    st.header(f"{i2 + 1}. {t2}")

st.write("=" * 88)

for i2, t2 in enumerate(st.session_state["task2_list"]):
    st.write("_" * 20)
    if st.checkbox(f"{i2 + 1}. {t2}"):
        st.session_state["task2_list"].remove(t2)

st.image("streamlitweb#1/assets/wat.jpg")
