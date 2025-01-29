import sys # Used for handling input/output and errors
import subprocess # Used to run command-line commands

with open("models.id", "rt") as file:
    models = file.read()
    models = models.split("\n")

def process_input(query):
    try:
        # Runs model with through Ollama with modelname
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME],
            input=query,
            text=True, # Specifies to read output as text instead of raw form
            stdout=subprocess.PIPE, # Capture standard output
            stderr=subprocess.PIPE # Capture standard error
        )

        if result.returncode == 0:
            print(result.stdout) # If no error occurs, returns standard output
        else:
            print(f"{result.stderr}", file=sys.stderr) # Returns error message

    except FileNotFoundError:
        print("Ollama is not installed or not in accessible directory.", file=sys.stderr)
    except UnicodeDecodeError:
        print("Model attempting to use unsupported characters.")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr) # Handles other errors

def model_selector(models):
    print("Choose a Model:")
    for i in range(len(models)):
        print(f"[{i+1}] {models[i]}")
    return models[int(input())-1]

def main():
    print("CLI LLM Client")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            query = input("Enter your prompt: ")
            if query.lower() == "quit":
                break
            process_input(query)
        except KeyboardInterrupt:
            print("\nExiting...", file=sys.stderr)
            break

if __name__ == "__main__":
    MODEL_NAME = model_selector(models)
    print(MODEL_NAME)
    main()