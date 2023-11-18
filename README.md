# s2s-decipherment

This repository contains the Project Gutenberg data that we used in [our paper](https://aclanthology.org/2021.acl-long.561/). It also contains code to reproduce the results in the paper.


# Data Processing Pipeline
## 1. dataLoader.py

### Description

`dataLoader.py` is responsible for loading the data that is intended to be processed. It ensures that the required data is available for subsequent steps in the pipeline.

### Usage

```bash
python dataLoader.py 
```
## 2. truncateData.py

### Description

`truncateData.py` truncates the loaded data to a desired length, a useful step when dealing with large datasets and you want to work with a subset of the data.
### Usage

```bash
python truncateData.py file_path word_length
```
## 3. preprocessData.py

### Description

`preprocessData.py` preprocesses the truncated data to lowercases, stripes punctuations, change whitespaces into underscores, and modifies text into character level, which are the necessary preprocesses to run a character level transformer model.
### Usage

```bash
python preprocessData.py input_path output_path
```
## 4. dataTokenizer.py

### Description

`Tokenizer.py` tokenizes a given file, breaking it down into its constituent tokens. It is especially useful for natural language processing tasks where tokenized input is required.

### Usage

```bash
python Tokenizer.py file_path
```


# Data Evaluation

### Description

`evaluation.py` evaluates the performance of model based on ter score
### Usage

```bash
python evaluation.py decipher_path plain_text_path
```