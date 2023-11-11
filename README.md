# Income-Prediction-ML-Project-with-FAST-API-Integration
This repository contains a machine learning project focused on predicting income levels and integrating the model into a web application using FAST API.

<p align="center">
  <img src="/screenshots/default.jpg" width="800">
</p>

This project aims to leverage machine learning to predict income levels, addressing the challenges of income inequality and providing insights for policymakers.

## Summary
|     Jupyter Notebook                       |     Power BI Dashboard|     Published Article|    Deployed App on Hugging Face   
| -------------                  | -------------    | -------------    |    -----------------
|[Notebook with analysis and model development](https://github.com/rasmodev/Income-Prediction-Challenge-For-Azubian/blob/main/dev/Income_Prediction.ipynb)|  [Interactive Dashboard]() |  [Published Article on Medium]() |[Link to App](https://huggingface.co/spaces/rasmodev/Income_Prediction_Streamlit)

## FastAPI Interface
After clicking on the link to the working FastAPI, click on "Try It Out", provide the required details, and click on the **"EXECUTE"** button.

![App Screenshot](screenshots/app_home.png)

### Before Prediction

![App Screenshot](screenshots/app_solution.png)

### After Prediction
![App Screenshot](screenshots/app_pred.png)

# Repository Contents:
- [Project Overview](#project-overview)
- [Project Setup](#project-setup)
- [Data Fields](#data-fields)
- [Getting Started](#getting-started)
- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Author](#author)


# Project Overview:
**i. Data Collection and Preprocessing:** I loaded and preprocessed a comprehensive dataset containing income-related data to train and evaluate the income prediction model.

**ii. Machine Learning Model:** I implemented a machine learning model tailored for predicting income levels. This model has been fine-tuned to achieve high accuracy in predicting income thresholds.

**iii. FAST API Integration:** I've seamlessly integrated the trained machine learning model into a web application using FAST API. This web application allows users to input individual data and receive instant predictions regarding income levels.

**iv. Usage and Deployment:** In this README file, you will find detailed instructions on how to use and deploy this web application, making it user-friendly for both developers and policymakers.

# Project Setup:
To set up the project environment, follow these steps:

i. Clone the repository:

```bash 
git clone https://github.com/your_username/Income-Prediction-ML-Project-with-FastAPI-Deployment.git
```

ii. Create a virtual environment and install the required dependencies:

- **Windows:**
  ```bash
  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
  ```

- **Linux & MacOS:**
  ```bash
  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
  ```

## Data Fields
The data used in this project consists of a diverse collection of income-related attributes obtained from [source](your_data_source_link).

| Column Name                | Data Type   | Description                                      |
|----------------------------|-------------|--------------------------------------------------|
| Age                        | Numeric     | Age of the individual                            |
| Gender                     | Categorical | Gender of the individual                        |
| Education                  | Categorical | Education level of the individual               |
| Class Of Worker            | Categorical | Class of worker                                 |
| Education Institute        | Categorical | Enrollment status in an educational institution in the last week  |
| Marital Status             | Categorical | Marital status                                  |
| Race                       | Categorical | Race                                            |
| Hispanic Origin            | Categorical | Hispanic origin                                 |
| Employment Commitment      | Categorical | Full or part-time employment status             |
| Unemployment Reason        | Categorical | Reason for unemployment                         |
| Employment Stat            | Categorical | Owns a business or is self-employed             |
| Wage Per Hour               | Numeric     | Wage per hour                                   |
| Labor Union Membership     | Categorical | Member of a labor union                         |
| Weeks Worked In A Year      | Numeric     | Weeks worked in a year                          |
| Industry Code              | Categorical | Industry category                               |
| Major Industry Code        | Categorical | Major industry category                         |
| Occupation Code            | Categorical | Occupation category                             |
| Major Occupation Code       | Categorical | Major occupation category                       |
| Num Persons Worked For Employer | Numeric | Number of persons worked for employer         |
| Household and Family Stat   | Categorical | Detailed household and family status            |
| Household Summary          | Categorical | Detailed household summary                      |
| Under 18 Family            | Categorical | Family members under 18                         |
| Veterans Admin Questionnaire| Categorical | Filled income questionnaire for Veterans Admin |
| Vet Benefit                | Categorical | Veteran benefits                                |
| Tax Filer Status           | Categorical | Tax filer status                                |
| Gains                      | Numeric     | Gains from financial investments                |
| Losses                     | Numeric     | Losses from financial investments               |
| Stocks Status              | Categorical | Dividends from stocks                           |
| Citizenship                | Categorical | Citizenship status                             |
| Migration Year             | Numeric     | Year of migration                               |
| Country Of Birth - Individual | Categorical | Individual's birth country                     |
| Country Of Birth - Father   | Categorical | Father's birth country                          |
| Country Of Birth - Mother   | Categorical | Mother's birth country                          |
| Migration Code Change In MSA | Categorical | Migration code - Change in MSA                   |
| Migration Prev Sunbelt      | Categorical | Migration previous Sunbelt                      |
| Migration Code Move Within Reg | Categorical | Migration code - Move within region              |
| Migration Code Change In Reg | Categorical | Migration code - Change in region                |
| Residence 1 Year Ago        | Categorical | Lived in this house one year ago                |
| Old Residence Region        | Categorical | Region of previous residence                   |
| Old Residence State         | Categorical | State of previous residence                    |
| Importance Of Record        | Numeric     | Weight of the instance                          |
| Income Above 50k           | Categorical | Binary indicator if income is above $50,000     |


# Machine Learning Lifecycle
I employed the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology in this project. 

<p align="center">
  <img src="screenshots/CRISP-DM.png" width="500">
</p>

Here are the steps I undertook:

## Business Understanding:

I began by understanding the problem domain, which involved predicting income levels.
I defined the project goals and objectives, such as addressing income inequality through data-driven insights.

## Data Understanding:
I collected the dataset from [your_data_source_link], which included various income-related attributes. After an overview of the first few columns, I formulated hypotheses and key analytical questions that would guide the understanding of the dataset.

**Hypothesis:** 
Null Hypothesis (H0): There is no significant association between the individual's age and income level.

Alternative Hypothesis (H1): There is a significant association between the individual's age and income level.

**Key

 Analytical Questions:** 

- i. Are there any correlations or patterns between numerical features (e.g., age, education) and income levels?

- ii. How does the distribution of key numerical variables (e.g., age) differ between income categories?

- iii. Is there a relationship between education level and income?

### Understanding the datasets
I conducted an in-depth exploration of the datasets to gain insights into the available variables, their distributions, and relationships.

...

## Data Preparation:
- I preprocessed the data by performing data cleaning, including handling missing values and encoding categorical variables.
- I conducted feature engineering to select relevant features and prepare them for modeling.

...

## Modeling:

- I split the dataset into training and evaluation sets.
- I used various classification algorithms to predict income levels.
- I assessed model performance using evaluation metrics such as accuracy and F1-score.

The model performance was as follows:

...

## Evaluation:

I evaluated the model's performance on the testing dataset to ensure its generalizability.
I used various evaluation metrics to assess how well the model predicted income levels.

...

## Deployment:
**i. FastAPI**. 
The model is deployed as a FastAPI web service, which provides an API for income prediction. This deployment offers an intuitive interface for users to input individual data and obtain predictions.

**ii. Docker Containerization**
The application is containerized using Docker, making it easy to package and run in various environments with consistent behavior.

**iii. Hugging Face Deployment**
The application is containerized using Docker, making it easy to package and run in various environments with consistent behavior.

# Conclusion
Following the CRISP-DM methodology, I systematically addressed the income prediction problem, from understanding the business context to deploying a machine learning model as a practical tool for addressing income inequality.

# Author

`Rasmo Wanyama`

`Data Analyst/Data Scientist`

Let's connect on LinkedIn:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rasmo-/) 

# Acknowledgments:
We would like to thank the open-source community and the data providers who contributed to the dataset used in this project. Their efforts have made advancements in income prediction possible.

Feel free to explore the code, use the web application, and contribute to the project's development. Data-driven insights can contribute to a more equitable society, and together, we can make a difference.

---

Feel free to adapt the content, and if you have specific links or screenshots you'd like to include, replace the placeholders accordingly.
