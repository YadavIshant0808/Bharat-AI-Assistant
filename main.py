import os
import datetime
import pywhatkit as kit
from questions import open_response
from sites import open_site
from speech import say
from chatbot import chat, chat_history
from gptai import ai
from programs import open_program
from get_wheather import main, get_location
from micinput import takeCommand
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # You can also use "microsoft/DialoGPT-small" or "microsoft/DialoGPT-large"

def initialize_model():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

# Initialize responses list to store conversation history
responses = []

def handle_nlp_query(query, tokenizer, model, chat_history_ids=None):
    input_ids = tokenizer.encode(query + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if chat_history_ids is not None else input_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output, chat_history_ids

if __name__ == '__main__':
    print('Welcome to Bharat A.I')
    say("Welcome to Bharat A. I.")
    
    tokenizer, model = initialize_model()
    chat_history_ids = None
    
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
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes")
            
        elif "date" in query.lower():
            date = datetime.datetime.now().strftime("%d")
            month = datetime.datetime.now().strftime("%B")
            year = datetime.datetime.now().strftime("%Y")
            say(f"Sir, today's date is {date} {month} {year}")
        
        elif "day" in query.lower():
            day = datetime.datetime.now().strftime("%A")
            say(f"Sir, today is {day}")
        
        # Get location
        elif "location" in query.lower():
            location = get_location()
            print(location)
            say(location)

        elif "weather" in query.lower():
            weather = main()
            print(weather)
            say(weather)

        # Shutdown system
        elif "shutdown" in query.lower():
            try:
                say("Shutting down the system, sir.")
                kit.shutdown()
            except Exception as e:
                say("Some error occurred while shutting down the system")

        # Cancel shutdown
        elif "cancel shutdown" in query.lower():
            try:
                say("Cancelling shutdown, sir.")
                kit.cancel_shutdown()
                say("Shutdown cancelled, sir.")
            except Exception as e:
                say("Unable to cancel the shutdown")

        # Screenshot task
        elif "screenshot" in query.lower() or "screenshots" in query.lower():
            try:
                if not os.path.exists("Screenshots"):
                    say("Creating a separate folder for storing screenshots, sir")
                    os.mkdir("Screenshots")
                say("Taking screenshot, sir.")
                screenshot_path = f"Screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                kit.take_screenshot(screenshot_path)
                say("Screenshot taken and saved.")
            except Exception as e:
                say("Unable to take screenshot. Some error occurred")

        # Handle AI commands
        elif "using artificial intelligence" in query.lower() or "ai" in query.lower() or "bharat ai" in query.lower():
            ai(prompt=query)

        # Quit Bharat AI
        elif "bharat quit" in query.lower() or "quit" in query.lower() or "exit" in query.lower():
            say("Goodbye! Have a great day.")
            break  # Use break to exit the while loop

        # Reset chat history
        elif "reset chat" in query.lower():
            say("Sure, clearing chat.")
            chat_history.clear()
            chat_history_ids = None
            
        # Show chat history
        elif "show chat history" in query.lower():
            say("Showing chat history")
            print(chat_history)

        # Handle NLP queries
        else:
            response, chat_history_ids = handle_nlp_query(query, tokenizer, model, chat_history_ids)
            say(response)
            print(f"User: {query}\nBharat A.I: {response}\n")
            responses.append((query, response))