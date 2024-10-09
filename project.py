import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This CSV file contains semicolons instead of comas as separator
data_frame=pd.read_csv('assets/real_estate.csv', sep=';')
df=pd.DataFrame(data_frame)

prices=df["price"]
prices=prices.dropna()
labels=pd.Series(df.columns)
##print(labels)

max_price=prices.max()
min_price=prices.min()

most_expensive=df.loc[df["price"]==max_price]
cheapest=df.loc[df["price"]==min_price]

#Exercise 01
e_address=most_expensive.iloc[0,12]
print("The house with address",str(e_address),"is the most expensive and its price is",str(max_price),"USD")

#Exercise 02
c_address=cheapest.iloc[0,12]
print("The house with address",str(c_address),"is the cheapest and its price is",str(min_price),"USD")

#for i in range(0,len(cheapest)):
#    addresses=cheapest.iloc[i,12]
#    cprice=cheapest.iloc[i,9]
#    print("The house with address",str(addresses),"is the cheapest and its price is",str(cprice),"USD")

#Exercise 03

area=df["surface"]
area = area.dropna()

max_area=area.max()
min_area=area.min()

biggest=df.loc[df["surface"]==max_area]
smallest=df.loc[df["surface"]==min_area]

address_b_h=biggest.iloc[0,12]
address_s_h=smallest.iloc[0,12]

print("The biggest house is located on",str(address_b_h),"and its surface is",str(max_area),"meters")
print("The smallest house is located on",str(address_s_h),"and its surface is",str(min_area),"meters")

#Exercise 04

population_list=df['level5'].unique()
sorted_population_list = sorted(list(population_list))
comma_separated_string = ','.join(sorted_population_list)
print(comma_separated_string)

#Exercise 05
#The isna() method returns a DataFrame object where all the values are replaced with a Boolean value True for NA (not-a -number) values, and otherwise False.
newdf = df.isna()
print(newdf)

#Exercise 06

dfad=df.dropna(axis='columns')

rows, columns = df.shape
print(f"The dimensions of the original DataFrame are: Number of rows= {rows}, Number of columns= {columns}")

rows_ad, columns_ad = dfad.shape
print(f"The dimensions of the DataFrame after deletions are: Number of rows= {rows_ad}, Number of columns= {columns_ad}")

#Exercise 07

arroyomolinos_data=df[df['level5'] == "Arroyomolinos (Madrid)"]
mean_price=arroyomolinos_data['price'].mean()
print("The mean of prices in the population (level5 column) of Arroyomolinos (Madrid) is",str(mean_price))

#Exercise 08

plt.hist(arroyomolinos_data['price'], bins=20, edgecolor='red')
plt.title('Histogram of Prices in Arroyomolinos (Madrid)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

#Exercise 09

data_v = df[df['level5'] == "Valdemorillo"]
data_v=data_v.dropna()

data_g = df[df['level5'] == "Galapagar"]
data_g=data_g.dropna()

mean_price_v=data_v['price'].mean()
mean_price_g=data_g['price'].mean()

print(f"Conclusion: The average price of Valdemorillo is {mean_price_v} and the average price of Galapagar is {mean_price_g}")

#Exercise 10

df['pps'] = df['price'] / df['surface']

avg_price_valdemorillo = df[df['level5'] == 'Valdemorillo']['pps'].mean()
avg_price_galapagar = df[df['level5'] == 'Galapagar']['pps'].mean()

print(f"The average price per square meter for Valdemorillo is {avg_price_valdemorillo} and the average price per square meter for Galapagar is {avg_price_galapagar}")

#Exercise 11

plt.figure(figsize=(10, 6))
plt.scatter(df['surface'], df['price'])
plt.xlabel('Surface (m2)')
plt.ylabel('Price')
plt.title('Relation between surface and price of houses')
plt.grid(True)

plt.show()

#### Exercise 12. How many real estate agencies does the dataset contain? 

real_state_name=df["realEstate_name"].nunique()
print(f"There are {real_state_name} real state agencies contained in the dataset")

#### Exercise 13. Which is the population (level5 column) that contains the most houses? 

population_counts = df['level5'].value_counts()

most_houses_population = population_counts.idxmax() 
number_of_houses_in_population = population_counts.max() 

print(f"Population with the most houses: {most_houses_population}") 
print(f"Number of houses in this population: {number_of_houses_in_population}") 

#### Exercise 14. Now let's work with the "south belt" of Madrid. Make a subset of the original DataFrame that contains the following populations (level5 column): "Fuenlabrada", "Leganés", "Getafe", "Alcorcón" (★★☆)
#Hint: Filter the original DataFrame using the column level5 and the function isin

south_belt = df[df['level5'].isin(["Fuenlabrada","Leganés","Getafe","Alcorcón"])]
print(south_belt)

#### Exercise 15. Make a bar plot of the median of the prices and explain what you observe (you must use the subset obtained in Exercise 14) (★★★)

#Print the bar of the median of the prices and write in the Markdown cell a brief analysis about the plot.

median_prices = south_belt.groupby('level5')['price'].median() 

plt.bar(x=median_prices.index, height=median_prices.values) 

plt.xlabel('City') 
plt.ylabel('Median Price') 
plt.title('Median Prices in South Belt Cities') 

plt.show()

#### Exercise 16. Calculate the sample mean and variance of the variables: price, rooms, surface area and bathrooms (you must use the subset obtained in Exercise 14) (★★★)
#Print both values for each variable.

mean_price = south_belt['price'].mean()
mean_rooms = south_belt['rooms'].mean()
mean_surface = south_belt['surface'].mean()
mean_bathrooms = south_belt['bathrooms'].mean()

variance_price = south_belt['price'].var()
variance_rooms = south_belt['rooms'].var()
variance_surface = south_belt['surface'].var()
variance_bathrooms = south_belt['bathrooms'].var()

print("Sample Mean (South Belt):")
print(f"Price: {mean_price}")
print(f"Rooms: {mean_rooms}")
print(f"Surface Area: {mean_surface}")
print(f"Bathrooms: {mean_bathrooms}")
print("\nSample Variance (South Belt):")
print(f"Price: {variance_price}")
print(f"Rooms: {variance_rooms}")
print(f"Surface Area: {variance_surface}")
print(f"Bathrooms: {variance_bathrooms}")