import pygame
import pymysql
from gtts import gTTS
from time import sleep
from sense_hat import SenseHat
import subprocess

# Initialize SenseHat and pygame mixer
sense = SenseHat()
pygame.mixer.init()

def start_screen():
    subprocess.run(["python3",f"emojis/dikke8.py" ])


# Play a specific sound effect
def play_sound_effect(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
def get_message_and_emoji_from_db():
    conn = pymysql.connect(host='localhost', user='root', password='root5730', database='magic8ball')
    cursor = conn.cursor()
    
    cursor.execute("SELECT message, emoji FROM answer ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0], result[1]
    return None, None



# Play an audio file
def play_audio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)

# Fetch an answer and play the corresponding TTS
def fetch_eightball_answer():
    message, emoji_file = get_message_and_emoji_from_db()
    if message:
        tts = gTTS(text=message, lang='en')
        print(str(message))
        tts.save("message.mp3")
        print("TTS MP3 generated.") #debug
        play_audio("message.mp3")
        
        if emoji_file:
            # Running the python file to display the emoji on SenseHat
            subprocess.run(["python3",f"emojis/{emoji_file}" ])
        
    return message if message else "Error"

def get_orientation():
    orientation = sense.get_orientation_degrees()
    roll = orientation['roll']
    
    # Print the roll value for debugging
    print("Roll:", roll)

    if 0 <= roll < 180:
        return 0
    else:
        return 180

def was_shaken(prev_values, threshold=1.5):
    # Get current accelerometer values
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    y = accel['y']
    z = accel['z']

    # Calculate difference from previous values
    dx = abs(prev_values['x'] - x)
    dy = abs(prev_values['y'] - y)
    dz = abs(prev_values['z'] - z)

    # Update previous values
    prev_values['x'] = x
    prev_values['y'] = y
    prev_values['z'] = z

    # If change is significant, return True
    if dx > threshold or dy > threshold or dz > threshold:
        return True

    return False
last_orientation = 0

def smooth_rotation():
    global last_orientation
    
    current_orientation = get_orientation()
    
    # Determine the difference
    difference = current_orientation - last_orientation
    
    # Only adjust if the difference is significant
    if abs(difference) >= 45:  # Adjust this threshold as needed
        sense.set_rotation(current_orientation)
        last_orientation = current_orientation
def main():
    start_screen()
    # Initial accelerometer values
    accel = sense.get_accelerometer_raw()
    prev_values = {'x': accel['x'], 'y': accel['y'], 'z': accel['z']}

    # Initial orientation
    last_orientation = get_orientation()
    sense.set_rotation(last_orientation)

    while True:
        if was_shaken(prev_values):
            play_sound_effect('sound.mp3')  # Play a sound effect when shaken
            sleep(5)
            answer = fetch_eightball_answer()
            
            smooth_rotation()  # Adjust the orientation smoothly
            
            #sense.show_message(answer, scroll_speed=0.2)
            sleep(1)  # delay to avoid repeated immediate shakes

if __name__ == "__main__":
    main()
