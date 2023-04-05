import os
import re
import plotly.express as px

# aim: count the number of times a word is used in all documents in a folder.

# 1. create empty lists in which we are going to store the document names and the word counts
text_files = []
counts = []

# go through all the items in the folder:
folder = "."
for item in os.listdir(folder):
    # check if the item is a text file:
    if item.endswith("txt"):
        # construct the path to the text file:
        path = os.path.join(folder, item)
        # load the text file:
        with open(path, encoding="utf8") as file:
            text = file.read()
        # store the file name in the text_files list:
        text_files.append(item)
        # count the number of times the word "test" is in this file:
        word_count = len(re.findall("test", text))
        # store the word count in the counts list:
        counts.append(word_count)

# Visualize the results:
fig = px.bar(y=text_files, x=counts)
fig.show()
