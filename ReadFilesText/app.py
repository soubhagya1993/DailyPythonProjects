# Task - use regular expressions and file handling in Python to extract the first sentence from every .txt file in a directory


import os
import re
# print(os.listdir("TxtFiles"))

file_dir = "TxtFiles"

try:
    for file_name in os.listdir(file_dir):
        file_path = os.path.join(file_dir, file_name)       # Combine directory path and filename        
        
        with open(file_path,"r") as f:
            text = f.read()
            pattern = r"(.*[.])"                            # Matches up to the first ., !, or ?
            match = re.search(pattern, text)
            first_sentence = match.group(1)
            print(first_sentence)

except Exception as e:
    print(e)
