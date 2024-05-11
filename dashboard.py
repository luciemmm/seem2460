import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = '/Users/moemmyat/Documents/GitHub/seem2460/housing.csv'
df=pd.read_csv(url)

# Set up sidebar for user inputs
st.sidebar.header('User Input Features')
# Option to select what to visualize
option = st.sidebar.selectbox(
    'What do you want to visualize?',
    ('Median House Value', 'Median House Age')
)

min_latitude = st.sidebar.number_input('Minimum Latitude', float(df['latitude'].min()), float(df['latitude'].max()), float(df['latitude'].min()))
max_latitude = st.sidebar.number_input('Maximum Latitude', float(df['latitude'].min()), float(df['latitude'].max()), float(df['latitude'].max()))
min_longitude = st.sidebar.number_input('Minimum Longitude', float(df['longitude'].min()), float(df['longitude'].max()), float(df['longitude'].min()))
max_longitude = st.sidebar.number_input('Maximum Longitude', float(df['longitude'].min()), float(df['longitude'].max()), float(df['longitude'].max()))

if option == 'Median House Value':
    min_value = st.sidebar.number_input('Minimum Median House Value', float(df['median_house_value'].min()), float(df['median_house_value'].max()), float(df['median_house_value'].min()))
    max_value = st.sidebar.number_input('Maximum Median House Value', float(df['median_house_value'].min()), float(df['median_house_value'].max()), float(df['median_house_value'].max()))
    value_column = 'median_house_value'
    label = 'Median House Value'
else:
    min_value = st.sidebar.number_input('Minimum Median House Age', float(df['housing_median_age'].min()), float(df['housing_median_age'].max()), float(df['housing_median_age'].min()))
    max_value = st.sidebar.number_input('Maximum Median House Age', float(df['housing_median_age'].min()), float(df['housing_median_age'].max()), float(df['housing_median_age'].max()))
    value_column = 'housing_median_age'
    label = 'Median House Age'

# Filtering data
df_filtered = df[(df['latitude'] >= min_latitude) & (df['latitude'] <= max_latitude) & 
                 (df['longitude'] >= min_longitude) & (df['longitude'] <= max_longitude) &
                 (df[value_column] >= min_value) & (df[value_column] <= max_value)]

# Visualization
st.write(f"## California Housing {label} Visualization")
fig, ax = plt.subplots(figsize=(10,7))
scatter = ax.scatter(df_filtered['longitude'], df_filtered['latitude'], alpha=0.4, 
                     s=df_filtered['population']/100, label='Population', 
                     c=df_filtered[value_column], cmap='jet')
plt.colorbar(scatter, ax=ax, label=label)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
st.pyplot(fig)
