import spacy
from data_process import extract_yoda_lines
from segment import segment_and_tokenize

nlp = spacy.load("en_core_web_sm")

def transform_to_word_order(text):
    doc = nlp(text)

    # determine S, V, O
    subjects = []
    verbs = []
    objects = []

    for token in doc:
        if token.dep_ == "nsubj":
            subjects.append(token.text)
        elif token.dep_ == "ROOT":
            verbs.append(token.text)
        elif token.dep_ == "dobj":
            objects.append(token.text)
    
    return subjects, verbs, objects



if __name__ == "__main__":
    yoda_lines = extract_yoda_lines("data/yoda-corpus.csv")

    yoda_sents = []
    for line in yoda_lines:
        # print(line)
        segs = segment_and_tokenize(line["text"])
        for seg in segs:
            yoda_sents.append(seg["sentence"])

    analysis = []
    for sent in yoda_sents:
        subjects, verbs, objects = transform_to_word_order(sent)
        analysis.append({
            "sentence": sent,
            "subjects": subjects,
            "verbs": verbs,
            "objects": objects
        })

    print(analysis)