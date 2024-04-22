#pip's required: pandas, matplotlab, seaborn

#Task 1
import pandas as pd

def extract_text(file):
    df = pd.read_csv(file)
    # Concatenate all text from each row
    combined_text = ""
    for index, row in df.iterrows():
        combined_text += str(row) + "\n"
    return combined_text

# List of CSV files
file_names = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Iterate through each file
all_text = ""
for file in file_names:
    file_text = extract_text(file)
    all_text += file_text + "\n"

# Writing all the combined text to a single .txt file
with open('all_text.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(all_text)

# Now 'all_text.txt' should contain the combined text from all CSV files
print("Combined text saved to 'all_text.txt'")








#Task 2

#In CMD 
#pip install spacy
#pip install scispacy
#pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.
#pip install transformers









#Task 3.1
#pip's required: spacy, scispacy, pandas, matplotlib, seaborn & 'python -m spacy download en_core_web_sm'

import pandas as pd
from collections import Counter

# For reading the combined text file:
with open('all_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenising the text and count occurrences:
words = text.split()
word_counts = Counter(words)

# Getting the top 30 most common words:
top_30_words = word_counts.most_common(30)

# Save top 30 words and counts to a CSV file
df_top_30 = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df_top_30.to_csv('top_30_words.csv', index=False)









#Task 3.2
#pip's required: spacy, scispacy, pandas, matplotlib, seaborn & 'python -m spacy download en_core_web_sm'

import pandas as pd
from transformers import AutoTokenizer
from collections import Counter

# Load the Auto Tokenizer
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

# Read the combined text file
with open('all_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text
tokens = tokenizer.tokenize(text)

# Count occurrences of each token
token_counts = Counter(tokens)

# Get the top 30 most common tokens
top_30_tokens = token_counts.most_common(30)

# Save top 30 tokens and counts to a CSV file
df_top_30_tokens = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])
df_top_30_tokens.to_csv('top_30_tokens.csv', index=False)

# Print the top 30 tokens
print("Top 30 tokens and their counts:")
for token, count in top_30_tokens:
    print(f"{token}: {count}")









#Task 4
#pip's required: spacy, scispacy, nltk, pandas & 'python -m spacy download en_core_web_sm'

import pandas as pd
import spacy
import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter

# Loading the spacy model
nlp = spacy.load("en_core_web_sm")

# Setting a higher max_length to accommodate longer texts
nlp.max_length = 20000000

# Reading the combined text file
with open('all_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Use NLTK for sentence segmentation
sentences = sent_tokenize(text)

# Initialising counters for diseases and drugs
diseases_counts = Counter()
drugs_counts = Counter()

# Processing each sentence with the model
for sentence in sentences:
    doc = nlp(sentence)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']
    diseases_counts.update(diseases)
    drugs_counts.update(drugs)

# Saving the entities and counts to CSV files
df_diseases = pd.DataFrame(diseases_counts.items(), columns=['Disease', 'Count'])
df_drugs = pd.DataFrame(drugs_counts.items(), columns=['Drug', 'Count'])

df_diseases.to_csv('diseases.csv', index=False)
df_drugs.to_csv('drugs.csv', index=False)

# Printing the entities and counts
print("Entities and Counts:")
print("Total Diseases:", len(diseases_counts))
print("Total Drugs:", len(drugs_counts))
print("Top 5 Diseases:")
for disease, count in diseases_counts.most_common(5):
    print(f"{disease}: {count}")
print("Top 5 Drugs:")
for drug, count in drugs_counts.most_common(5):
    print(f"{drug}: {count}")