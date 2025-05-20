def chatbot():
    print("Hi! I'm a chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing fine! 😊")
        elif "name" in user_input:
            print("Chatbot: I'm your simple Python chatbot.")
        elif "help" in user_input:
            print("Chatbot: Sure! You can ask me about anything general.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
