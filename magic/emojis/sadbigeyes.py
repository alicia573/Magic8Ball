from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()

# Define colors
black = (0, 0, 0)       # Black (off)
pink = (255, 105, 180)  # Pink (for the face)
dark_pink = (255, 20, 147)  # Dark pink (for the tears)

# Create an 8x8 pixel art pattern for a pink sad emoji
pink_sad_emoji = [
    black, black, black, black, black, black, black, black,
    black, pink, pink, black, black, pink, pink, black,
    black, pink, pink, black, black, pink, pink, black,
    black, black, black, black, black, black, black, black,
    black, black, black, black, black, black, black, black,
    black, black, pink, pink, pink, pink, black, black,
    black, pink, black, black, black, black, pink, black,
    pink, black, black, black, black, black, black, pink,
]

# Display the pink sad emoji pattern
sense.set_pixels(pink_sad_emoji)
