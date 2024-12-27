from speech import say
from config import api_key
import google.generativeai as genai


# Ensure the AI21 API Key is set in the environment variables
API_KEY = api_key
if not API_KEY:
    raise ValueError("API key not found. Set AI21_API_KEY as an environment variable.")



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
 
    # Append user's query to the conversation history
    # chat_history.append("User:\t",query)

    try:
        # Send the request to gemini  API
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)

        # Collect and print the response in chunks
        print(f"User: {query}\n\n Bharat AI: \n", end="")
        full_response = ""
        full_response += str(response)
       
        # Append the AI's response to the conversation history
        # chat_history.append("AI:\t",full_response)
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
