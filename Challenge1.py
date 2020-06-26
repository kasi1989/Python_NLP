import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
import pandas as pd

#Read csv using Pandas
input=pd.read_csv("./ticket_Data.csv")  
input.head()
input.shape

# Removing the column TicketId. It is optional, if you want, you can keep it.
input = input.drop("TicketId", axis=1) 

# We will create a new column tokenized_text. This column will contain the tokenized words[list of words]
input['tokenized_text'] = input['Description'].apply(word_tokenize)
input.head()

#Save Description column to a variable
description=data['Description']
                 
#Apply Word Tokenization on every row of the Description column
vocabularyList = [ word_tokenize( str(sentence) ) for sentence in description ]
                 
#Flat out the list of lists
vocabulary = [item.lower() for sublist in vocabularyList for item in sublist]
                 
print("Length of Vocabulary BEFORE removing duplicates: ", len(vocabulary))
#Remove Duplicate tokens
vocabulary = list(dict.fromkeys(vocabulary))
print("\nLength of Vocabulary AFTER removing duplicates: ", len(vocabulary))

#Final Vocabulary                 
print("\nFinal Vocabulary List: \n", vocabulary)
