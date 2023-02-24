import os

def apply_function_to_files_in_directory(directory_path, function):
    for file_name in os.listdir(directory_path):
        if not os.path.isfile(os.path.join(directory_path, file_name)):
            continue

        # Read in the contents of the file as a string
        with open(os.path.join(directory_path, file_name), 'r', encoding='utf-8') as f:
            file_contents = f.read()

        # Apply the function to the file contents
        processed_contents = function(file_contents)

        # Write out the processed contents to a new file with the prefix "il_"
        new_file_name = f'il_{file_name}'
        with open(os.path.join(directory_path, new_file_name), 'w', encoding='utf-8') as f:
            f.write(processed_contents)

import pythainlp, sys 
from pythainlp.corpus import wordnet

def make_interlinear(txt):
    words = pythainlp.word_tokenize(txt)

    iltxt = ""
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            definition = synsets[0].definition()
            iltxt = iltxt + f"{word} ({definition}) "
        else:
            iltxt = iltxt + word + ' ' 
    return iltxt 
		

function = make_interlinear
directory_path = "D:\\GITHUB_MY\\NEWSAUTOMATION\\thainews"
apply_function_to_files_in_directory(directory_path, function)


"""
This function takes two arguments: directory_path, which is a string representing the path to the directory containing the files to be processed, and function, which is a function that will be applied to the contents of each file.

The function first iterates over all files in the specified directory using os.listdir(), skipping any subdirectories that might be present. For each file, it opens the file using open() and reads its contents into a string.

Next, the function applies the provided function to the file contents using function(file_contents) and stores the result in the processed_contents variable.

Finally, the function writes the processed contents to a new file with the prefix "il_" added to the original filename. It uses open() again to create the new file, writes the processed contents using write(), and then closes the file.

Note that this code assumes that the input files are encoded in UTF-8 and will also encode the output files in UTF-8.

"""

