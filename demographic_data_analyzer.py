#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[14]:


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv') 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = race_count=(df['race']).value_counts()

    # What is the average age of men?
    average_age_men = round((((df.loc[df['sex']=='Male',['age']]).mean())['age']),1)

    # What is the percentage of people who have a Bachelor's degree?
    
    percentage_bachelors = round((((((df[['education','fnlwgt']]).groupby('education')['fnlwgt'].sum().reset_index()).set_index('education'))['fnlwgt'])['Bachelors']*100)/df['fnlwgt'].sum(), 1)
                                 
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    higher_education = (df[((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'))])[['education','fnlwgt','salary']]
    lower_education = (df[~((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'))])[['education','fnlwgt','salary']]
    
    # percentage with salary >50K
    
    higher_education_rich = round(((higher_education[(higher_education['salary']=='>50K')]['fnlwgt']).sum()*100)/higher_education['fnlwgt'].sum(), 1)
    lower_education_rich = round(((lower_education[(lower_education['salary']=='>50K')]['fnlwgt']).sum()*100)/lower_education['fnlwgt'].sum(), 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df[((df['hours-per-week']==1) & (df['salary']=='>50K'))])['fnlwgt'].sum()
    
    rich_percentage = (num_min_workers*100)/(df[df['hours-per-week']==1])['fnlwgt'].sum()

    # What country has the highest percentage of people that earn >50K?
    country_list=(((df[(df['salary']=='>50K')])[['native-country','fnlwgt']]).groupby('native-country')['fnlwgt'].sum().reset_index()).set_index('native-country')
    country_list1=((df[['native-country','fnlwgt']]).groupby('native-country')['fnlwgt'].sum().reset_index()).set_index('native-country')
    country_list1.columns = ['fnlwgt_total']
    country_list['fnlwgt_total']=(country_list1)
    country_list['percentage_>50k']=(country_list['fnlwgt']*100)/country_list['fnlwgt_total']
    country_list=country_list.reset_index()
    
    highest_earning_country = country_list[country_list['percentage_>50k']==(country_list['percentage_>50k'].max())]['native-country'].reset_index()['native-country'][0]
    
    highest_earning_country_percentage = round(country_list[country_list['percentage_>50k']==(country_list['percentage_>50k'].max())]['percentage_>50k'].reset_index()['percentage_>50k'][0], 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    occupation_list =((df[((df['native-country']=='India') & (df['salary']=='>50K'))])[['occupation','fnlwgt']]).groupby('occupation')['fnlwgt'].sum().reset_index()
    top_IN_occupation = ((((occupation_list[(occupation_list['fnlwgt']==occupation_list['fnlwgt'].max())])['occupation']).reset_index())['occupation'])[0]
    
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# In[15]:


calculate_demographic_data()


# In[ ]:




