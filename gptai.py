import os
from speech import say  # Ensure this module exists and works as expected
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from config import api_key  # Assuming API key is stored in config.py as "apikey"

# Validate API key
if not api_key:
    raise ValueError("API key is missing. Please set it in config.py.")

# Initialize the Bharat A.I. client
try:
    client = AI21Client(api_key=api_key)  # Updated client initialization
except Exception as e:
    raise RuntimeError(f"Failed to initialize AI client: {e}")

def ai(prompt):
    """
    Function to send a prompt to Bharat A.I.'s API and save the response to a file.
    Parameters:
        prompt (str): The input prompt to the AI.
    """
    try:
        # Format prompt into a conversation message
        messages = [ChatMessage(content=prompt, role="user")]

        # Send the request to Bharat A.I. API
        response_stream = client.chat.completions.create(
            messages=messages,
            model="jamba-1.5-mini",  # Ensure the model name is correct
            stream=True  # Enable streaming for better performance
        )

        # Collect the AI's response
        text = f"Bharat A.I. response for Prompt: {prompt} \n *************************\n\n"
        response_text = ""

        for chunk in response_stream:
            # Safely extract content from the streamed response
            content = chunk.choices[0].delta.content
            if content:  # Skip if content is None
                response_text += content

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
