import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Resume - Vivek Prasath", layout="centered", initial_sidebar_state="auto")
col1, col2 = st.columns([1, 3])  # Adjust column ratios as needed

# Add the GIF to the left column
with col1:
    st.image("my logo.gif", use_container_width=True)

# Add other content in the right column
with col2:
    st.title("Welcome to my portfolio")
# Header Section
st.title(" Vivek Prasath S")
st.subheader("Data Analyst | Business Analyst | Power BI Developer")
st.write(" 📞 +91 96771 65731 |📧 vsrajan2k@gmail.com |🌍 Trichy, India")
gif_url = "https://media1.tenor.com/m/dzock0eDxV0AAAAd/gofiber-really.gif"  # Replace with your GIF URL or local path
css_code = f"""
<style>
    body {{
        background: url("{gif_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    .stApp {{
        background: rgba(255, 255, 255, 0);  /* Add a semi-transparent background for better text readability */
        border-radius: 100px;
        padding: 20px;
    }}
</style>
"""
st.markdown(css_code,unsafe_allow_html=True)
st.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivek-prasath/)"
)

# Objective Section
st.header("Objective")
st.write("""
To leverage my solid background in accounting alongside my acquired skills in data analysis 
to embark on a rewarding career as a Data Analyst. Eager to apply my analytical mindset, 
attention to detail, and aptitude for problem-solving to extract actionable insights from 
complex datasets, contributing effectively to organizational success while continuously enhancing 
my proficiency in data analytics tools and techniques.
""")

# Technical Skills Section
st.header("Technical Skills")
skills = [
    {"SQL (SQL Server, MySQL)"},
    "Python (NumPy, Pandas, Matplotlib, Seaborn, Plotly)",
    "Tableau",
    "Power Platform (Power BI, Power Apps, Power Automate, Power Virtual Agents)",
    "Excel (Conditional Formatting, V-Lookup, Pivot Tables and Charts, Formulas)",
    "SharePoint", "Sharegate", "Data Collection", "Data Cleaning",
    "Data Modeling", "Data Visualization", "Microsoft Azure","data science","data analytics"
]
for skill in skills:
    st.write(f"- {skill}")
# st.write(", ".join(skills))
st.header("Professional Skills")
soft_skills = [
    "Critical Thinking","Problem Solving","Effective Communication","Creative Thinking","Analytical Thinking"
]
for soft_skill in soft_skills:
    st.write(f"- {soft_skill}")
# Certifications Section
st.header("Certifications")
certifications = [
    {"Name":"Microsoft Certified Azure Cloud Administrator (AZ-104)","image":"my badge.png"},
    {"Name":"Microsoft Certified Data Analyst Associate (DA-100)","image":"cloud badge.png"}
]
for cert in certifications:
    col1,col2 = st.columns([1,3])
    with col1:
        st.image(cert['image'],use_container_width=True)
        with col2:
            st.write(f"- {cert['Name']}")

# Projects Section
st.header("Projects")
projects = [
    {
        "title": "Adventure Works Database Project Using Power BI",
        "description": """
- 	In this project I had used SQL server connector in direct query mode as the for importing the data.
- 	Using the data, I had developed Product Dashboard and product details reports using power BI Desktop and created Power BI dashboard. And developed the report and dashboard as power BI apps
- 	The aim for the preparation of this project is to showcase my ability and my knowledge to recruiters in SQL server and Power BI.
- 	The and tools used queries handled by me in this project
- [GitHub Code](https://github.com/vivekprasathsoundar/sql.git)

        """
    },
    {
        "title": "Weather Analysis Project",
        "description": """
-	This is a weather analysis project created to assist weather forecasters in predicting future weather conditions.
-	In this project, I used Power Query Editor in Power BI for data cleaning and Power BI Desktop for data visualization.
-	In the dashboard, I presented the trends related to wind speed, pressure deviation, and variance in relative humidity.

        """
    },
    {
        "title": "Kevin Cookies Company Marketing Dashboard",
        "description": """
- 	This is a marketing analysis project about Kevin Cookies Company created to assist the marketers of that which highest selling product and total profit and revenue over the period.
-	In these projects I had used pandas for importing and data cleaning and for visualization I had used matplotlib.
-	These dashboards will help them to predict and derive strategies to increase their demand for their products and their profit.

        """
    },
    {
        "title": "Kevin Cookies Company Product Analysis Dashboard",
        "description": """
- 	This is a product analysis project focused on Kevin Cookies Company, aimed at assisting the company in enhancing its production strategies. By analyzing the number of units sold over a specific period, the company can refine its product offerings and better cater to market preferences.
-	In this project, I utilized the Pandas library for data importing and data cleaning. Additionally, I employed the Streamit package in Python for data visualization and dashboard deployment.
-	Within the dashboard, I showcased the number of units sold over time, categorized by different product types
-  [Live Demo](https://python-project-using-app-hpsgzgrufkxkzuvszslrry.streamlit.app/)
        """
    },
    {
"title": "User Access Request",
        "description": """
"In this freelance project, I completed the following tasks:
-	Imported data using the SharePoint connector and performed transformation steps, such as removing unnecessary columns, renaming columns, and changing data types, in order to create reports in Power BI Desktop.
- Published the report in the Power BI Service and created a dashboard based	on the information extracted from the report. Sharing the dashboard to the client.
-	Deployed the report created in the SharePoint site using migration tools known as Sharegate.
-	Connected to the SQL database server using direct server authentication to build a connection string and, in Power BI Report Builder (SSRS SOFTWARE), created paginated reports containing sub-report tables and matrices by Utilizing stored procedures and views provided by the database.
-	Finally, delivered the output of paginated reports in PDF format using the export option in Power BI Report Builder."

"""
    }
]
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
# Experience Section
st.header("Experience")
experience = [
    {'Name':"Data Analyst | Prowesstics IT Services, Chennai (Apr 2024 - Nov 2024)",'image':'prowesstics logo.png'},
    {'Name':"Data Analyst | VDart Technologies Private Limited (Jul 2022 - Nov 2022)",'image':'vdart logo.jpg'},
    {'Name':"Accountant (Part-Time) | NAS Engineering Services, Mathur (Jan 2021 - Feb 2024)",'image':'NAS engineering services.png'},
    #{'Name':"Data Analyst | VDart Technologies Private Limited (Jul 2022 - Nov 2022)","image":}
]

for exp in experience:
    col1,col2 = st.columns([1,3])
    with col1:
        st.image(exp['image'],use_container_width=True)
        with col2:
                 st.write(f"- {exp['Name']}")

# Education Section
st.header("Education")
education = [
    {'Name':"Bachelor of Commerce (B.Com) | Bishop Heber College, Trichy (2015 - 2018)","image":"bachelor_logo.png"},
    {'Name':"Master of Commerce (M.Com) | Bharathidasan University, Trichy (2018 - 2020)","image":"master_logo.png"}
]
for edu in education:
    col1,col2 = st.columns([1,3])
    with col1:
        st.image(edu['image'],use_container_width=True)
        with col2:
            st.write(f"- {edu['Name']}")

# Footer
sidebar_css = """
<style>
    [data-testid="stSidebar"] {
        background-color: grey;
    }
</style>
"""

# Inject the CSS
st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)
st.sidebar.image("my_photo.gif",use_container_width=True)
st.sidebar.markdown(css_code, unsafe_allow_html=True)
st.sidebar.title("Contact Me")
st.sidebar.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivek-prasath/)"
)
#st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/vivek-prasath/)")
st.sidebar.write("📧 vsrajan2k@gmail.com")
st.sidebar.write("📞 +91 96771 65731")
