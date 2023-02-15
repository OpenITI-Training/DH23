# session recap

# load the regex library here:


s = """
This is a sample text.
It contains more than 10 words.
بالعربية وبالانكليزية
ألف باء 23 555555
"""

# print all words and numbers in the string s:


# print only the numbers in the string s, each on a separate line:


# print only the English words in the string s, each on a separate line:


# print only the Arabic words in the string s, each on a separate line:
# (NB: Google the Unicode Arabic Block to find out
# what the first and last letters are in Unicode)


# print only the capitalized words in the string s, each on a separate line:



# match the pdf file names in this piece of html:

html = """
<table>
<tbody>
<tr><td><a href="10FF80.pdf">10FF80.pdf</a></td><td align="right"> 29K</td></tr>
<tr><td><a href="ErrorLink.pdf">ErrorLink.pdf</a></td><td align="right"> 32K</td></tr>
<tr><td><a href="Readme.txt">Readme.txt</a></td><td align="right"> 91 </td></tr>
<tr><td><a href="U0A00.pdf">U0A00.pdf</a></td><td align="right">119K</td></tr>
<tr><td><a href="U0A80.pdf">U0A80.pdf</a></td><td align="right">122K</td></tr>
<tr><td><a href="U0B00.pdf">U0B00.pdf</a></td><td align="right">127K</td></tr>
</tbody>
</table>
"""

# Match the lines starting with an asterisk: *

starstudded = """
Do not match this line
Do not match this line either
* Please match this one
* this one too!
Definitely* don't match this one!
"""


