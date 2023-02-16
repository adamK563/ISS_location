import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components

API_URL = "http://api.open-notify.org/iss-now.json"

# Function to get the spacecraft location from the API
def get_spacecraft_location():
    # Make the API request
    response = requests.get(API_URL)
    # Parse the response and return the spacecraft location as a DataFrame
    location = response.json()["iss_position"]
    location_df = pd.DataFrame({"latitude": [float(location["latitude"])], "longitude": [float(location["longitude"])]})
    return location_df

def refresh():
    """Function to refresh the Streamlit script."""
    components.html("<script>location.reload();</script>")

# Streamlit app
def app():
    st.title("Spacecraft Trajectory Visualization")

    # Get the spacecraft location from the API
    location = get_spacecraft_location()
           
    # Display the spacecraft location on a map using streamlit-leaflet
    if not location.empty:
        st.map(location ,zoom=3)
    
    if st.button("Update"):
        refresh()
      

if __name__ == '__main__':
    app()