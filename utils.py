import random

def colorful():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def color_128():
    colors = []
    while len(colors) < 128:
        new = colorful()
        if new not in colors:
            colors.append(new)
    return colors