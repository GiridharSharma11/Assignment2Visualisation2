'''
Giridhar Gopal Sharma
29223709
Data Extraction
'''

import pandas as pd

# Load dataset
dataset = pd.read_csv("suicide.csv")

# Analyzing Suicide Data Based on Gender

gender_data = dataset[["sex"]]
first100_gender = gender_data.head(100)
ordered_gender = first100_gender.sort_values(by=["sex"], ascending=True)
ordered_gender
ordered_gender.to_excel(r'C:\Users\User\Desktop\FIT3179\Data Visualisation 2\gender_suicides.xlsx', index=True, header=True)

# Update column names
dataset.rename(columns={"suicides/100k pop": "suicides_rate",
                        "gdp_for_year ($)": "annual_gdp", 
                        "gdp_per_capita ($)": "gdp_per_person"}, inplace=True)

dataset.head()

# Suicides by country and gender
country_gender_data = dataset.groupby(by=["country", "sex"])["suicides_no"].sum().reset_index()
country_gender_data["country"]
country_gender_data.to_excel(r'C:\Users\User\Desktop\FIT3179\Data Visualisation 2\country_gender_suicides.xlsx', index=False, header=True)

# Analyzing Suicide Rates by Age Group and Country

age_group_data = dataset.groupby(by=["country", "age"])["suicides_rate"].sum().reset_index()
ordered_age_group = age_group_data.sort_values(by=["suicides_rate"], ascending=False)
selected_countries_data = ordered_age_group.loc[(ordered_age_group["country"].isin([
    "Republic of Korea", "Hungary", "Austria", "Bulgaria", "Singapore",
    "France", "Russian Federation", "Cuba", "Lithuania", "Belgium"]))]

sorted_selected_countries = selected_countries_data.sort_values(by=["country"])
sorted_selected_countries
sorted_selected_countries.to_excel(r'C:\Users\User\Desktop\FIT3179\Data Visualisation 2\top_countries_age_group_suicides.xlsx', index=False, header=True)

# Analyzing Annual Suicide Rates by Age Group

annual_suicides_data = dataset.groupby(by=["year", "age"])["suicides_rate"].sum().reset_index()
ordered_annual_suicides = annual_suicides_data.sort_values(by=["year"], ascending=True)
ordered_annual_suicides
ordered_annual_suicides.to_excel(r'C:\Users\User\Desktop\FIT3179\Data Visualisation 2\annual_age_group_suicides.xlsx', index=False, header=True)

# Analyzing Suicide Rates by Country

country_suicides_data = dataset.groupby(by=["country"])["suicides_rate"].sum().reset_index()
ordered_country_suicides = country_suicides_data.sort_values(by=["suicides_rate"], ascending=False)
ordered_country_suicides.to_excel(r'C:\Users\User\Desktop\FIT3179\Data Visualisation 2\country_suicides_rates.xlsx', index=False, header=True)
ordered_country_suicides
