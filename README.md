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

`truncateData.py` truncates the loaded data to a desired length (Default = 64 characters), a useful step when dealing with large datasets and you want to work with a subset of the data. Onlu use this on preprocessed text (Character-level and underscore separated).
### Usage

```bash
python truncateData.py file_path word_length
```
## 3. preprocessData.py

### Description

`preprocessData.py` truncates the loaded data to a desired length (Default = 64 characters), processes all characters to lowercases, stripes punctuations, changes whitespaces into underscores, and modifies text into character level, which are the necessary preprocesses to run a character level transformer model. Only use this on unpreprocessed text.
### Usage

```bash
python preprocessData.py file_path
```
or with customized word length
```bash
python preprocessData.py file_path word_length
```
## 4. dataTokenizer.py

### Description

`Tokenizer.py` tokenizes a given file, breaking it down into its constituent tokens. It is especially useful for natural language processing tasks where tokenized input is required.

### Usage

```bash
python Tokenizer.py file_path
```

# Model Training

### Set Up
Run setUp.sh to create configuration file for training, run modifyConfig.py to change parameters as needed.

### Training
Run the following command in terminal to start training:
```bash
rtg-pipe 01-tfm-deen --gpu-only
```

### Decoding
After model is trained, run the following command to perform decoding on extra test sets:
```bash
rtg-decode 01-tfm-deen -if [input_file_path] -of [output_file_path]
```



# Data Evaluation

### Description

`evaluation.py` evaluates the performance of model based on ter score
### Usage

```bash
python evaluation.py decipher_path plain_text_path
```
