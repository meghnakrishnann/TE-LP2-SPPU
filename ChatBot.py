import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    #
    [
        r"my name is (.)",
        ["Hello %1, How are you"]
    ],
    # Or expression
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello my name is AI Chatbot"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by meghna. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Meghna created me using Python's NLTK library ","top secret ;)",]
    ],

    [
        r"quit",
        ["Thank you for using our intelligence services"]
    ],
    

]

def chat():
    print("Hey there! I am AI Chat bot at your service")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()
