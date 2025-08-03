# In this project, you’ll build a simple note-taking application that 
# saves user input into a file named with the current date. This is a 
# 
# great way to practice working with dates, file handling, and user input in Python.

# from datetime import date

# today_date = date.today()
# file_name = f"{today_date}.txt"

# print("Enter your Notes for Today. type 'exit' to save and exit")

# user_txt = input("Enter your Note: ")

# for text in user_txt:
#     with open(file_name , "a") as f:
#         f.write(user_txt)
#         if user_txt == "exit":
#             f.close()


import datetime

# Get today's date
today_date = datetime.datetime.today().strftime('%Y-%m-%d')
file_name = f"{today_date}.txt"

print("Enter notes line by line. Type 'exit' to stop.")

notes = []
while True:
    line = input()
    if line.lower() == "exit":  # Stop input when 'exit' is typed
        break
    notes.append(line)

# Save input to the file
with open(file_name, "w") as file:
    file.write("\n".join(notes))

print(f"Your notes have been saved to {file_name}")