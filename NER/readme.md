# Training Custom Named Entity Recognition Tags

Please see the notebook "spacy ner training.ipynb" for an example workflow training a new named entity using spaCy. 

## Sample Output

Trained on 80% of small sample dataset (~87 labels)

```
Low Head
Dam
Pete Thompson
Methods of Dam
Passive Dam
Channels Following Dam
Passive Dam
Passive Dam
Stochastic Incipient Motion Criterion
Open Channel Flow
Water Data Coordination
Hawkesville Dam
Hawkesville Dam
Huttonville Dam
Huttonville Dam
ELEVATION(m)
Greenfield Dam
```

### Requirements

```sh
pip install -r requirements.txt
```

## DAM NER 

Trained model can be found at './dam-ner-spacy',  and can be used as a regular spacy model:

```python
import spacy

nlp = spacy.load('./dam-ner-spacy')
```

### Labeling Data

We used BRAT to help annotate training examples.

```
BRAT NER Tag: "PERSON" = River NER 

BRAT NER Tag: "ORGANIZATION" = Dam NER
```