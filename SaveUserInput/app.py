# In this project, you'll write a Python script that asks the user to enter three sentences 
# and saves them into a text file. Between each sentence (except the last), 
# a dashed line will be written to visually separate them.


for n in range(1,4):
    name = input(f"Enter Senetence{n}: ")
    with open("user_sentences.txt", "a") as f:
        f.write(f"{name}\n")
        if n < 3:
            f.write(f"-----------\n")

print("Thanks! Your Data have been saved to user_sentences.txt")
