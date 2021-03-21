# Using Python and API to plot the location of ISS.
import pandas as pd
import plotly.express as px

# this the url that we want pandas to read.
url = 'http://api.open-notify.org/iss-now.json'
data_frame = pd.read_json(url)
# adding 'latitude' and 'longitude' columns
data_frame['latitude'] = data_frame.loc['latitude', 'iss_position']
data_frame['longitude'] = data_frame.loc['longitude', 'iss_position']
# resetting the index
data_frame.reset_index(inplace = True)
# drop the 'index' and 'message' columns
data_frame = data_frame.drop(['index', 'message'], axis = 1)

figure = px.scatter_geo(data_frame, lat = 'latitude', lon = 'longitude')
figure.show()