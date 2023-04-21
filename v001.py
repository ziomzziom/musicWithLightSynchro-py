import time
import random

# define the color for each key
colors = {
    "A": (255, 0, 0),
    "S": (0, 255, 0),
    "D": (0, 0, 255),
    "F": (255, 255, 0),
    "G": (255, 0, 255),
    "H": (0, 255, 255),
    "J": (255, 128, 0),
    "K": (128, 255, 0),
    "L": (0, 128, 255),
    ";": (128, 0, 255)
}

# define the frequency range for each key
frequencies = {
    "A": (261.63, 523.25),
    "S": (293.66, 587.33),
    "D": (329.63, 659.25),
    "F": (349.23, 698.46),
    "G": (392.00, 783.99),
    "H": (440.00, 880.00),
    "J": (493.88, 987.77),
    "K": (523.25, 1046.50),
    "L": (587.33, 1174.66),
    ";": (659.25, 1318.51)
}

# simulate the music playing
def play_music():
    while True:
        time.sleep(0.5)
        frequency = random.choice(list(frequencies.values()))
        print(f"Playing frequency range: {frequency}")

# change the color of the keyboard based on the playing frequency range
def change_color(frequency_range):
    for key, color in colors.items():
        if frequencies[key][0] <= frequency_range <= frequencies[key][1]:
            print(f"Key {key} is playing with frequency {frequency_range}. Changing color to {color}")
        else:
            print(f"Key {key} is not playing with frequency {frequency_range}. Keeping color as is.")

# main loop
while True:
    frequency_range = random.uniform(250, 1500)
    print(f"Random frequency range: {frequency_range}")
    change_color(frequency_range)
