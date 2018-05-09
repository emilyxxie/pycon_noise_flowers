TOTAL_DEGREES = 360
radius = 0

def setup():
    global displayWidth, displayHeight, radius
    size(displayWidth / 2, displayHeight)
    background(0)
    noFill()
    stroke(255, 25)
    radius = height / 2

def draw():
    center_x = width / 2
    center_y = height / 2

    global TOTAL_DEGREES, radius


    beginShape()
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i * 0.02, float(frameCount) / 150)
        x = center_x + radius * cos(radians(i)) * noiseFactor
        y = center_y + radius * sin(radians(i)) * noiseFactor
        curveVertex(x, y)
    endShape(CLOSE)

    radius -= 1

    if radius == 0:
        noLoop()
