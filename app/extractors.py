'''Extractor module'''


def find_dam_candidate_phrases(doc_sents, keyword):
    """ Function to identify dam related phrases
    This returns a list of candidate phrase indexes
    from the document sentence list passed in.

    Parameters
    ----------
    document_sentences : list
    """
    dam_idx = []  # Return list

    # Iterate through the sentences looking for keyword
    for idx, sentence in enumerate(doc_sents):
        # Find occurance, append index of sentence below and above.
        # Three total sentences stored. Overlap may occur.
        if keyword in sentence.lower():
            tmp_sentence_index = []
            # print('Evaluating Sentence: ', sentence, '\n')
            tmp_sentence_index.append(doc_sents[idx])
            # Exceptions in place for first and last sentence issues.
            try:
                tmp_sentence_index.append(doc_sents[idx+1])
            except Exception:
                pass
            try:
                tmp_sentence_index.append(doc_sents[idx-1])
            except Exception:
                pass
            dam_idx.append(tmp_sentence_index)
    return dam_idx


def filter_candidate_phrases(phrases, nlp, dams):
    """ Function to use more intensive methods to
    filter the phrases down.

    Parameters
    ----------
    phrases : list
        Python list of 3 sentences.
    """
    match = 0

    # required
    custom = [' dam', ' Dam', 'dam', 'remove', 'Remove', 'removal', 'Removal']
    match_wordlist = 0
    for sentence in phrases:
        # Clean
        phrase = sentence.replace('et', '').replace('al', '')

        for word in custom:
            if word in phrase:
                match_wordlist += 1
                # print('Matched: ', word)
        if match_wordlist == 0:
            return []
        # POS
        for token in nlp(phrase):
            for dam in list(dams['name']):
                if token.text.replace(' ', '') in dam and token.pos_ == 'PROPN':
                    match += 1
    if match > 0:
        return phrases
    else:
        return []