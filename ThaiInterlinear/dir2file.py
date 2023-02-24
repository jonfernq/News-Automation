import os

def concatenate_files(directory_path):
    # Create an empty string to hold the concatenated contents of all files
    concatenated_contents = ""

    # Iterate over all files in the directory
    for file_name in os.listdir(directory_path):
        # Only read in text files
        if file_name.endswith(".txt"):
            # Read in the contents of the file and concatenate to the string
            with open(os.path.join(directory_path, file_name), 'r', encoding='utf-8') as f:
                concatenated_contents += f.read()

    # Write out the concatenated string to a summary file with the name of the directory
    summary_file_name = os.path.basename(directory_path) + "_summary.txt"
    with open(os.path.join(directory_path, summary_file_name), 'w', encoding='utf-8') as f:
        f.write(concatenated_contents)
        
concatenate_files("./thainews")         
