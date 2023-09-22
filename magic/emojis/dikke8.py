from sense_hat import SenseHat
import time 

# Initialize the Sense HAT
sense = SenseHat() 

# Define colors
white = (0, 0, 0)  # White
pink = (150,50, 128)        # Pink (off)

# Create an 8x8 pixel art pattern for a white "8"
starting_screen = [
    white, pink, pink, pink, pink, pink, pink, white,
    white, pink, pink, white, white, pink, pink, white,
    white, pink, pink, white, white, pink, pink, white,
    white, white, white, pink, pink, white, white, white,
    white, pink, pink, pink, pink, pink, pink, white,
    white, pink, pink, white, white, pink, pink, white,
    white, pink, pink, white, white, pink, pink, white,
    white, pink, pink, pink, pink, pink, pink, white,
]

# Display the white "8" pattern
sense.set_pixels(starting_screen)
time.sleep(5)

sense.clear()
