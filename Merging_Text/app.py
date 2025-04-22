# Merge multiple .txt files from a folder into a single text file. 
# You’ll use modules like glob and os to locate files and process them programmatically.

import os
import glob

print(glob.glob('./TextFiles/*.txt',recursive=True))