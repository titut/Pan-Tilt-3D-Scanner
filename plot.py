import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash

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
        interval=500,  # in milliseconds
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
    fig = px.scatter_3d(new_data, x='x', y='y', z='z', color="point_type", title='Cool Plot')
    camera = dict(eye=dict(x=2,y=2,z=0.5))
    fig.update_layout(scene_camera=camera)
    
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)