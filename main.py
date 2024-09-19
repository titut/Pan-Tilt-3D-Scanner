import serial
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash

arduinoPort = "COM4"
baudRate = 9600

serialPort = serial.Serial(arduinoPort, baudRate, timeout=1)

# Load initial data from Excel file
csv_file = 'data.csv'
df = pd.read_csv(csv_file)

# Create a Dash web application
app = Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    dcc.Graph(id='real-time-plot'),
    dcc.Interval(
        id='interval-component',
        interval=4*1000,  # in milliseconds
        n_intervals=0
    )
])

# Define callback to update the plot in real-time
@app.callback(Output('real-time-plot', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_graph(n_intervals):
    # Load new data from Excel file
    new_data = pd.read_csv(csv_file)
    
    # Update the plot
    fig = px.scatter_3d(new_data, x='x', y='y', z='z', title='Cool Plot')
    fig.update_scenes(xaxis_autorange="reversed")
    
    return fig

app.run_server(debug=True)

while True:

    data = serialPort.readline().decode()

    if len(data) > 0:
        print(data)