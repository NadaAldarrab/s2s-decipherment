import argparse
import string

def preprocessData(file_path, line_length=64):
    # Open the input file for reading
    with open(file_path, 'r') as input_file:
        # Open a new file for writing the filtered content
        with open(f'{file_path}_trimmed{line_length}', 'w') as output_file:
            # Read and process each line in the input file
            for line in input_file:
                if line == '\n':
                    continue
                # Make characters to lowercases
                line = line.lower()
                # Strip punctuations and leading/trailing whitespaces
                translation_table = str.maketrans("", "", string.punctuation)
                stripped_line = line.translate(translation_table).strip()
                # Change whitespace to underscore
                line_with_underscores = stripped_line.replace(' ', '_')

                # Check if the line with underscores is less than or equal to 64 characters
                if len(line_with_underscores) <= line_length:
                    # If the modified line is within the desired length, write it to the output file
                    processed_line = ' '.join(line_with_underscores) + '\n'
                    # Write line to file
                    output_file.write(processed_line)
                else:
                    # If the modified line is longer, trim it to the desired line length and then write it
                    processed_line = ' '.join(line_with_underscores[:line_length]) + '\n'
                    # Write line to file
                    output_file.write(processed_line)

def main():
    parser = argparse.ArgumentParser(description='Preprocess data by modifying data into lowercase, stripping punctuation, and changing whitespaces into underscores')
    parser.add_argument('input_path', help='Path of file that needs to be processed')
    parser.add_argument('output_path', help='Path of file after processed')

    args = parser.parse_args()
    preprocessData(args.input_path, args.output_path)
    
if __name__ == "__main__":
    main()