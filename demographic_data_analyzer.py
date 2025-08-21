import pandas as pd




def calculate_demographic_data(print_data=True):
   # Read data from file
   df = pd.read_csv('adult.data.csv')
 
   #print(df.info())
  # print(df.head())
 
   # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
   race_count = df['race']
   race_count = race_count.value_counts()


   # What is the average age of men?
   male = df[df['sex'] == 'Male']
   male_df = male[['sex','age']]
 
   average_age_men = male_df['age'].mean().round(1)


   # What is the percentage of people who have a Bachelor's degree?
 
   education = df['education']
   total_education = len(education)
   bachelor = education.value_counts()['Bachelors']
  
   percentage_bachelors = round(bachelor / total_education * 100,1)


   # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
   # What percentage of people without advanced education make more than 50K?


   # with and without `Bachelors`, `Masters`, or `Doctorate`
   higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
   higher_education_total = len(higher_education)
  
   lower_education = df.drop(higher_education.index)
   lower_education_total = len(lower_education)


   higher_education_with_50 = len(higher_education[higher_education['salary'] == '>50K'])
  
   higher_education_rich = round(higher_education_with_50 / higher_education_total * 100,1)
  
   lower_education_with_50 = len(lower_education[lower_education['salary'] == '>50K'])
  
   lower_education_rich = round(lower_education_with_50 / lower_education_total * 100,1)




   # What is the minimum number of hours a person works per week (hours-per-week feature)?
 
   work_hours = df.sort_values('hours-per-week',ascending=True)
  
   min_work_hours = work_hours['hours-per-week'].min()


   # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  
   num_min_workers = work_hours[work_hours['hours-per-week'] == min_work_hours]
   num_min_workers_count = len(num_min_workers)
  
   rich_min_work = num_min_workers[num_min_workers['salary'] == '>50K']
   rich_min_work_count = len(rich_min_work)




   rich_percentage = round(rich_min_work_count / num_min_workers_count * 100,1)


   # What country has the highest percentage of people that earn >50K?
   # Calcular percentual para cada país
   country_counts = df['native-country'].value_counts()
   country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
  
   # Calcular percentual de ricos por país
   country_percentages = (country_rich_counts / country_counts * 100).fillna(0)
  
   highest_earning_country = country_percentages.idxmax()
   highest_earning_country_percentage = round(country_percentages.max(),1)


   # Identify the most popular occupation for those who earn >50K in India.
  
   india = df[df['native-country'] == 'India']
   india_filtered = india[['salary','occupation']]


   india_50 = india_filtered[india_filtered['salary'] == '>50K']
   india_occupation_count = india_50['occupation'].value_counts()


   top_IN_occupation = india_occupation_count.idxmax()


   # DO NOT MODIFY BELOW THIS LINE


   if print_data:
       print("Number of each race:\n", race_count)
       print("Average age of men:", average_age_men)
       print(f"Percentage with Bachelors degrees: {percentage_bachelors:.1f}%")
       print(f"Percentage with higher education that earn >50K: {higher_education_rich:.1f}%")
       print(f"Percentage without higher education that earn >50K: {lower_education_rich:.1f}%")
       print(f"Min work time: {min_work_hours} hours/week")
       print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
       print("Country with highest percentage of rich:", highest_earning_country)
       print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.2f}%")
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





