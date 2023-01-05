# Import spaCy module
import spacy

# Load the English language module 'en_core_web_md' in variable 'nlp'
nlp = spacy.load('en_core_web_md')

# Compared outputs with the smaller language model 'en_core_web_sm'
# My comment on the results: There is a significantly higher similarity in all instances using the small language model.
# It also prints the UserWarning: [W007].

# nlp = spacy.load('en_core_web_sm')

# Assign words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("screwdriver")

# Print out the similarity between the words
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word1.similarity(word4))

# Notes:
#   -   There is a significant similarity of ~0.6 between 'cat' and 'monkey' as they are both animals.
#   -   'Banana' and 'monkey' have a 0.4 similarity as the former is eaten by the latter. 
#       This is in contrast to 'banana' and 'cat' which is only a 0.2 similarity.
#   -   'cat' and 'screwdriver' being completely unrelated gives a 0.07 similarity, which makes sense.