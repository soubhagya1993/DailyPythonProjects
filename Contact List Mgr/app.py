
while True:
    name = input("Enter Your Name (or type 'done' to finish): ")
    if name == "done":
        break
    else:
        ph = input("Enter Phone Number: ")
        f = open("file.txt","a")
        f.write(f"\n{name} : {ph}")
    f.close()