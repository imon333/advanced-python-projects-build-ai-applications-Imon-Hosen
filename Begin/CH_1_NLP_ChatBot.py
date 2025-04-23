from textblob import TextBlob

intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": ["We are open from 9 AM to 5 PM, Monday to Friday"]
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": ["I'd be happy to help you with the return process. Let me transfer you to a live agent."]
    }
}

def get_response(message):
    message = message.lower()
    
    # Check if the message contains any keywords associated with defined intents
    for intent_data in intents.values():
        if any(keyword in message for keyword in intent_data["keywords"]):
            return intent_data["response"][0]  # Return the first response
    
    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity
    
    # Return a response based on the sentiment score
    return ("That's so great to hear!" if sentiment > 0 else
            "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
            "I see. Can you tell me more about that?")

def chat():
    print("Chatbot: Hi, How can I help you today?")
    
    while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")

    print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    chat()
