import serial
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash
import random

arduinoPort = "COM4"
baudRate = 9600

d = {
    "x": [1],
    "y": [1],
    "z": [1]
}

serialPort = serial.Serial(arduinoPort, baudRate, timeout=1)

while True:

    data = serialPort.readline().decode()

    if len(data) > 0:
        data = [int(x) for x in data.split(",")]
        d["x"].append(data[0])
        d["y"].append(data[1])
        d["z"].append(data[2])
        df = pd.DataFrame(data=d)
        df.to_csv("data.csv")