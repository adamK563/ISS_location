# ISS_location - Spacecraft Trajectory Visualization

This is a Streamlit app that visualizes the real-time location and velocity of the International Space Station (ISS) on a map, with an arrow that displays the direction and speed of its movement. The app uses data from an API and the `streamlit-leaflet` library to display the spacecraft location on a map.

## Usage

To use this app, you will need to install `Docker` on your machine. Once you have installed Docker, you can run the app using the following commands:

Build the Docker image:
```
docker build -t spacecraft-app .
```
Run the Docker container
```
docker run -p 8501:8501 spacecraft-app
```

After running these commands, you can open your web browser and navigate to `http://localhost:8501` to use the app.

## Requirements

The following packages are required to run this app:

- `streamlit`
- `pandas`
- `streamlit-leaflet`
- `requests`

They are included in the coker file if you want to install them localy you can install these packages by running the following command:
```
pip install -r requirements.txt
```

## Author

This app was created by [LinkedIn Profile: Adam Karpovich](https://www.linkedin.com/in/adam-karpovich-26038a206/)
. 