print(" ChatBot: Hello! I’m CodSoftBot. Ask me anything or type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        print(" ChatBot: Hey there! How can I assist you today?")
    
    elif "how are you" in user_input:
        print(" ChatBot: I'm just code, but I'm doing great!")

    elif "your name" in user_input or "who are you" in user_input:
        print(" ChatBot: I'm CodSoftBot — your virtual assistant!")

    elif "what can you do" in user_input:
        print(" ChatBot: I can answer simple questions based on set rules. Try asking about me!")

    elif "bye" in user_input or "exit" in user_input:
        print(" ChatBot: Bye! Have a great day!")
        break

    elif "help" in user_input:
        print(" ChatBot: You can say 'hello', ask my name, or say 'bye' to end.")

    else:
        print(" ChatBot: Sorry, I didn't understand that. Try asking something else.")