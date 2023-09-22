from sense_hat import SenseHat

# Initialiseer de Sense HAT
sense = SenseHat()

# Definieer kleuren 
groen = (0, 255, 0)  # Groen
zwart = (0, 0, 0)    # Zwart (uit)

# Maak een pixelart-patroon van een groen vinkje
groen_vinkje_patroon = [
    zwart, zwart, zwart, zwart, zwart, zwart, zwart, zwart,
    zwart, zwart, zwart, zwart, zwart, zwart, zwart, zwart,
    zwart, zwart, zwart, zwart, zwart, zwart, zwart, zwart,
    zwart, zwart, zwart, zwart, zwart, zwart, zwart, groen,
    groen, zwart, zwart, zwart, zwart, zwart, groen, zwart,
    zwart, groen, zwart, zwart, zwart, groen, zwart, zwart,
    zwart, zwart, groen, zwart, groen, zwart, zwart, zwart,
    zwart, zwart, zwart, groen, zwart, zwart, zwart, zwart,
]

# Toon het groene vinkje-patroon
sense.set_pixels(groen_vinkje_patroon)

