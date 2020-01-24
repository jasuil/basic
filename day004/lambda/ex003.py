# matplot

import matplotlib.pyplot as plt

def shape(shape):
    color = 'green'

    def drawCircle(radius):
        plt.gca().add_patch(plt.Circle((0, 0), radius=radius, fc=color))
        plt.axis("scaled")
        plt.show()

    def drawRec(width, height):
        plt.gca().add_patch(plt.Rectangle((10, 10), width=width, height=height, fc=color))
        plt.axis("scaled")
        plt.show()

    if shape == 'circle':
        return drawCircle
    elif shape == 'rect':
        return drawRec
    else:
        print("invalid parameter")


circle = shape("circle")
rect = shape("rect")

circle(10)
rect(20, 100)