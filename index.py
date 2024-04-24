from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer 
import pandas as pd 
from joblib import dump, load

#C:\Users\USER\AppData\Local\Programs\Python\Python37\lib\site-packages\chatterbot\tagging.py
#data dialogs_expanded.csv : ##https://www.kaggle.com/code/hosammhmdali/nlp-chatbot/input
# Create a new ChatBot instance

df = pd.read_csv('corpus.csv')
# Initialize an empty list to store the conversation data
conversations = []

# Iterate over the DataFrame rows and append input text and response pairs to the list
for index, row in df.iterrows():
    conversations.extend([row['input_text'], row['response']])
    
    
    
dialogsdata = pd.read_csv('dialogs_expanded.csv')
# Initialize an empty list to store the conversation data
dialogs = []

# Iterate over the DataFrame rows and append input text and response pairs to the list
for index, row in dialogsdata.iterrows():
    dialogs.extend([row['question'], row['answer']])

bot = ChatBot(
    'chatbot',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, I do not understand.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)


trainer = ListTrainer(bot)
trainer.train(dialogs)

# Create a ChatterBotCorpusTrainer instance and train the bot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


trainer = ListTrainer(bot)
trainer.train(conversations)


# Start the conversation loop
while True:
    try:
        user_input = input("You: ")
        # Check if user input is empty
        if not user_input.strip():
            continue  # Display the input prompt again
        response = bot.get_response(user_input)
        print("Bot:", response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
