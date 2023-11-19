import argparse

def truncateData(file_path, line_length=64):
    # Initialize the desired line length
    # Open the input file for reading
    with open(file_path, 'r') as input_file:
        # Open a new file for writing the filtered content
        with open(f'{file_path}_trimmed{line_length}', 'w') as output_file:
            # Read and process each line in the input file
            for line in input_file:
                if line == '\n':
                    continue
                # Remove whitespace characters from the line
                line_without_spaces = line.replace(' ', '')

                # Check if the line without spaces is less than or equal to 64 characters
                if len(line_without_spaces) <= line_length:
                    # If the modified line is within the desired length, write it to the output file
                    output_file.write(line)
                else:
                    # If the modified line is longer, trim it to the desired line length and then write it
                    truncated_line = ' '.join(line_without_spaces[:line_length]) + '\n'
                    output_file.write(truncated_line)
                    
                    
def main():
    parser = argparse.ArgumentParser(description='Truncate lines in file')
    parser.add_argument('file_path', help='path of file that needs to be truncated')
    parser.add_argument('word_length', type=int, help='The desired word length.')

    args = parser.parse_args()
    truncateData(args.file_path, args.word_length)
    
if __name__ == "__main__":
    main()