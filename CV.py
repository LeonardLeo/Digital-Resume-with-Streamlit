# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:09:08 2023

@author: lEO
"""

# DIGITAL CV
import streamlit as st
import pandas as pd
import time
import numpy as np
import base64

# -----> STREAMLIT FUNCTIONS <-----
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: repeat;
        background-attachment: scroll;
    }}
    </style>
    """,
        unsafe_allow_html = True
    )
    
# -----> STREAMLIT APP <-----
# RUN: cd Desktop/Digital CV/
# streamlit run CV.py
st.set_page_config(
    page_title = 'Onyiriuba Leonard',
    page_icon = '📜',
    layout = 'centered',
    initial_sidebar_state = 'auto',
    )

# Background Image
add_bg_from_local('img/magicpattern (3).png')

# Page Info
col4, col5 = st.columns([5, 1])
with col4:
    st.title('Full-Stack Data Scientist')
    
with col5:
    from PIL import Image
    img = Image.open('img/Profile.PNG')
    st.image(img, width = 70)
    


col1, col2, col3 = st.columns(3)
with col3:
    email = 'workwithtechleo@gmail.com'
    st.markdown(
    """
    <style>
    p {
        margin-bottom: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown("<p style='font-size: 14.5px;'>Call: +234 907 6488 226</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 14.5px;'>Email:<a href = {email}> {email}</a> </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14.5px;'>Address: Lagos, Nigeria.</p>", unsafe_allow_html=True)   

st.divider()
with st.container():
    st.subheader('Work Experience')
    with st.container():
        st.markdown("##### Power BI Instructor,")
        img1 = Image.open('img/Picture1.png')
        st.image(img1, width = 170)
        st.markdown("###### Gomycode, August 2023 - Present.")
        st.write("""
                 • Guided students in mastering DAX (Data Analysis Expressions), time-intelligence analysis, and understanding measures, resulting in a 95% proficiency rate in effective data analysis.
                 
                 • Mentored students in using Power BI and Tableau to expertly analyze data, enabling them to transform complex datasets into strategic insights for informed business decision-making while maintaining a Net Promoter Score of 90%.
                 
                 • Conducted data quality assessments and validation checks, emphasizing the importance of data accuracy and reliability, resulting in a 98% improvement in data quality awareness among students.
                 
                 • Taught students the mastery of ETL (Extract, Transform, Load) processes and a strong understanding of Power Query, leading to a 40% increase in query performance optimization and efficient data models for responsive dashboards and reports.
                 
                 • Acted as a subject matter expert in Power BI, offering guidance on best practices, design principles, and data visualization techniques to enhance the impact of analytics efforts.
                 """)
        
    st.markdown('<br> </br>', unsafe_allow_html=True)
    with st.container():
        st.markdown("##### Business Intelligence Instructor,")
        img1 = Image.open('img/Picture1.png')
        st.image(img1, width = 170)
        st.markdown("###### Gomycode, July 2023 - Present.")
        st.write("""
                 • Trained over 20 students in database management and achieved a 95% satisfaction rate in SQL training, enhancing data manipulation skills.
                 
                 • Ensured 100% proficiency in OLAP and OLTP systems among students through advanced knowledge sharing.
                 
                 • Provided comprehensive insights into data architecture, resulting in a 90% increase in informed data storage decisions.
                 
                 • Instructed students in Microsoft BI tools, leading to a 30% improvement in data quality and a 40% increase in tool adoption.
                 
                 • Implemented advanced data modeling and reporting tools, reducing data analysis time by 25% and increasing data visualization efficiency by 50%.
                 """)
                 
    st.markdown('<br> </br>', unsafe_allow_html=True)
    with st.container():
        st.markdown("##### Data Science Instructor,")
        img2 = Image.open('img/Picture1.png')
        st.image(img2, width = 170)
        st.markdown("###### Gomycode, February 2023 - Present.")
        st.write("• Achieved a high Net Promoter Score (NPS) of 90% across all mentoring groups, mentoring over 30 data scientists.")
        st.write("• Teaching students machine learning concepts, including Python, Numpy, Pandas, Sci-kit learn, and MLXtend, enabling them to create predictive models and algorithms.")
        st.write("• Guiding students in deep learning with PyTorch, Keras, and Tensorflow, allowing them to work on complex neural networks and advanced AI applications.")
        st.write("• Empowering students with data analysis skills using Python, Power BI, Tableau, and Pandas Profiling, resulting in extracting valuable insights from raw data.")
        st.write("• Providing hands-on experience in deploying data science solutions, introducing tools like Streamlit for converting models into practical applications.")
        st.write("• Educating students on database fundamentals, covering infrastructure, database design, and practical SQL training to manage and query data effectively.")
        
    st.markdown('<br> </br>', unsafe_allow_html=True)
    with st.container():
        st.markdown("##### Corper Analyst")
        img3 = Image.open('img/NYSC_LOGO.svg.png')
        st.image(img3, width = 50)
        st.markdown("###### National Youth Service Corps (NYSC), February 2022 - January 2023.")
        st.write('• Completed a one-year national service program in Ikeja, Lagos state.')
        st.write('• Contributed to community development projects and initiated data collection and analysis with a team of over 20 data enthusiasts to measure impact.')
        st.write('• Mentored youth on data analysis and visualization, enabling them to make informed decisions based on data insights.')
    
    st.markdown("<br> </br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("###### Data Analyst,")
        st.markdown("###### XCD Truckers Limited, April 2021 - January 2022.")
        st.write('• Analyzed and interpreted large datasets, identifying trends and patterns that led to a 20% increase in data-driven insights.')
        st.write('• Developed and maintained databases, resulting in a 98% accuracy and completeness rate of data, improving data reliability.')
        st.write('• Designed and implemented data visualization dashboards, which enhanced communication of insights to stakeholders and led to a 25% improvement in data comprehension.')
        st.write('• Automated and optimized data processing workflows, improving efficiency by 30% and reducing processing time.')
        st.write('• Collaborated with cross-functional teams, resulting in the identification of business opportunities that contributed to a 15% increase in overall decision-making effectiveness.')

st.divider()
with st.container():
    st.subheader('Skills')
    with st.expander(label = "Data Analysis & Database Management"):
        st.divider()
        st.write("""
                 • SQL (MySQL, Microsoft SQL Server)
                 
                 • Database Design (Conceptual, Logical, and Physical Modeling)
                 
                 • OLAP and OLTP Operations
                 """)
    with st.expander(label = "Python for Machine Learning"):
        st.divider()
        st.write("""
                 • Pandas
                 
                 • Numpy
                 
                 • Scikit Learn
                 
                 • Matplotlib
                 
                 • Seaborn
                 
                 • Pandas Profiling
                 
                 • Sweetviz
                 
                 • LazyPredict
                 
                 • MLXtend
                 
                 • NLTK
                 """)
    with st.expander(label = "Python for Deep Learning"):
        st.divider()
        st.write("""
                 • Keras
                 
                 • Theano
                 
                 • Tensorflow
                 
                 • Pytorch
                 """)
    with st.expander(label = "Business Intelligence & Data Vizualization"):
        st.divider()
        st.write("""
                 • Power BI
                 
                 • Tableau
                 
                 • Microsoft BI Toolkit (SQL Server, SSAS, SSIS, SSRS, SQL Server Master Data Service)
                 """)
    with st.expander(label = "Data Science & Data Analysis with Cloud Technologies"):
        st.divider()
        st.write("""
                 • VertexAI
                 
                 • DataPrep
                 
                 • Looker
                 
                 • BigQuery
                 
                 • DataProc
                 """)
    with st.expander(label = "Application Development"):
        st.divider()
        st.write("""
                 • Python
                 
                 • Streamlit for Deployment
                 
                 • Git & Github
                 
                 • Javascript
                 
                 • HTML & CSS
                 """)
    
        
        
st.divider()
with st.container():
    st.subheader('Education')
    col9, col10 = st.columns(2)
    with col9:
        with st.expander("University"):
            st.divider()
            with st.container():
                st.markdown("###### Alchemy University, USA.")
                st.markdown("###### May 2023 - Present.")
                st.write('• Ethereum Developer.')
                st.write('• Web3.')
              
            st.markdown('<br></br>', unsafe_allow_html = True)
            st.divider()
            with st.container():
                st.markdown("###### University of Lagos, Nigeria.")
                st.markdown("###### September 2015 - November 2019.")
                st.write('• Bachelor of Science, Economics.')
                st.write('• Second-Class Honours (Upper Division)')
                st.write('• PROJECT: Impact of Government Expenditure on Economic Growth (1985-2017)')
                
            st.markdown('<br></br>', unsafe_allow_html = True)
            
    with col10:
        with st.expander("High School"):
            st.divider()
            with st.container():
                st.markdown("###### Grandmates Secondary School.")
                st.markdown("###### January 2014 - June 2015.")
                st.write('• SSS 2-3')
                st.write('• Commercial Student.')
              
            st.markdown('<br></br>', unsafe_allow_html = True)
            st.divider()
            with st.container():
                st.markdown("###### Maryland Comprehensive Secondary School (MCSS).")
                st.markdown("###### September 2009 - December 2013.")
                st.write('• JSS 1-3')
                st.write('• SSS 1-2')
                st.write('• Commercial Student.')
                
            st.markdown('<br></br>', unsafe_allow_html = True)    
    
st.divider()
with st.container():
    st.subheader('Projects & Socials')
    col11, col12 = st.columns(2)
    with col11:
        with st.expander(label = "Projects"):
            st.divider()
            st.markdown("""
                     • Chatbot for Unilag Finance Department.
                     
                     • LaLiga 2021/2022 Season Table Analysis.
                     
                     • Video Game Sales Analysis (1980 - 2022).
                     
                     • NBA Analysis (1980 - 2022).
                     
                     • Steph Curry NBA Analysis.
                     
                     • US Data Analysis.
                     
                     • Customer Churn Predictive Model.
                     
                     • Hate Speech Detection Model.
                     
                     • Facebook Posts Sentiment Analysis.
                     
                     • Email Spam Detection Model.
                     
                     • Face Detection Model.
                     
                     • SMS Spam Detection Model.
                     
                     • Customer Segmentation Model.
                     """)
            st.divider()
            st.button(label = "View")
                     
    with col12:
        with st.expander(label = "Socials"):
            st.markdown("""
                     Chatbot for Unilag Finance Department.
                     """)

    


    
        
    