import spacy

nlp = spacy.load("en_core_web_sm")

def segment_and_tokenize(text):
    doc = nlp(text)
    segmented_data = []
    
    # Iterate over the sentences identified by spaCy
    for sent in doc.sents:
        tokens = [token for token in sent]
        segmented_data.append({
            "sentence": sent.text,
            "tokens": tokens
        })
    
    return segmented_data


# text = "Help you, I can."
# doc = nlp(text)

# # Iterate over tokens to extract grammatical structures
# for token in doc:
#     print(f"Token: {token.text}")
#     print(f"  POS: {token.pos_}")
#     print(f"  Dependency: {token.dep_}")
#     print(f"  Head: {token.head.text}")
#     print(f"  Children: {[child.text for child in token.children]}\n")
