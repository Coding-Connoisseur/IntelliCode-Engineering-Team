import os

def generate_structure(directory, output_file):
    with open(output_file, 'w') as outfile:
        # Start from the root directory and traverse
        for root, dirs, files in os.walk(directory):
            # Calculate the relative indentation level based on the root directory
            level = root.replace(directory, '').count(os.sep)
            indent = '    ' * level  # Each level of indentation is 4 spaces

            # Get the folder name and write it to the file
            folder_name = os.path.basename(root) or directory
            outfile.write(f"{indent}{folder_name}/\n")

            # Filter out ignored directories and files
            dirs[:] = [d for d in dirs if not d.startswith('__') and not d.startswith('.') and not d.startswith('z')]
            files = [f for f in files if not f.startswith('.') and not f.startswith('create') and not f.startswith('unpack') and not f.startswith('STRUCTURE')]

            # Write each file in the directory
            for file in files:
                outfile.write(f"{indent}    {file}\n")

if __name__ == "__main__":
    # Set the directory to the current directory
    directory = os.getcwd()
    output_file = "STRUCTURE.txt"
    generate_structure(directory, output_file)
    print(f"The file structure has been saved to {output_file}.")
