import os
import datetime
import time
#import random
#import numpy as np
import pywhatkit as kit
from questions import open_response
from sites import open_site #imported sites from site page

#importing say() function from speech
from speech import say
#importing chat from chatbot
from chatbot import chat, chat_history
#importing ai from gptai
from gptai import ai
#importing programs
from programs import open_program
#import take command
from micinput import takeCommand

if __name__ == '__main__':
    print('Welcome to Bharat A.I')
    say("WellCome Too Bhaarat A. I.")
    while True:
        print("Listening...")
        query = takeCommand()
         
        # Handle opening websites
        open_site(query)

        # Handle opening programs
        open_program(query)
        
        # Handle questions
        open_response(query)
                   
        # Play a specific song
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

        # Check time and report it
        elif "time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")
            
        elif "date" in query.lower():
            dt=datetime.datetime.now().strftime("%D")
            month=datetime.datetime.now().strftime("%B")
            #print(day)
            say(f"Sir today's date is {dt[3:5]} {month} 20{dt[6:]}")
        
        elif "day" in query.lower():
            day=datetime.datetime.now().strftime("%A")
            say(f"Sir Today is {day}")
        
        # Shutdown system
        elif "shutdown" in query.lower():
            try:
                say("Shutting down the system sir.")
                kit.shutdown()
            except Exception as e:
                say("Some Error occurred while shutting down the system")
        
        # Cancel shutdown
        elif "cancel shutdown" in query.lower():
            try:
                say("Cancelling Shutdown  sir.")
                kit.cancel_shutdown()
                say("Shutdown Successful  sir.")
            except Exception as e:
                print("Error: ",e)
                say("Unable to cancel the shutdown")
        
        # Screenshot task
        elif "screenshot" in query.lower() or "screenshots" in query.lower():
            try:
                if not os.path.exists("Screenshots"):
                    say("Creating separate folder for storing screenshots sir")
                    os.mkdir("Screenshots")
                say("Taking Screenshot Sir.")
                screenshot_path = f"Screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                kit.take_screenshot(screenshot_path)
                say("Screenshot taken and saved.")
            except Exception as e:
                print("Unable to take screenshot. Some error occurred", e)
                say("Unable to take screenshot. Some error occurred")

        # Handle AI commands
        elif "Using artificial intelligence" in query.lower() or "ai" in query.lower() or "bharat ai" in query.lower():
            ai(prompt=query)

        # Quit Bharat AI
        elif "Bharat Quit" in query.lower() or "quit" in query.lower() or "exit" in query.lower():
            say("Goodbye! Have a great day.")
            break  # Use break to exit the while loop

        # Reset chat history
        elif "reset chat" in query.lower():
            say("Sure, Clearing chat.")
            chat_history = ""
            
        # Show chat history
        elif "show chat history" in query.lower():
            say("Showing Chat history")
            print(chat_history)

        # Default chat handler
        else:
            say("Sure, let's start chatting.")
            chat(query)
