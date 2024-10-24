import pandas as pd
import matplotlib.pyplot as plt

# give the paths of the dataset
df = pd.read_excel('E:/final pro data/weatherDataSet.xlsx')

# First query :  Average Temperature per State
avg_temp_state = df.groupby('State')['Temperature (°C)'].mean()
#print the value in the console
print("Average Temperature per State:\n", avg_temp_state)

# Plot average temperature per state
avg_temp_state.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Average Temperature per State in 2000')
plt.xlabel('State')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Second Query :  Correlation between Temperature and Humidity
corr = df[['Temperature (°C)', 'Humidity (%)']].corr()
#print the value in the console
print("\nCorrelation between Temperature and Humidity:\n", corr)

# Third Qurey:  Plot Temperature vs Humidity for a specific state 
west_bengal_data = df[df['State'] == 'West Bengal'] #here i am using westbengal data

plt.figure(figsize=(10, 6))
plt.scatter(west_bengal_data['Temperature (°C)'], west_bengal_data['Humidity (%)'], color='green')
plt.title('Temperature vs Humidity in West Bengal (2000)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()

# Fourth Query :  Highest recorded rainfall day in each state
max_rainfall = df.loc[df.groupby('State')['Rainfall (mm)'].idxmax()]
#print the value in the console
print("\nHighest Recorded Rainfall Day per State:\n", max_rainfall[['State', 'Date', 'Rainfall (mm)']])

# Fifth Query:  Maximum Wind Speed per State
max_wind_speed = df.loc[df.groupby('State')['Wind Speed (km/h)'].idxmax()]
#print the value in the console
print("\nDay with Maximum Wind Speed per State:\n", max_wind_speed[['State', 'Date', 'Wind Speed (km/h)']])

# 6. Temperature Distribution Plot
plt.figure(figsize=(10, 6))
plt.hist(df['Temperature (°C)'], bins=30, color='orange', edgecolor='black')
plt.title('Temperature Distribution in All States (2000)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Seventh Query:  Top 5 Rainiest Days in India
top_rainfall_days = df.nlargest(5, 'Rainfall (mm)')[['Date', 'State', 'Rainfall (mm)']]
#print the value in the console
print("\nTop 5 Rainiest Days in India:\n", top_rainfall_days)

# Eight Query:  Average Humidity per Month
df['Month'] = df['Date'].dt.month
avg_humidity_month = df.groupby('Month')['Humidity (%)'].mean()
#print the value in the console
print("\nAverage Humidity per Month:\n", avg_humidity_month)

# Plot average humidity per month
avg_humidity_month.plot(kind='line', marker='o', figsize=(10, 6), color='blue')
plt.title('Average Humidity per Month (2000)')
plt.xlabel('Month')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()

# Data Validation & Error Detection

# Nineth Query:  Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values in Dataset:\n", missing_values)

# Tenth Query:  Check for temperature outliers (outside -10 to 50°C)
invalid_temp = df[(df['Temperature (°C)'] < -10) | (df['Temperature (°C)'] > 50)]
#print the value in the console
print("\nInvalid Temperature Entries:\n", invalid_temp)

# Eleventh Query:  Check for humidity outliers (outside 0-100%)
invalid_humidity = df[(df['Humidity (%)'] < 0) | (df['Humidity (%)'] > 100)]
print("\nInvalid Humidity Entries:\n", invalid_humidity)
