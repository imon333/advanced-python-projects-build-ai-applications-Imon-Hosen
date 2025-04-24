from textblob import TextBlob

# Define comprehensive intents and responses
intents = {
    "hours": {
        "keywords": ["hours", "open", "close", "opening", "closing", "timing"],
        "response": ["We are open from 9 AM to 5 PM, Monday to Friday."]
    },
    "return": {
        "keywords": ["refund", "money back", "return", "exchange"],
        "response": ["I'd be happy to help you with the return process. Please make sure you have your receipt and the product is in original condition."]
    },
    "shipping": {
        "keywords": ["shipping", "delivery", "ship", "send"],
        "response": ["Standard shipping takes 3-5 business days. Expedited options are also available at checkout."]
    },
    "payment": {
        "keywords": ["payment", "pay", "card", "credit", "debit", "cash", "paypal"],
        "response": ["We accept Visa, MasterCard, PayPal, and cash on delivery in select areas."]
    },
    "tracking": {
        "keywords": ["track", "tracking", "where is", "order status", "shipment"],
        "response": ["You can track your order using the tracking number sent to your email."]
    },
    "product_info": {
        "keywords": ["details", "specs", "information", "features", "product"],
        "response": ["Please let me know which product you're referring to so I can provide more details."]
    },
    "complaint": {
        "keywords": ["bad", "worst", "terrible", "complain", "angry", "problem", "issue"],
        "response": ["I'm really sorry to hear that. Let me know what happened so I can help fix it."]
    },
    "compliment": {
        "keywords": ["great", "awesome", "thank you", "love", "excellent", "good", "nice"],
        "response": ["Thank you so much! We appreciate your kind words!"]
    },
    "location": {
        "keywords": ["location", "where", "address", "store"],
        "response": ["Our store is located at 123 Main Street, Downtown. Come visit us!"]
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "call"],
        "response": ["You can reach us at support@example.com or call us at (123) 456-7890."]
    },
    "help": {
        "keywords": ["help", "assist", "support"],
        "response": ["I'm here to help! Please tell me what you need assistance with."]
    }
}

# Intent matching using keyword scanning
def get_intent_response(message):
    message = message.lower()
    for intent_data in intents.values():
        if any(keyword in message for keyword in intent_data["keywords"]):
            return intent_data["response"][0]
    return None

# Sentiment fallback response
def get_sentiment_response(message):
    polarity = TextBlob(message).sentiment.polarity
    if polarity > 0:
        return "That's wonderful to hear! 😊"
    elif polarity < 0:
        return "I'm sorry to hear that. Let me try to help. 💬"
    else:
        return "Got it! Can you tell me more? 🤔"

# Core response function
def get_response(message):
    response = get_intent_response(message)
    if response:
        return response
    return get_sentiment_response(message)

# Main chatbot loop
def chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Thanks for chatting. Have a great day! 👋")
            break
        print(f"Chatbot: {get_response(user_message)}")

# Run the chatbot
if __name__ == "__main__":
    chat()
