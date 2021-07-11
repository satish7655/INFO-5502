import pandas as pd
import numpy as np

# 1
df = pd.read_excel('indicator hiv estimated prevalence% 15-49.xlsx')
print(df.head())

Asia = ['Myanmar', 'North Korea', 'Chinese Taipei', 'North Yemen (former)', 'Lao', 'Hong Kong, China',
        'Kyrgyz Republic', 'Macao, China', 'Maldives', 'Montserrat', 'Timor-Leste',
        'Western Sahara', 'Western Sahara', 'South Yemen (former)', 'South Yemen (former)',
        'Afghanistan', 'Christmas Island', 'Armenia', 'Cocos Island', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan',
        'Brunei', 'Burma', 'Cambodia', 'China', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran',
        'Iraq', 'Israel', 'Japan',
        'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Nepal', 'North',
        'Korea', 'Oman', 'Pakistan', 'Papua New Guinea', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore',
        'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan',
        'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
Africa = ['Eritrea and Ethiopia', 'Guinea-Bissau', 'Congo, Rep.', 'Lesotho', 'Mayotte', 'Sao Tome and Principe',
          'Senegal', 'Somaliland', 'Swaziland',
          'Algeria', 'Congo, Dem. Rep.', 'Central African Republic', 'Burkina Faso', 'Angola', 'Benin', 'Botswana',
          'Cape Verde', 'Gibraltar', 'Burkina', 'Faso', 'Burundi', 'Cameroon', 'Cabo', 'Verde', 'Chad',
          'Comoros', 'Congo', 'the Democratic Republic of Congo', 'Cote d’Ivoire', 'Djibouti', 'Equatorial Guinea',
          'Egypt', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau.', 'Kenya',
          'the Kingdom of Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
          'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Saharawi Arab Democratic Republic',
          'Republic', 'Sao Tome and Principe Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa',
          'South Sudan', 'Sudan', 'Kingdom of Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
Europe = ['Falkland Is (Malvinas)', 'Saint Eustatius', 'Norfolk Island', 'Northern Cyprus', 'Czech Republic',
          'Holy See', 'Isle of Man', 'Jersey', 'Kosovo', 'Liechtenstein', 'Macedonia, FYR',
          'Moldova', 'Netherlands Antilles', 'Reunion', 'Serbia and Montenegro', 'Serbia excluding Kosovo',
          'Slovak Republic',
          'South Ossetia', 'Svalbard', 'Transnistria', 'United Kingdom', 'USSR', 'West Bank and Gaza', 'West Germany',
          'Yugoslavia', 'Åland', 'Sark', 'Saba', 'Czechoslovakia', 'East Germany', 'Faeroe Islands',
          'Gibraltar,''Guernsey',
          'Albania', 'Channel Islands', 'Abkhazia', 'Andorra', 'Akrotiri and Dhekelia', 'Armenia', 'Austria',
          'Azerbaijan', 'Belarus', 'Belgium',
          'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland',
          'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Uzbekistan',
          'Kazakhstan', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Monaco', 'Montenegro',
          'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Republic Moldova', 'Romania',
          'Russian Federation', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
          'Tajikistan', 'Turkey', 'Turkmenistan', 'Ukraine', 'United Kingdom of Great Britain', 'England',
          'Northern Ireland']
North_America = ['Guernsey', 'Puerto Rico', 'Samoa', 'United States', 'Martinique', 'Dominica', 'American Samoa',
                 'Dominican Republic', 'Guadeloupe', 'Guam', 'St. Barthélemy', 'St. Helena', 'St. Kitts and Nevis',
                 'St. Lucia', 'Turks and Caicos Islands', 'St. Martin', 'St. Vincent and the Grenadines',
                 'St.-Pierre-et-Miquelon', 'United States', 'Virgin Islands (U.S.)', 'Sint Maarten (Dutch part)',
                 'St. Martin (French part)', 'Virgin Islands, British', 'Hawaiian Trade Zone', 'Antigua and Barbuda',
                 'Cayman Islands', 'British Virgin Islands', 'Bermuda', 'Anguilla', 'Bahamas', 'Barbados', 'Belize',
                 'Canada', 'Costa Rica', 'Cuba', 'Dominica Dominican', 'Republic El Salvador', 'Grenada', 'Guatemala',
                 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Saint Kitts and Nevis', 'Panama',
                 'Saint Lucia', 'Saint Vincent Grenadines', 'Trinidad and Tobago', 'United States of America, USA']
South_America = ['El Salvador', 'French Guiana', 'Curaçao', 'Wake Island', 'Bonaire',
                 'Argentina', 'Aruba', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Falkland', 'Islands',
                 '(United',
                 'Kingdom)', 'French', 'Guiana', '(France)', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay',
                 'Venezuela']
Oceania = ['French Polynesia', 'Coastline', 'Northern Mariana Islands', 'Marshall Islands', 'Micronesia, Fed. Sts.',
           'New Caledonia', 'Ngorno-Karabakh',
           'Pitcairn', 'Solomon Islands', 'Tokelau', 'Wallis et Futuna', 'U.S. Pacific Islands',
           'Australia', 'Micronesia', 'Fiji', 'Kiribati', 'Marshall', 'Islands', 'Nauru', 'New Zealand', 'Palau',
           'Papua', 'New', 'Guinea', 'american samoa', 'Solomon', 'Islands', 'Tonga', 'Tuvalu', 'Vanuatu']
Antarctica = ['Antarctica']


def country_to_continent(check):
    for i in Asia:
        if i == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'Asia'
    for j in Africa:
        if j == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'Africa'
    for k in Europe:
        if k == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'Europe'
    for l in North_America:
        if l == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'North_America'
    for m in South_America:
        if m == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'South_America'
    for o in Oceania:
        if o == check['Estimated HIV Prevalence% - (Ages 15-49)']:
            return 'Oceania'
    for p in Antarctica:
        return 'Antarctica'


df['continent'] = df.apply(country_to_continent, axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df.head())
df.to_excel('Updated_indicator hiv estimated prevalence% 15-49.xlsx')

# 2
df1 = df
df1['Average'] = df1.iloc[:, 23:35].mean(axis=1)
df1[['continent', 'Estimated HIV Prevalence% - (Ages 15-49)', 'Average']]
print("\nDisplaying country in the given continent with the HIGHeST average HIV estimated prevalence of people ages "
      "from 15to 49 of from year 2000 to 2011")
print(df1.groupby('continent')['Estimated HIV Prevalence% - (Ages 15-49)'].max())

print("\nDisplaying country in the given continent with the LOWEST average HIV estimated prevalence of people ages "
      "from 15to 49 of from year 2000 to 2011")
print(df1.groupby('continent')['Estimated HIV Prevalence% - (Ages 15-49)'].min())

df1.iloc[df1['Average'].idxmax()][['Estimated HIV Prevalence% - (Ages 15-49)', 'continent', 'Average']]
df1.iloc[df1['Average'].idxmax()][['Estimated HIV Prevalence% - (Ages 15-49)', 'continent', 'Average']]

import matplotlib.pyplot as pt

# for the highest Average based on each continent
max = df1.loc[df1.groupby(['continent'])['Average'].idxmax()]
pt.figure(figsize=(13, 13))
pt.bar(max['continent'], max['Average'], color='b')
pt.title("Highest average HIV estimated prevalence of people ages from 15 to 49 of from year 2000 to 2011 in each "
         "continent", fontsize=14)
pt.xlabel("Continent Names", fontsize=15, color='b')
pt.ylabel("Highest average HIV estimated prevalence", fontsize=18, color='b')
pt.show()

# for the lowest Average based on each continent
min = df1.loc[df1.groupby(['continent'])['Average'].idxmin()]
pt.figure(figsize=(13, 13))
pt.bar(min['continent'], min['Average'], color='b')
pt.title("Lowest average HIV estimated prevalence of people ages from 15 to 49 of from year 2000 to 2011 in each "
         "continent", fontsize=14)
pt.xlabel("Continent Names", fontsize=15, color='b')
pt.ylabel("Highest average HIV estimated prevalence", fontsize=18, color='b')
pt.show()

# 3.
df1 = df1.fillna(0)  # replace nan values with zero's in a column
cols = [i for i in range(1979, 2012)]

# returning the copy of the object with the operation performed
df1.rename(columns={'2008': 2008, '2009': 2009, '2010': 2010, '2011': 2011}, inplace=True)

# calculate the average based on the continent for a given range of years
average_df = df1.groupby('continent')[cols].agg('mean')

average_df.plot(legend=True)
average_df.T.plot(kind='line', legend=True)
pt.title("Overlaid line chart")
pt.xlabel("Continents", fontsize=14, color='r')
pt.ylabel("HIV estimated prevalence in diff years", fontsize=14, color='r')
pt.legend()
pt.show()

# 4. Scatter plot
# Scatter plot to show HIV estimated prevalence in the Year 1990 for different continent
df1_1990 = df1.groupby('continent')[[1990]].agg('mean')
pt.figure(figsize=(13, 13))
pt.scatter(average_df[[1990]], df1_1990[[1990]],
           color=['red', 'yellow', 'green', 'black', 'lime', 'orange', 'purple'])
pt.title("HIV estimated prevalence in the year 1990 for different continent")
pt.xlabel("Average HIV prevalence for each continent", fontsize=14, color='r')
pt.ylabel("Year 1990", fontsize=14, color='r')
pt.show()

# Scatter plot to show HIV estimated prevalence in the Year 2010 for different continent
df1_2010 = df1.groupby('continent')[[2010]].agg('mean')
pt.figure(figsize=(13, 13))
pt.scatter(average_df[[2010]], df1_2010[[2010]],
           color=['red', 'yellow', 'green', 'black', 'lime', 'orange', 'purple'])
pt.title("HIV estimated prevalence in the year 2010 for different continent")
pt.xlabel("Average HIV prevalence for each continent", fontsize=14, color='r')
pt.ylabel("Year2010", fontsize=14, color='r')
pt.show()

#5.Write a report to explain how each question is implemented and its output graphs (2 point).

'''In an attempt to solve problem number one, I made a list for each continent and added the corresponding countries 
to the list, then wrote a function that used a for loop to return a matching continent from the list of countries 
provided in the excel sheet. Finally, add a new column and apply the function to the data frame before saving the 
updated excel file. 


To finish problem number 2, I used the panda's library and the inbuilt method iloc to get rows/columns with specific 
labels for the selected columns 23,35. (for years 2000,2011 as per the index value provided in the excel sheet). 
Then, to find countries in each continent, I used a max and min function to return the required lowest and highest 
averages. In addition, as required by the assignment, I used the idxmax() function to obtain the row label of the 
maximum value. Finally, for visualization purposes, Matplotlib was imported and a bar chart and overlaid bar chart 
were created to show the highest and lowest average HIV estimated prevalence of people in each continent for the 
selected year. 

In order to complete problem number 3, I followed the same procedure as in problem number two, using Matplotlib to 
create a line chart and an overlaid line chart. However, in the panda's data frame, I first removed all the nan 
values with zeros and calculated the average using an aggregation function based on the continent for a given range 
of years. 

The same previously used libraries were implemented to complete problem number four. I created a new data frame for 
both the years 1990 and 2010 and used the continent-based aggregation function for the selected year. I simply 
plotted the scatter plot diagram to show HIV estimated prevalence in the chosen year after calculating the average 
HIV estimated prevalence in each continent. As required, different color patterns were used to show the data from 
different continents. 


'''