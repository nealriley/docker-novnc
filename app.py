from interpreter import interpreter
import os

def main():
    # Configure interpreter to use Ollama
    interpreter.offline = True
    interpreter.llm.model = "ollama/codestral"
    interpreter.llm.api_base = "https://jarvis.ngrok.dev"  # This allows access to the host machine from within Docker

    interpreter.auto_run = True
    interpreter.conversation_history = []

    # Print a message about the data directory
    print("Data directory contents:")
    print(os.listdir("/data"))

    # Define a simple default query
    default_query = "How many files are in the /data directory?"

    # Run the default query
    print(f"Executing default query: {default_query}")
    response = interpreter.chat(default_query)

    # Print the response
    print("Response from interpreter:")
    print(response)

    # Save the response to a file in the data directory
    with open("/data/interpreter_response.txt", "w") as f:
        f.write(response)

    print("Response saved to /data/interpreter_response.txt")

if __name__ == "__main__":
    main()
