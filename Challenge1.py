import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
import csv

print ('This is Course 1 of NLTK Training') 

#Reading the input file

with open('/ticket_Data.csv') as inputfile:
  exceldata=inputfile.read()
#Extracting all words
  vocabs = word_tokenize(exceldata)
  #print (vocabs)

#Removing duplicates by converting list into a disctionary
final_vocabs = list(dict.fromkeys(vocabs) )

print ('Unique Word List')
print (final_vocabs)
