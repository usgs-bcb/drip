# Preprocessing PDF Documents

Documentation for a possible workflow batch converting PDFs to machine readable text not following the GeoDeepDive process. 

### Requirements

* CentOS vm (processing)
* Mac OS (development)
* pdftotext and all required packages to install

#### Transfer using shared directory

```sh
scp -r user@url:/Users/Shared/data/pdf .
```

#### Pdftotext

```sh
ls *.pdf | xargs -n1 pdftotext
```

#### Transfer back

```sh
scp -r . user@url:/Users/Shared
```

