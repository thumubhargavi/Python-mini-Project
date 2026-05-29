# University Management System (UMS) using Streamlit

# pip install steamlit
# streamlit run OOP_UMS.py
import streamlit as st

st.set_page_config(
    page_title="University System",
    layout="wide"
)

st.title("University Management System")

# creating session variable for list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

# Side bar
menu_choice = st.sidebar.radio(
    "Select Action",
    (
    "Create College",
    "Add Student",
    "Add Teacher",
    "Display Students",
    "Display Teachers",
    "List Colleges"
    )
)

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []  # list of student objects
        self.teachers = []  # list of teacher objects
    def add_student(self, s):
        self.students.append(s)
    def add_teacher(self, t):
        self.teachers.append(t)

class person:
    def __init__(self, branch, name):
        self.branch = branch
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(branch, name)
        self.rollno =rollno
    
class teacher(person):
    def __init__(self, branch, name, subject):
        super().__init__(branch, name)
        self.subject = subject
# finding college out of all available colleges
def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname == cname), None)

# Create a new college
if menu_choice == "Create College":
    cname = st.text_input("Enter New College Name")
    if st.button("Create College"):
        st.session_state.colleges.append(college(cname)) # storing the object
        st.success(f"{cname} created successfully!")

# Add student
elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Select College", [c.cname for c in st.session_state.colleges])
        roll = st.text_input("Enter Roll Number")
        sname = st.text_input("Enter Student Name")
        branch = st.text_input("Enter Branch")
        if st.button("Add Student"):
            if not(roll and sname and branch and clgname):
                st.error("Please fill all the fields")
            else:
                clg = find_college(clgname)
                clg.add_student(student(roll, sname, branch))
                st.success(f"Student {sname} added to {clgname} successfully!")
                    
elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Select College", [c.cname for c in st.session_state.colleges])
        tname = st.text_input("Enter Teacher Name")
        branch = st.text_input("Enter Branch")
        subject = st.text_input("Enter Subject")
        if st.button("Add Teacher"):
            if not(tname and branch and subject and clgname):
                st.error("Please fill all the fields")
            else:
                clg = find_college(clgname)
                clg.add_teacher(teacher(branch, tname, subject))
                st.success(f"Teacher {tname} added to {clgname} successfully!")

elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Select College", [c.cname for c in st.session_state.colleges])
        clg = find_college(clgname)
        st.subheader(f"Students in {clgname}:")
        if clg.students:
            for i, s in enumerate(clg.students, start=1):
                st.write(f"{i}. {s.name}")
        else:
            st.warning("No students found.")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Select College", [c.cname for c in st.session_state.colleges])
        clg = find_college(clgname)
        st.subheader(f"Teachers in {clgname}:")
        if clg.teachers:
            for i, t in enumerate(clg.teachers, start=1):
                st.write(f"{i}. {t.name} - {t.subject}")
        else:
            st.warning("No teachers found.")

elif menu_choice == "List Colleges":
    st.subheader("List of Colleges")
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        for i, c in enumerate(st.session_state.colleges, 1):
            st.write(f"{i} : {c.cname}")