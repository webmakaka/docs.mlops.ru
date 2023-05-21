---
layout: page
title: Kubeflow for Machine Learning From Lab to Production - Data and Feature Preparation
description: Kubeflow for Machine Learning From Lab to Production - Data and Feature Preparation
keywords: Kubeflow for Machine Learning From Lab to Production - Data and Feature Preparation
permalink: /books/kubeflow-for-machine-learning-from-lab-to-production/data-and-feature-preparation/
---

<br/>

# Chapter 05. Data and Feature Preparation

<br/>

```
$ cd ~
$ source kfvenv/bin/activate
```

<br/>

```
$ {
  pip3 install lxml
  pip3 install pandas
  pip3 install scikit-learn
  pip3 install scipy
  pip3 install tables
}
```

<br/>

```
$ cd ~/tmp/Kubeflow-for-Machine-Learning-From-Lab-to-Production/ch05/data-extraction/python-notebook/
$ python3 MailingListDataPrep.py
```

<br/>

```
Traceback (most recent call last):
  File "MailingListDataPrep.py", line 118, in <module>
    records += scrapeMailArchives("spark-dev", y, m)
  File "MailingListDataPrep.py", line 41, in scrapeMailArchives
    root = etree.fromstring(r.text.replace('encoding="UTF-8"', ""),
  File "src/lxml/etree.pyx", line 3254, in lxml.etree.fromstring
  File "src/lxml/parser.pxi", line 1913, in lxml.etree._parseMemoryDocument
  File "src/lxml/parser.pxi", line 1793, in lxml.etree._parseDoc
  File "src/lxml/parser.pxi", line 1082, in lxml.etree._BaseParser._parseUnicodeDoc
  File "src/lxml/parser.pxi", line 615, in lxml.etree._ParserContext._handleParseResultDoc
  File "src/lxml/parser.pxi", line 725, in lxml.etree._handleParseResult
  File "src/lxml/parser.pxi", line 654, in lxml.etree._raiseParseError
  File "<string>", line 40
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: link line 32 and head, line 40, column 10
```
