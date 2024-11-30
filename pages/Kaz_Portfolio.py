import streamlit as st
import Kaz_Info
import pandas as pd
import base64

def render_image(filepath: str, width: int):
   """
   filepath: path to the image. Must have a valid file extension.
   """
   mime_type = filepath.split('.')[-1:][0].lower()
   with open(filepath, "rb") as f:
    content_bytes = f.read()
    content_b64encoded = base64.b64encode(content_bytes).decode()
    image_string = f'data:image/{mime_type};base64,{content_b64encoded}'
    st.image(image_string, width=width)

#About Me
def about_me_section():
    st.header("About Me")
    render_image("/mount/src/webdeblab03-new/profile.jpg", 200)
    # st.image("../profile.jpg", width=200)
    st.write(Kaz_Info.about_me)
    st.write('---')
about_me_section()

#SideBar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link= f'<a href="{Kaz_Info.my_linkedin_url}"><img src="{Kaz_Info.linkedin_image_url}" alt="LinkedIn" width ="75" height ="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check out my work")
    github_link = f'<a href="{Kaz_Info.my_github_url}"><img src="{Kaz_Info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{Kaz_Info.my_email_address}"><img src="{Kaz_Info.email_image_url}" alt="Email" width ="75" height ="75"></a>'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework=pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("---")
    
education_section(Kaz_Info.education_data, Kaz_Info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
        st.write("---")
experience_section(Kaz_Info.experience_data)

#Projects
def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description, in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(Kaz_Info.projects_data)

#Skills

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{Kaz_Info.programming_icons.get(skill, '')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{Kaz_Info.spoken_icons.get(spoken, '')}: {proficiency}")
        
    st.write("---")
skills_section(Kaz_Info.programming_data, Kaz_Info.spoken_data)

#Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(Kaz_Info.leadership_data, Kaz_Info.activity_data)

    
