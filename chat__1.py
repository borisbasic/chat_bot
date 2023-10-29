import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

f = open('chat.txt', 'r', errors='ignore', encoding='utf-8')
with open('new_words.txt', 'r', errors='ignore', encoding='utf-8') as buffer:
    list_of_words = buffer.readlines()

raw_doc = f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw_doc) # recenice
word_tokens = nltk.word_tokenize(raw_doc)   # rijeci 

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREET_INPUTS = ('zdravo', 'cao', 'pozdrav', 'dobar dan')
GREET_RESPONSES = ['cao', 'pozdrav', 'zdravo', 'drago mi je. Da li Vam mogu pomoci']

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES )
        


def response(user_response):
    robo1_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo1_response = robo1_response + 'Žao mi je. Možete li preformulisati svoje pitanje?'
        return robo1_response
    else:
        robo1_response = robo1_response + sent_tokens[idx]
        return robo1_response
flag = True
print("Bot: Zovem se Čera. Hajde da razgovaramo. Pitaj šta te zanima o biljkama. Kada ti bude dosadno samo napiši Bok")
while(flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response!='Bok'):
        if(user_response=='hvala' or user_response=='hvala vam'):
            flag=False
            print('Bor: Nema na cemu')
        else:
            if(greet(user_response)!=None):
                print('Bot: '+greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print('Bot: ', end='')
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("Bot: Cao. Budi mi dobro. <3")





