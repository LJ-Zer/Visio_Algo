import os

input_folder = 'ground-truth'
output_folder = 'ground-truth'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each .txt file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(input_folder, filename), 'r') as infile:
            # Read each line and split it into name and numbers
            lines = [line.strip().split() for line in infile]

        # Modify the name by removing spaces
        modified_lines = [''.join(parts[:-4]).replace(' ', '') + ' ' + ' '.join(parts[-4:]) for parts in lines]

        # Write the modified lines to a new file in the output folder
        output_filename = os.path.join(output_folder, filename)
        with open(output_filename, 'w') as outfile:
            outfile.write('\n'.join(modified_lines))

        print(f'{filename} processed and saved to {output_filename}')
