###############################
#                             #
# APIs, JSON and DICTIONARIES #
#                             #
###############################

# In this exercise, we're going to use the quran.com API to
# get the text of a Quran verse.

# You may have to review the lesson on downloading to be able to do this
# (unless you have created a great cheat sheet of course!)

# We're going to need the `requests` library to download data from the API;
# Import it here:



# We'll also need to import the `json` library to convert the
# server's json response (which is a string) into a Python dictionary.
# This library is built-in in Python, so we don't have to install it using pip.
# Import the json library here:



# The API allows us to download the Quran texts in different styles;
# Uthmani (as it is in printed Qurans, with full voweling and other symbols);
# Imlaei (simplified voweling and symbols); Indopak (Pakistani style).
# Each of the styles has its own "endpoint" (URL to which you send the request):
# https://api.quran.com/api/v4/quran/verses/uthmani
# https://api.quran.com/api/v4/quran/verses/imlaei
# https://api.quran.com/api/v4/quran/verses/indopak

# Send a request to the uthmani endpoint using the request library's `get` function
# and store the response in a variable called `r`:



# Remember how we got the downloaded text from the response object?
# We used its `text` attribute.
# Print the first 500 characters of `r.text` to get an idea of
# what we downloaded:



# describe in words what you see:

#
#

# The response from the API is a JSON string.
# We can use the `json` library's `loads` (the "s" stands for "string") function
# to convert the json string into a Python dictionary.
# Like this: json.loads("{'sample_key': 'sample_value'}")

# Convert the text attribute of the API response to a dictionary and
# assign that to a variable called "quran_d" ("d" for "dictionary"):



# To understand what our quran_d contains, we can print its keys.
# Use a loop to print all keys in the dictionary:




# Now, let's print for each key in the dictionary not only its name
# but also the number of items in it.
# If you don't remember, google "Python count the number of items"
# (and update your cheat sheet!)
# Write the same loop as above, but now print not only the key,
# but also the length of the value of that key in the dictionary:




# the quran_d dictionary has two keys: "verses" and "meta".
# As we could see from our initial printout of the first 500 characters
# of the API response, the value of the "verses" key is a list of dictionaries,
# one dictionary for each verse.
# Assign the list of verses to a new variable called "verses":



# Print the dictionary for the first verse:



# Print the text of the last verse:
# (remember how to access the last element of a list? If not, google it!)



# Note that each verse dictionary contains a key called "verse_key";
# it consists of two numbers, separated by a colon.
# The first number is the sura number, the second the aya number.

# Since `verses` is a list, it's not easy to access a specific verse
# (say, sura 12 verse 3): we don't know the position of that verse in the list.

# APIs usually allow filtering the results you receive from the API
# using parameters in query strings.
# These query strings are attached at the end of the endpoint URL,
# separated from it by a question mark. Like this: api.example.com?id=5
# Multiple parameters are separated by an ampersand: api.example.com?text=door&date=2022

# The quran.com API also allows this. A few examples
# (see the documentation of the API:
# https://quran.api-docs.io/v4/quran/get-uthmani-script-of-ayah-2):
#
# https://api.quran.com/api/v4/quran/verses/uthmani?chapter_number=5
# -> this will return only the verses from the fifth sura
#
# https://api.quran.com/api/v4/quran/verses/uthmani?page_number=25
# -> this will return the verses on page 25 of the Madani Mushaf



# We can use the verse_key item that we found in each verse dictionary
# as a query parameter to the API call (see the documentation of the API:
# https://quran.api-docs.io/v4/quran/get-uthmani-script-of-ayah-2 ;
# you'll have to expand the list of "Query string" options to see it)

# Make a new call to the API using the request library's `get` function.
# Add a query string to the endpoint URL we used before
# and use the verse_key as a parameter in it
# to download only the text of sura 12 verse 3:



# Print the content of the request to check if it worked:



# Take a look at the documentation of the quran.com API
# and try to do the following:

# download the Imlaei script version of only the verses of the 12th juz of the Quran:




# download a list of all available translations of the Quran:





# Download the Chinese translation of the first sura of the Quran
# (the Chinese translation has translation_id 56)
