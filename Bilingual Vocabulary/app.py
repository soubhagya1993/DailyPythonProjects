# In this project, you’ll build a bilingual vocabulary tool that allows users to enter word pairs in two languages and 
# save the vocabulary to a CSV file. This is a practical project for learning how to use dictionaries, loops, and 
# CSV file handling in Python.

import csv
Eword = ""

# if Eword == "done":
#     pass
# else:
#     t_word = input(f"Enter the translation of {Eword} in Hindi: ")

#     print(f"{Eword} in English has been added with the translation: {t_word} (Hindi)")

while Eword != "done":
    Eword = input("Enter a word in English (or type 'done' to finish): ")
    t_word = input(f"Enter the translation of {Eword} in Hindi: ")
    print(f"{Eword} in English has been added with the translation: {t_word} (Hindi)")
    data =[
        ["English" , "Hindi"],
        [Eword , t_word]
    ]
    file_name = "file.csv"
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)