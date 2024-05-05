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
print('Task 1 Complete')

#Task 2

#In CMD 
#pip install spacy
#pip install scispacy
#pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.
#pip install transformers

#Task 3.1
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
print("Top 30 words saved to 'top_30_words.csv'")
print('Task 3.1 complete')


#Task 3.2

from transformers import AutoTokenizer
from collections import Counter

# Load the Auto Tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Tokenizing the text
tokens = tokenizer.tokenize(text)  # Use 'text' instead of 'combined_text'

# Counting occurrences of each token
token_counts = Counter(tokens)

# Getting the top 30 most common tokens
top_30_tokens = token_counts.most_common(30)

# Creating a DataFrame from the top 30 tokens
df_top_tokens = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])

# Saving the top 30 tokens to a CSV file
df_top_tokens.to_csv('top_30_tokens.csv', index=False)

print("Top 30 tokens saved to 'top_30_tokens.csv'")
print('Task 3.2 complete')

#Task 4

# Task 4 part 4: Function to compare most common words
def compare_most_common_words(model_words, other_model_words, model_name, other_model_name):
    common_words = set(model_words) & set(other_model_words)
    unique_model_words = set(model_words) - set(other_model_words)
    unique_other_model_words = set(other_model_words) - set(model_words)

    # Ensure that all lists have the same length
    max_length = max(len(common_words), len(unique_model_words), len(unique_other_model_words))

    # Pad the lists with empty strings to the same length
    common_words = list(common_words)[:max_length] + [''] * (max_length - len(common_words))
    unique_model_words = list(unique_model_words)[:max_length] + [''] * (max_length - len(unique_model_words))
    unique_other_model_words = list(unique_other_model_words)[:max_length] + [''] * (max_length - len(unique_other_model_words))

    # Create a list for the 'Total Entities' column with the same value for all rows
    total_entities_model = [len(model_words)] * max_length
    total_entities_other_model = [len(other_model_words)] * max_length

    comparison_result = {
        f'{model_name} Unique Words': unique_model_words,
        f'{other_model_name} Unique Words': unique_other_model_words,
        'Common Words': common_words,
        f'Total {model_name} Entities': total_entities_model,
        f'Total {other_model_name} Entities': total_entities_other_model,
    }

    return pd.DataFrame(comparison_result, columns=[f'{model_name} Unique Words', f'{other_model_name} Unique Words', 'Common Words'])

# Function to get most common words
def get_most_common_words(text, top_n=100):
    words = text.split()
    word_counts = Counter(words)
    return dict(word_counts.most_common(top_n))

# Get most common words for each model
most_common_words_sci = get_most_common_words(text)
most_common_words_bc5cdr = get_most_common_words(text)
most_common_words_biobert = get_most_common_words(text)

# Compare most common words
comparison_sci_bc5cdr = compare_most_common_words(most_common_words_sci, most_common_words_bc5cdr, 'spaCy (Sci)', 'spaCy (BC5CDR)')
comparison_sci_biobert = compare_most_common_words(most_common_words_sci, most_common_words_biobert, 'spaCy (Sci)', 'BioBERT')
comparison_bc5cdr_biobert = compare_most_common_words(most_common_words_bc5cdr, most_common_words_biobert, 'spaCy (BC5CDR)', 'BioBERT')

# Export comparisons to CSV
comparison_sci_bc5cdr.to_csv('comparison_sci_bc5cdr.csv', index=False)
comparison_sci_biobert.to_csv('comparison_sci_biobert.csv', index=False)
comparison_bc5cdr_biobert.to_csv('comparison_bc5cdr_biobert.csv', index=False)

print('Task 4 complete')
