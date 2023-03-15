# Dictionary exercise:


#---------------------------------------------------------------------


my_book = {"author": "Jonathan Coe", "title": "The Rotters' Club"}


# print the title of the book in the `my_book` dictionary:



#---------------------------------------------------------------------


# create a dictionary that contains two keys: "first_name" and "last_name";
# give your own first and last name as the value.
# Assign it to the variable `my_name`: 



# print your first name, using the dictionary
# (remember that you access a key's value using square brackets!)



# create a second dictionary, `other_name` that contains the same keys
# but has the first and last name of your neighbour as values:



# print your neighbour's last name using that dictionary:



# Create a third dictionary, `my_class`, that contains two keys:
# your own first name, and that of your neighbour;
# the values of these keys are the two dictionaries you created above



# print the dictionary



# print the last name of your neighbour, using the `my_class` dictionary



# add another item to the `my_class` dictionary:
# its key is the name of another student in class,
# its value a dictionary with that other student's first and last name
# NB: to add a new item to a dictionary, use the square brackets, like this:
# my_dict["new key"]  = "new value"


# print the last name of that other student, using the `my_class` dictionary:



# loop through the `my class` dictionary and print the first name of each student:



# loop through the `my class` dictionary and print the **last** name of each student:



#---------------------------------------------------------------------


coe = {
    "first name": "Jonathan",
    "last name": "Coe",
    "books": [
        {
            "title": "The Closed Circle",
            "publisher": "Viking Press",
            "year": 2004
        },
        {
            "title": "Middle England",
            "publisher": "Viking Press",
            "year": 2018
        }
    ]
}

# print the list of books by Jonathan Coe:



# print the data for Jonathan Coe's first book:



# print the publication year of the second book by Jonathan Coe:


#---------------------------------------------------------------------


s = "This is a test string. Test test test! This is the end of the text."

# tokenize the string `s` and assign the list of tokens to a variable `tokens`:

import regex
tokens = regex.findall("\w+", s)

# we import the `Counter` class from the inbuilt Python library `collections`;
# this counts the number of times each token is in a string
# and stores this in a dictionary-like object

from collections import Counter

token_count = Counter(tokens)

# print the token count:
print(token_count)



# print the frequency of the token "This":
print(token_count["This"])


# print the frequency of the token "test":



# Let's build our own counter:
# First, we create a new dictionary that starts with count 0 for
# each item in the tokens list:

my_token_count = dict.fromkeys(tokens, 0)
print(my_token_count)

