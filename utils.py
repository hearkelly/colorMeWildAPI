import random

from wonderwords import RandomWord

WORDS = RandomWord()

def color_1() -> list:
    return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

def color_128() -> list:
    colors = []
    while len(colors) < 128:
        new = color_1()
        if new not in colors:
            colors.append(new)
    return colors

def color_unique(unique_colors: list) -> list:
    """
    compares a generated color list[] from color_1()
    with a list of existing unique RGB colors
    returns new RGB color not in use
    """
    new_color = color_1()
    while new_color in unique_colors:
        new_color = color_1()
    return new_color

def make_name() -> str:
    return (WORDS.word(include_categories=["adjective"]) + 
            WORDS.word(include_categories=["noun"]))