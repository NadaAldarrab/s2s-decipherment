import re
from collections import Counter
import argparse

def tokenizePerLine(input_text):
    input_text = " ".join(input_text.split(" "))
    #transformed_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_text).lower()#.replace(' ', '_')
    #input_text = ' '.join(list(transformed_string))

    def ranked_frequencies(input_list):
        frequency_counter = Counter(input_list)
        ranked_freq_dict = {}
        rank = 1

        for item, frequency in frequency_counter.most_common():
            if item == " " or item == "_":
                continue
            ranked_freq_dict[item] = rank
            rank += 1

        return ranked_freq_dict

    mapping = ranked_frequencies(input_text)
    mapping[" "] = " "
    mapping["_"] = "_"
    mapping[""] = ""

    result = " ".join(str(mapping[i]) for i in input_text.split(" "))
    return result

def tokenize(file_path):
    
    input_file_path = file_path  # Replace with your input file path
    output_file_path = f"{file_path}.tok"  # Replace with your desired output file path

    try:
        with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
            for line in input_file:
                processed_line = tokenizePerLine(line.strip())
                output_file.write(processed_line+"\n")
    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    else:
        print("File processing complete.")
        
def main():
    parser = argparse.ArgumentParser(description='Tokenize data')
    parser.add_argument('file_path', help='path of file that needs to be tokenized')

    args = parser.parse_args()
    tokenize(args.file_path)
    
if __name__ == "__main__":
    main()