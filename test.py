import spacy

nlp = spacy.load("en_core_web_sm")

def segment_sentence_to_phrases(text):
    """
    Segments a sentence into phrases with grammatical labels.
    For example, for "Your father he is." it should output:
      - "Your father" labeled as OBJ (object/attribute)
      - "he" labeled as SUBJ (subject)
      - "is" labeled as VERB (main verb)
    
    Returns:
        List[dict]: A list of chunks with keys "text", "label", "start", "end"
    """
    doc = nlp(text)
    chunks = []
    
    # 1. Use spaCy's noun_chunks to extract noun phrases.
    for nc in doc.noun_chunks:
        # Decide the label based on the dependency of the noun chunk's root.
        if nc.root.dep_ in ("nsubj", "nsubjpass"):
            label = "SUBJ"
        elif nc.root.dep_ in ("dobj", "attr", "pobj"):
            label = "OBJ"
        else:
            label = "NP"  # generic noun phrase
        chunks.append({
            "text": nc.text,
            "label": label,
            "start": nc.start,
            "end": nc.end
        })
    
    # 2. Identify verb tokens not already covered by noun chunks.
    covered_indices = set()
    for chunk in chunks:
        covered_indices.update(range(chunk["start"], chunk["end"]))
    
    tokens = list(doc)
    i = 0
    while i < len(tokens):
        if i not in covered_indices and tokens[i].pos_ == "VERB":
            start = i
            # Group contiguous verbs together.
            while i < len(tokens) and i not in covered_indices and tokens[i].pos_ == "VERB":
                i += 1
            chunks.append({
                "text": doc[start:i].text,
                "label": "VERB",
                "start": start,
                "end": i
            })
        else:
            i += 1
    
    # 3. Optionally, group any remaining tokens into a miscellaneous chunk.
    # This ensures every token is included in some chunk.
    covered_indices = set()
    for chunk in chunks:
        covered_indices.update(range(chunk["start"], chunk["end"]))
    
    i = 0
    while i < len(tokens):
        if i not in covered_indices:
            start = i
            while i < len(tokens) and i not in covered_indices:
                i += 1
            chunks.append({
                "text": doc[start:i].text,
                "label": "MISC",
                "start": start,
                "end": i
            })
        else:
            i += 1

    # 4. Sort the chunks in the order they appear in the sentence.
    chunks = sorted(chunks, key=lambda x: x["start"])
    return chunks

if __name__ == "__main__":
    sentence = "The dependency parser jointly learns sentence segmentation and labelled dependency parsing, and can optionally learn to merge tokens that had been over-segmented by the tokenizer."
    phrases = segment_sentence_to_phrases(sentence)
    for phrase in phrases:
        print(phrase)