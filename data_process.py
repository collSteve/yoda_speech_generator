import pandas as pd
import re
import spacy


nlp = spacy.load("en_core_web_sm")


def extract_yoda_lines(file_path):
    df = pd.read_csv(file_path)

    yoda_df = df[df['character'].str.lower() == 'yoda']
    yoda_lines = yoda_df.to_dict(orient='records')
    return yoda_lines


def clean_text(txt):
    txt = txt.strip()                           # trim whitespace
    txt = re.sub(r"\s+", " ", txt)              # collapse multiple spaces
    txt = txt.replace("“","\"").replace("”","\"").replace("’","'")
    txt = re.sub(r"[^ -~]", "", txt)            # remove non-ASCII
    txt = txt.lower()                           # unify casing
    return txt

def split_into_sentences(text: str) -> list:
    """
    Uses spaCy to segment the text into individual sentences.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]


# Apply cleaning

## extract_yoda_lines("data/yoda-corpus.csv")



