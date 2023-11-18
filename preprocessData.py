import argparse
import string

def preprocessData(input_path, output_path):
    # Open the input file for reading
    with open(input_path, 'r') as input_file:
        # Open a new file for writing the filtered content
        with open(output_path, 'w') as output_file:
            # Read and process each line in the input file
            for line in input_file:
                if line == '\n':
                    continue
                # Make characters to lowercases
                line = line.lower()
                # Strip punctuations
                translation_table = str.maketrans("", "", string.punctuation)
                stripped_line = line.translate(translation_table).strip()
                # Change whitespace to underscore
                processed_line = stripped_line.replace(' ', '_')
                # Separacter characters with whitespace
                output_line = ' '.join(processed_line) + '\n'
                # Write line to file
                output_file.write(output_line)

def main():
    parser = argparse.ArgumentParser(description='Preprocess data by modifying data into lowercase, stripping punctuation, and changing whitespaces into underscores')
    parser.add_argument('input_path', help='Path of file that needs to be processed')
    parser.add_argument('output_path', help='Path of file after processed')

    args = parser.parse_args()
    preprocessData(args.input_path, args.output_path)
    
if __name__ == "__main__":
    main()