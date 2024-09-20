import serial
import pandas as pd
from create_point import d_inches, create_point

arduinoPort = "COM4"
baudRate = 9600

d = {
    "x": [0],
    "y": [0],
    "z": [0],
    "point_type": ["camera"]
}

serialPort = serial.Serial(arduinoPort, baudRate, timeout=1)

while True:

    data = serialPort.readline().decode()

    if len(data) > 0:
        data = data.split(",")
        angle_1 = float(data[0])
        angle_2 = float(data[1])
        distance = d_inches(float(data[2]))
        xyz = create_point(distance, angle_1, angle_2)
        if(xyz != (0, 0, 0)):
            d["x"].append(xyz[0]) # change this to x, y, and z when we calculate for them
            d["y"].append(xyz[1])
            d["z"].append(xyz[2])
            d["point_type"].append("reading")

            df = pd.DataFrame(data=d)
            df.to_csv("data.csv")