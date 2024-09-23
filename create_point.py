import math

## d_raw = distance between sensor and shape IN 
## d = distnace between sensor and shape IN INCHES
## theta = angle of top servo
## phi = angle of bottom servo

def d_inches(d_raw):
    '''
    Converts the output voltage from sensor into a distance in inches 
    '''
    d = 50.1153*math.exp(-0.0038*d_raw) #converison equation from calibration data
    return d

def create_point(d, theta_deg, phi_deg):
    '''
    If sensor data is reading less that 18 inches, converts angle in degrees and
    distance in inches into a point with x, y, and z values
    '''
    if d <= 18:
        theta = math.radians(theta_deg)
        phi = math.radians(phi_deg)
        z = -1 * d * math.cos(theta)
        g = d * math.sin(theta)
        x = -1 * g * math.cos(phi)
        y = g * math.sin(phi)
        return (x, y, z)
    else:
        return (0, 0, 0)
