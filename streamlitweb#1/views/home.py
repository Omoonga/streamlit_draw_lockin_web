import streamlit as st

# st.title("HOME")

@st.dialog("Say what's up")
def show_contact_form():
    st.text_input("Type Something 😊")
    submit_button = st.button("Submit")
    if submit_button:
        st.success("Literally nothing happened")

# --- HERO SECTION ---
col1, col2, = st.columns(2, gap="large", vertical_alignment = "center")
with col1:
    st.image("streamlitweb#1/assets/thumbsup.png")
with col2:
    st.subheader("Know Exactly What To Practice", anchor = False)
    st.write("Always make sure you list out the errors you see.")
    if st.button("🤔 Curious?"):
        show_contact_form()
        

# --- SECTIONS --- 
st.write("\n")
st.subheader("SABA", anchor=False)
st.write(
    """
    - Find what looks off
      - Write it down
        - Go through the list and explain each problem outloud
    """
)

st.title("List of Errors ❌")
st.subheader("We know you have a lot.")
st.write("""
- All the errors that you: 
  - Can explain
  - Can't explain 
""")

# --- TASK LIST ---
task = st.text_input("List them all out: "," ")

if st.button("Add Task: "):
    if task:
        st.session_state["task_list"].append(task)

if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

for i, t in enumerate(st.session_state["task_list"]):
    st.header(f"{i + 1}. {t}")

for i, t in enumerate(st.session_state["task_list"]):
    st.write("_" * 20)
    if st.checkbox(f"{i + 1}. {t}"):
        st.session_state["task_list"].remove(t)

st.image("streamlitweb#1/assets/The_Swamp.png")
