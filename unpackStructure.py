import os

def create_structure_from_file(file_path):
    with open(file_path, 'r') as file:
        root_directory = None
        current_path = []
        
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Determine the indentation level (each level is 4 spaces)
            indent_level = (len(line) - len(line.lstrip(' '))) // 4
            name = line.strip()
            
            # Handle root directory
            if indent_level == 0:
                root_directory = name.rstrip('/\\')
                os.makedirs(root_directory, exist_ok=True)
                current_path = [root_directory]
            else:
                # Update the current path to the correct depth
                current_path = current_path[:indent_level]
                
                # Determine if it's a file or directory (directories end with '/')
                if name.endswith('/'):
                    dir_path = os.path.join(*current_path, name.rstrip('/'))
                    os.makedirs(dir_path, exist_ok=True)
                    current_path.append(name.rstrip('/'))
                else:
                    file_path = os.path.join(*current_path, name)
                    # Create an empty file
                    with open(file_path, 'w') as f:
                        pass

if __name__ == "__main__":
    # Specify the path to your file structure definition
    input_file = "structure.txt"  # Replace with the path to your input file
    create_structure_from_file(input_file)
    print("File structure created successfully.")
