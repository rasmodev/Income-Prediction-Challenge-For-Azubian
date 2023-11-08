import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import catboost
from sklearn.impute import SimpleImputer
import requests

# Custom CSS styles for the top bar
st.markdown(
    """
    <style>
    .top-bar {
        background-color: #FF4C1B;
        color: white;
        padding: 1rem;
        text-align: center;
    }
    .top-bar a {
        text-decoration: none;
        color: white;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def home_page():
    # Page title and banner image
    st.title("Income Prediction App")
    st.image("https://i.ytimg.com/vi/WULwst0vW8g/maxresdefault.jpg")
    
    st.write("""
    The "Income Prediction Challenge for Azubian" is a data-driven initiative that seeks to address the critical issue of income inequality in developing nations. The project focuses on utilizing machine learning techniques to predict whether an individual's income falls above or below a specific income threshold. By developing a robust predictive model, we aim to contribute to more accurate and cost-effective methods of monitoring key population indicators, such as income levels, between census years. This valuable information will empower policymakers to take more informed actions to mitigate and manage income inequality on a global scale.
    """)

    # The Problem of Income Inequality
    st.header("The Problem: Income Inequality 💸")
    st.write(
        """
        Income inequality, a pervasive challenge that hinders economic progress and social well-being, demands innovative solutions. The "Income Prediction Challenge for Azubian" tackles this issue head-on, harnessing the power of machine learning to predict individual income levels.

        **Key Challenges of Income Inequality:** ⚠

        1. **Limited Economic Mobility:** 📉

            Individuals from lower-income households often face barriers to education and professional growth, perpetuating income disparities.

        2. **Healthcare Disparities:** 🩺

            Income inequality often translates into unequal access to quality healthcare, leading to adverse health outcomes for lower-income individuals.

        3. **Education Gaps:** 📚

            Children from low-income households may have limited access to quality education, hindering their future opportunities.

        4. **Social Unrest:** 💢

            Extreme income inequality can fuel social unrest as individuals feel disenfranchised and discouraged.

        5. **Economic Impact:** 📉

            Income inequality impedes economic growth by reducing aggregate demand and creating economic instability.

        6. **Policymaking Challenges:** 🧩

            Policymakers require accurate data and insights to formulate effective strategies for reducing income inequality.
            """)

    
def solution():
    # Page title
    st.title("Income Prediction Solution")
    st.image("https://d2gg9evh47fn9z.cloudfront.net/1600px_COLOURBOX15103453.jpg")

    # Solution Overview
    st.header("Solution 💡: Combating Income Inequality with Data-Driven Solutions 📈 ")
    st.write("""

        The "Income Prediction Challenge for Azubian" utilizes machine learning to predict individual income levels, providing valuable data to policymakers for informed action. This data-driven approach offers several advantages:

        * **Cost-Effectiveness:** 💰

            Machine learning models are more cost-effective than traditional census methods.

        * **Timeliness:** ⏱️

            Income predictions can be generated frequently, enabling timely interventions.

        * **Scalability:** 🚀

            Machine learning models can be scaled to predict incomes for large populations, making them applicable to a wide range of scenarios.
        """)
    
    st.header("Objectives: 🎯")
    st.write("""
       1. **Income Prediction Model:** Develop a robust machine learning model to accurately predict individual income levels.

       2. **Economic Inequality Mitigation:** Empower policymakers with data-driven insights to effectively address income inequality.

       3. **Cost and Accuracy Improvement:** Enhance income-level monitoring through a cost-effective and accurate method compared to traditional census methods.

        Join us in tackling income inequality with data-driven solutions!
        """)

    # Model Description
    st.header("Model Description")
    st.write("""
    **Model Training:**
    *Trained on a dataset of demographic and socioeconomic factors influencing income levels 📊
    
    * A [CatBoost Classifier](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier) supervised learning algorithm used for model development ⚙️
    
    **Model Evaluation:**
    * Performance assessed using metrics like accuracy, precision, recall, and F1 score 📈📊
    
    * Metrics evaluate the model's ability to correctly classify individual income levels ☑️
    """)

    # Impact and Benefits
    st.header("Impact and Benefits 📈")
    st.write("""
    
    **Empowering Policymakers and Promoting Equitable Growth 📈**

    By providing accurate and timely insights into income distribution, we can empower policymakers to make informed decisions that:

    * Enhance understanding of income patterns 📊

    * Identify areas with high income inequality 📍

    * Target interventions to address income gaps 🎯

    * Effectively allocate resources to poverty reduction 💰

    * Promote economic mobility for individuals from low-income backgrounds ⬆️

    Overall, this tool has the potential to make a meaningful contribution to the fight against income inequality and promote a more just and equitable society. ⚖️
    """)


def perform_eda():
    st.title("Exploratory Data Analysis")
    st.write("""
        📊📈 Welcome to the Exploratory Data Analysis for the "Income Prediction" Project! 📈📊
        Dive into the wealth of data and uncover insights about income prediction. Explore the data and understand the factors that contribute to an individual's income level. Let's begin our data-driven journey! 💰🔍
        """)

    # Show the Power bi dashboard
    power_bi()

def power_bi():
    """
    Embeds the Power BI report with specified dimensions and full-screen height.
    """

    st.subheader("Exploring Income Data")
    st.write("Let's dive deeper into the data to understand income distribution and relationships between variables.")

    # Embed the Power BI iframe with specified dimensions
    power_bi_html = """
    <iframe title="Sepsis" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiYWI1NTRiNTgtMzc5Yi00MjUzLTk4YzAtYjFlZTk3ZWUwMjEyIiwidCI6IjQ0ODdiNTJmLWYxMTgtNDgzMC1iNDlkLTNjMjk4Y2I3MTA3NSJ9" frameborder="0" allowFullScreen="true"></iframe>
    """

    st.components.v1.html(power_bi_html)

    # Ensure full-screen height using CSS
    with st.empty():
        st.write("""
        <style>
            html, body {
              height: 100%;
              margin: 0;
              padding: 0;
            }

            iframe {
              width: 100%;
              height: 100vh;
            }
        </style>
        """, unsafe_allow_html=True)


def prediction():

    # Load the saved model and unique values:
    with open("model_and_key_components.pkl", "rb") as f:
        components = pickle.load(f)
    
    # Extract the individual components
    dt_model = components["model"]
    unique_values = components["unique_values"]
    
    
    st.image("https://i.ytimg.com/vi/WULwst0vW8g/maxresdefault.jpg")
    st.title("Income Prediction App")
    
    # Sidebar with input field descriptions
    st.sidebar.header("Description of the Required Input Fields")
    st.sidebar.markdown("**Age**: Enter the age of the individual (e.g., 25, 42, 57).")
    st.sidebar.markdown("**Gender**: Select the gender of the individual (e.g., Male, Female).")
    st.sidebar.markdown("**Education**: Choose the highest education level of the individual (e.g., Bachelors Degree, High School Graduate, Masters Degree).")
    st.sidebar.markdown("**Worker Class**: Select the class of worker for the individual (e.g., Private, Government, Self-employed).")
    st.sidebar.markdown("**Marital Status**: Choose the marital status of the individual (e.g., Married, Never married, Divorced).")
    st.sidebar.markdown("**Race**: Select the race of the individual (e.g., White, Black, Asian-Pac-Islander).")
    st.sidebar.markdown("**Hispanic Origin**: Choose the Hispanic origin of the individual (e.g., Mexican, Puerto Rican, Cuban).")
    st.sidebar.markdown("**Full/Part-Time Employment**: Select the employment status as full-time or part-time (e.g., Full-time schedules, Part-time schedules).")
    st.sidebar.markdown("**Wage Per Hour**: Enter the wage per hour of the individual (numeric value, e.g., 20.50).")
    st.sidebar.markdown("**Weeks Worked Per Year**: Specify the number of weeks the individual worked in a year (numeric value, e.g., 45).")
    st.sidebar.markdown("**Industry Code**: Choose the category code of the industry where the individual works (e.g., Category 1, Category 2).")
    st.sidebar.markdown("**Major Industry Code**: Select the major industry code of the individual's work (e.g., Industry A, Industry B).")
    st.sidebar.markdown("**Occupation Code**: Choose the category code of the occupation of the individual (e.g., Category X, Category Y).")
    st.sidebar.markdown("**Major Occupation Code**: Select the major occupation code of the individual (e.g., Occupation 1, Occupation 2).")
    st.sidebar.markdown("**Total Employed**: Specify the number of persons worked for the employer (numeric value, e.g., 3, 5).")
    st.sidebar.markdown("**Household Stat**: Choose the detailed household and family status of the individual (e.g., Single, Married-civilian spouse present).")
    st.sidebar.markdown("**Household Summary**: Select the detailed household summary (e.g., Child under 18 never married, Spouse of householder).")
    st.sidebar.markdown("**Veteran Benefits**: Choose whether the individual receives veteran benefits (Yes or No).")
    st.sidebar.markdown("**Tax Filer Status**: Select the tax filer status of the individual (e.g., Single, Joint both 65+).")
    st.sidebar.markdown("**Gains**: Specify any gains the individual has (numeric value, e.g., 1500.0).")
    st.sidebar.markdown("**Losses**: Specify any losses the individual has (numeric value, e.g., 300.0).")
    st.sidebar.markdown("**Dividends from Stocks**: Specify any dividends from stocks for the individual (numeric value, e.g., 120.5).")
    st.sidebar.markdown("**Citizenship**: Select the citizenship status of the individual (e.g., Native, Foreign Born- Not a citizen of U S).")
    st.sidebar.markdown("**Year of Migration**: Enter the year of migration for the individual (numeric value, e.g., 2005).")
    st.sidebar.markdown("**Country of Birth**: Choose the individual's birth country (e.g., United-States, Other).")
    st.sidebar.markdown("**Importance of Record**: Enter the weight of the instance (numeric value, e.g., 0.9).")
    
    # Create the input fields in the order of your DataFrame
    input_data = {
        'age': 0,  # Default values, you can change these as needed
        'gender': unique_values['gender'][0],
        'education': unique_values['education'][0],
        'worker_class': unique_values['worker_class'][0],
        'marital_status': unique_values['marital_status'][0],
        'race': unique_values['race'][0],
        'is_hispanic': unique_values['is_hispanic'][0],
        'employment_commitment': unique_values['employment_commitment'][0],
        'employment_stat': unique_values['employment_stat'][0],
        'wage_per_hour': 0,  # Default value
        'working_week_per_year': 0,  # Default value
        'industry_code': 0,  # Default value
        'industry_code_main': unique_values['industry_code_main'][0],
        'occupation_code': 0,  # Default value
        'occupation_code_main': unique_values['occupation_code_main'][0],
        'total_employed': 0,  # Default value
        'household_stat': unique_values['household_stat'][0],
        'household_summary': unique_values['household_summary'][0],
        'vet_benefit': 0,  # Default value
        'tax_status': unique_values['tax_status'][0],
        'gains': 0,  # Default value
        'losses': 0,  # Default value
        'stocks_status': 0,  # Default value
        'citizenship': unique_values['citizenship'][0],
        'mig_year': 0,
        'country_of_birth_own': 'United-States',
        'importance_of_record': 0.0  # Default value
    }
    
    # Create the input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        input_data['age'] = st.number_input("Age", min_value=0, key='age')
        input_data['gender'] = st.selectbox("Gender", unique_values['gender'], key='gender')
        input_data['education'] = st.selectbox("Education", unique_values['education'], key='education')
        input_data['worker_class'] = st.selectbox("Class of Worker", unique_values['worker_class'], key='worker_class')
        input_data['marital_status'] = st.selectbox("Marital Status", unique_values['marital_status'], key='marital_status')
        input_data['race'] = st.selectbox("Race", unique_values['race'], key='race')
        input_data['is_hispanic'] = st.selectbox("Hispanic Origin", unique_values['is_hispanic'], key='is_hispanic')
        input_data['employment_commitment'] = st.selectbox("Full/Part-Time Employment", unique_values['employment_commitment'], key='employment_commitment')
        input_data['employment_stat'] = st.selectbox("Has Own Business Or Is Self Employed", unique_values['employment_stat'], key='employment_stat')
        input_data['wage_per_hour'] = st.number_input("Wage Per Hour", min_value=0, key='wage_per_hour')
    
    with col2:
        input_data['working_week_per_year'] = st.number_input("Weeks Worked Per Year", min_value=0, key='working_week_per_year')
        input_data['industry_code'] = st.selectbox("Category Code of Industry", unique_values['industry_code'], key='industry_code')
        input_data['industry_code_main'] = st.selectbox("Major Industry Code", unique_values['industry_code_main'], key='industry_code_main')
        input_data['occupation_code'] = st.selectbox("Category Code of Occupation", unique_values['occupation_code'], key='occupation_code')
        input_data['occupation_code_main'] = st.selectbox("Major Occupation Code", unique_values['occupation_code_main'], key='occupation_code_main')
        input_data['total_employed'] = st.number_input("Number of Persons Worked for Employer", min_value=0, key='total_employed')
        input_data['household_stat'] = st.selectbox("Detailed Household and Family Status", unique_values['household_stat'], key='household_stat')
        input_data['household_summary'] = st.selectbox("Detailed Household Summary", unique_values['household_summary'], key='household_summary')
        input_data['vet_benefit'] = st.selectbox("Veteran Benefits", unique_values['vet_benefit'], key='vet_benefit')
    
    with col3:
        input_data['tax_status'] = st.selectbox("Tax Filer Status", unique_values['tax_status'], key='tax_status')
        input_data['gains'] = st.number_input("Gains", min_value=0, key='gains')
        input_data['losses'] = st.number_input("Losses", min_value=0, key='losses')
        input_data['stocks_status'] = st.number_input("Dividends from Stocks", min_value=0, key='stocks_status')
        input_data['citizenship'] = st.selectbox("Citizenship", unique_values['citizenship'], key='citizenship')
        input_data['mig_year'] = st.selectbox("Migration Year", unique_values['mig_year'], key='migration_year')
        input_data['country_of_birth_own'] = st.selectbox("Country of Birth", unique_values['country_of_birth_own'], key='country_of_birth_own')
        input_data['importance_of_record'] = st.number_input("Importance of Record", min_value=0, key='importance_of_record')
    
    # Button to make predictions
    if st.button("Predict"):
        # Transform the input data to a DataFrame for prediction
        input_df = pd.DataFrame([input_data])
    
        # Make predictions
        prediction = dt_model.predict(input_df)
        prediction_proba = dt_model.predict_proba(input_df)
    
        # Display prediction result
        st.subheader("Prediction")
        if prediction[0] == 1:
            st.success("This individual is predicted to have an income of over $50K.")
        else:
            st.error("This individual is predicted to have an income of under $50K")
    
        # Show prediction probability
        st.subheader("Prediction Probability")
        st.write(f"The probability of the individual having an income over $50K is: {prediction_proba[0][1]:.2f}")
          

# Add navigation to the selected page
selected_page = st.selectbox("Select a page", ["Home", "Solution", "EDA", "Predict Income"])

if selected_page == "Home":
    home_page()
elif selected_page == "Solution":
    solution()   
elif selected_page == "EDA":
    perform_eda()
else:
    prediction()