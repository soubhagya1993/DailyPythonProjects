import time

usertime = int(input("Enter a starting number(e.g., 10): "))
while usertime < 0:
    print("Please enter a positive integer.")
    usertime = int(input("Enter a starting number(e.g., 10): "))

usermsg = input("Enter your final message: ")

for n in range(usertime+1,1,-1):
    print(n - 1)
    time.sleep(1)
print(usermsg)