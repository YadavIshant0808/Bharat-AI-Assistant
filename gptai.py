from speech import say
import os
from config import api_key
import google.generativeai as genai


# Ensure the AI21 API Key is set in the environment variables
API_KEY = api_key
if not API_KEY:
    raise ValueError("API key not found. Set AI21_API_KEY as an environment variable.")



def ai(prompt):
    """
    Function to send a prompt to Bharat A.I.'s API and save the response to a file.
    Parameters:
        prompt (str): The input prompt to the AI.
    """
    try:
    
        # Send the request to gemini  API
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Send the request to Bharat A.I. API
        response_stream = model.generate_content(prompt)

        # Collect the AI's response
        text = f"Bharat A.I. response for Prompt: {prompt} \n *************************\n\n"
        response_text = ""
        response_text += response_stream
        text += response_text

        # Create a directory for saving responses, if it doesn't exist
        output_dir = "Bharat A.I."
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        # Generate a filename based on the prompt
        sanitized_prompt = ''.join(e for e in prompt if e.isalnum() or e.isspace()).strip()
        filename = os.path.join(output_dir, f"{sanitized_prompt[:50]}.txt")

        # Save the response to a file
        with open(filename, "w") as f:
            f.write(text)

        print(f"Response saved to {filename}")
        say(f"Response saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
