from speech import say
from config import api_key
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

# Ensure the AI21 API Key is set in the environment variables
API_KEY = api_key
if not API_KEY:
    raise ValueError("API key not found. Set AI21_API_KEY as an environment variable.")

client = AI21Client(api_key=API_KEY)

# Store the conversation history
chat_history = []

def chat(query):
    
    """
    Function to send a query to AI21's API and get a response.
    Parameters:
        query (str): User's input question or statement.
    Returns:
        str: AI21's response.
    """
    global chat_history

    # Append user's query to the conversation history
    chat_history.append(ChatMessage(content=query, role="user"))

    try:
        # Send the request to AI21 API
        response = client.chat.completions.create(
            messages=chat_history,
            model="jamba-1.5-mini",  # Use the optimized model
            stream=True  # Enable streaming for better performance
        )

        # Collect and print the response in chunks
        print(f"User: {query}\n\n Bharat AI: \n", end="")
        full_response = ""
        for chunk in response:
            # Access the delta content directly from the object and handle NoneType safely
            content = chunk.choices[0].delta.content
            if content:  # Only concatenate if content is not None
                print(content, end="")
                full_response += content

        # Append the AI's response to the conversation history
        chat_history.append(ChatMessage(content=full_response, role="assistant"))
        print()  # Print a new line after streaming
        say(full_response)
        return full_response

    except KeyError as e:
        print(f"KeyError: Missing expected key in response: {e}")
    except ValueError as e:
        print(f"ValueError: Invalid input or parameter: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, something went wrong."

# Example usage
# if __name__ == "__main__":
#     print("Chat with AI! Type 'exit' to quit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         response = chat(user_input)
#         print(response)
