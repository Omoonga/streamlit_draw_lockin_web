import streamlit as st

left3, mid3, right3 = st.columns(3, vertical_alignment="center")
with mid3:
    st.image("streamlitweb#1\\assets\\SameMori.png")

st.title("PERCEPTION GAP 👀")
st.subheader("FLIP CANVAS: Find the errors in your art.")
st.write("""
- Outside Views
- Feedback
""")

# --- TASK LIST ---
task3 = st.text_input("Enter what needs practice: "," ")

if st.button("Add Task: "):
    if task3:
        st.session_state["task3_list"].append(task3)

if "task3_list" not in st.session_state:
    st.session_state["task3_list"] = []

for i3, t3 in enumerate(st.session_state["task3_list"]):
    st.header(f"{i3 + 1}. {t3}")

st.write("=" * 88)

for i3, t3 in enumerate(st.session_state["task3_list"]):
    st.write("_" * 20)
    if st.checkbox(f"{i3 + 1}. {t3}"):
        st.session_state["task3_list"].remove(t3)


st.image("streamlitweb#1\\assets\\Eric chud.png")