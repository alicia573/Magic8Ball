from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()

# Define colors
red = (255, 0, 0)  # Red
black = (0, 0, 0)  # Black (off)

# Create an 8x8 pixel art pattern for a red "X"
red_x_pattern = [
    red, black, black, black, black, black, black, red,
    black, red, black, black, black, black, red, black,
    black, black, red, black, black, red, black, black,
    black, black, black, red, red, black, black, black,
    black, black, black, red, red, black, black, black,
    black, black, red, black, black, red, black, black,
    black, red, black, black, black, black, red, black,
    red, black, black, black, black, black, black, red,
]

# Display the red "X" pattern
sense.set_pixels(red_x_pattern)
