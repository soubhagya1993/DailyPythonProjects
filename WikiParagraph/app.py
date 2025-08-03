# try writing a script that fetches a Wikipedia page and extracts its first few paragraphs.
# Write a Python script that:
# Sends a request to a Wikipedia article URL
# Parses the HTML content
# Extracts the first four paragraphs

import requests
from bs4 import BeautifulSoup

# f = open("wiki.txt","r")
# for i in range(4):
#     data = f.readline()
#     print(data)



# Specify the Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)

extracted_paragraphs = []
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    
    for p in paragraphs:
        text = p.text.strip()                        # Remove extra spaces
        if text:                                     # Ensure it's not empty
            extracted_paragraphs.append(text)
        if len(extracted_paragraphs) == 4:           # Stop after collecting 4 paragraphs
            break
    
    f = open("wiki.txt","w")

    for item in extracted_paragraphs:
        f.write(item + "\n")


