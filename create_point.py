import math

## d_raw = distance between sensor and shape IN 
## d = distnace between sensor and shape IN INCHES
## theta = angle of top servo
## phi = angle of bottom servo

def d_inches(d_raw):
    '''
    Converts the output voltage from sensor into a distance in inches
    
    '''
    d = 51.422*math.exp(-0.004*d_raw) #converison equation from calibration data
    print(d)

def create_point(d, theta, phi):
    if d >= 24:
        z = d * math.sin(theta)
        g = d * math.cos(theta)
        x = g * math.sin(phi)
        y = g * math.sin(phi)
        print(x, y, z)
