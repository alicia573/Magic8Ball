from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()

# Define colors
p = (255, 105, 180)  # Pink
b = (0, 0, 0)        # Black (off)

# Pink Thumbs-up symbol
pink_thumbs_up = [
    b, b, b, b, b, b, b, b,
    b, p, p, b, b, p, p, b,
    b, p, p, b, b, p, p, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    p, b, b, b, b, b, b, p,
    b, p, p, p, p, p, p, b,
    b, b, b, b, b, b, b, b
]

# Display the pink thumbs-up symbol
sense.set_pixels(pink_thumbs_up)
