## Text Mining Application 

A simple python text mining application to identify possibly relevant scientific documents for a set of keywords related to dam removal. This application processes _phrases_ that represent a list that contains 3 sentences. 

### Command Line Arguments

```
# Runs a document-level random forest model to classify into 3 classes
# Output into output directory
-classify

# GeoDeepDive text mining
-gdd

# Local file (in development)
-local
```

#### Document Classification (in progress) 

Currently configured to process one and print the classification 

#### Keywords 

Custom stopwords:

```
[' dam', ' Dam', 'dam', 'remove', 'Remove', 'removal', 'Removal']
```

#### Development Requirements 

This was built using Python 3.6 with the packages found in the requirements. 

#### Provisional Software Disclaimer

Under USGS Software Release Policy, the software codes here are considered preliminary, not released officially, and posted to this repo for informal sharing among colleagues.

This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.