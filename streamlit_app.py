import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns
from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

# Function to load data from BigQuery
def load_data():
    query = """
        SELECT * FROM `sound-repeater-452503-t2.DM_HW1_Cloud_Data_Mining.Trial`
    """
    df = client.query(query).to_dataframe()
    df['latitude'].fillna(value=df['latitude'].mean(), inplace=True)
    df['longitude'].fillna(value=df['longitude'].mean(), inplace=True)
    return df

# Streamlit user interface
st.title('Streamlit Fire Incidents Dashboard')
df = load_data()

if df.empty:
    st.write("No data available to display.")
else:
    # Display the DataFrame in the app
    st.write(df)  

    st.header("Incident Frequency by Month")
    monthly_incidents = df['Date_Time_Of_Event'].dt.month.value_counts().sort_index()
    fig, ax = plt.subplots()
    monthly_incidents.plot(kind='line', marker='o', ax=ax)
    ax.set_title('Incident Frequency by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Incidents')
    st.pyplot(fig)

    def create_map(df):
        m = folium.Map(location=[37.3382, -121.8863], zoom_start=12, tiles='OpenStreetMap')
        for idx, row in df.iterrows():
            if pd.notna(row['latitude']) and pd.notna(row['longitude']):  # Checking for NaN values
                folium.CircleMarker(
                    location=[row['latitude'], row['longitude']],
                    radius=5,
                    color='blue',
                    fill=True,
                    fill_color='blue',
                    fill_opacity=0.7,
                    popup=row['Final_Incident_Type']
                ).add_to(m)
        return m

    st.header("Map of Incidents")
    map_fig = create_map(df)
    folium_static(map_fig)

    st.header('Frequency of Incident Categories')
    if 'Final_Incident_Category' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, x='Final_Incident_Category', order=df['Final_Incident_Category'].value_counts().index)
        plt.title('Frequency of Incident Categories')
        plt.xticks(rotation=45)

        # Show plot in Streamlit
        st.pyplot(plt.gcf())
    else:
        st.error("Column 'Final_Incident_Category' does not exist in the Excel file. Please check the column names.")

    st.header("Heatmap of Incident Priority vs. Time of Day")
    pivot_table = df.pivot_table(values='Incident_No', index='Hour', columns='Priority', aggfunc='count', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='d')
    plt.title('Heatmap of Incident Priority vs. Time of Day')
    st.pyplot(plt.gcf())

    selected_month = st.selectbox('Select Month', df['Date_Time_Of_Event'].dt.month.unique())
    filtered_data = df[df['Date_Time_Of_Event'].dt.month == selected_month]

    incident_types = df['Final_Incident_Type'].unique().tolist()
    selected_types = st.multiselect('Select Incident Types', options=incident_types, default=incident_types)

    filtered_df = df[df['Final_Incident_Type'].isin(selected_types)]
