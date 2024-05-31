import os

def remove_spaces_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    modified_lines = [line.replace(' ', '') for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

    print(f"Spaces removed and saved to {output_file}")

if __name__ == "__main__":
    input_file = "labelmap.txt"  # Replace with your input file name
    output_file = "labelmap.txt"  # Replace with your desired output file name
    
    # Call the function to remove spaces from the input file and save to output file
    remove_spaces_from_file(input_file, output_file)
