# Magic 8-Ball with SenseHat and Sound

This project simulates a magic 8-ball using a Raspberry Pi with a SenseHat. The 8-ball provides a random answer when shaken, plays sound effects, and can display corresponding emojis on the SenseHat.

## Features:
* **Shake Detection:** Detects when the device has been shaken using the SenseHat's accelerometer.
* **Sound Effects:** Uses `pygame` to play sound effects.
* **Database Integration:** Fetches random 8-ball answers and corresponding emojis from a MySQL database.
* **Text-To-Speech:** Converts the fetched answer to speech using `gtts` (Google Text-to-Speech) and plays it.
* **Emoji Display:** Runs external Python scripts to display the corresponding emoji on the SenseHat.
* **Orientation Management:** Adjusts the orientation of the displayed message on the SenseHat based on the device's orientation.

## Prerequisites:

- `pygame`: For sound effects.
- `pymysql`: For MySQL database connection and operations.
- `gtts`: For converting text to speech.
- `sense_hat`: To interact with the Raspberry Pi's SenseHat.
- `subprocess`: To run external Python scripts for displaying emojis on the SenseHat.

## How to Run:

1. Ensure that you have a Raspberry Pi with a SenseHat attached.
2. Install the required Python libraries:
   `pip install pygame pymysql gtts sense-hat`



3. Set up your MySQL database with a table named `answer` containing the columns `message` and `emoji`.
4. Ensure that the Python scripts for displaying emojis are located in the `emojis/` directory.
5. Run the main Python script:
  `python3 <script_name>.py`

## Usage:

- Shake the Raspberry Pi.
- A sound effect will play.
- After a delay, the magic 8-ball answer will be fetched from the database, converted to speech, and played.
- If a corresponding emoji exists in the database, it will be displayed on the SenseHat.
- The orientation of the message on the SenseHat will adjust based on the orientation of the Raspberry Pi.
