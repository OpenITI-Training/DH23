# import the regex library:

## WRITE YOUR SOLUTION ON THE NEXT LINE


# A. LETTERS AND NUMBERS

# 1. Match any digit in the `numbers` variable using
#    the findall function of the regex library
#    and print the result

numbers = "1 5 8 ؜٣؜ ٦ ؜٨ ؜ ٥ ۵"

## WRITE YOUR SOLUTION ON THE NEXT LINE.


# 2. There is usually more than one solution to a problem.
#    Use a different regext to match all digits in the `numbers` variable:

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 3. Match all years in the 18th century: 

years = """
756
1756
1856
156
1777
1878
177"""

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 4. Match all years in the 2nd century

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 5. An OpenITI author URI contains exactly 4 digits
#    followed by a transcripton of the name of the author
#    in CamelCase (without spaces or other non-letter characters).
#    Match only the correct URIs. 

uris = """
310Tabari            # incorrect URI!
0386IbnHawqal
0310al-Tabari        # incorrect URI!
0310.al-Tabari       # incorrect URI!
0255Al_Jahiz         # incorrect URI!
0255Jahiz
0000anonymous        # incorrect URI!
0310الطبري           # incorrect URI!
"""

## WRITE YOUR SOLUTION ON THE NEXT LINE




# B. FUN WITH TABARI



# 1. Open the Tabari text in the DH23/session_3 folder
#    and save it in a variable named "tabari"

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 2. Print the first 2000 characters of the text.

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 3. Observe the printed output. Each OpenITI text has a metadata
#    header. Find out what pattern matches the end of the metadata header.
#    Use the regex.split() function or the <string>.split() method
#    to split the metadata header off from the body of the text
#    NB: remember that to access the first element of a list,
#    you use [0]!
#    Print the first 500 characters of the body to make sure
#    you have correctly removed the metadata header:

## WRITE YOUR SOLUTION TO SPLIT THE HEADER OFF HERE:


## PRINT THE FIRST 500 CHARACTERS OF THE BODY TEXT HERE:
print("First 500 words after splitting the header off:")

# 4. Count the number of Arabic tokens in the text.
#    (use the findall function)

## WRITE YOUR SOLUTION HERE:


# 5. The headings in an OpenITI text all start with three hashes: `###`
#    The hashes are followed by a space,
#    and then one or more pipe `|` characters.
#    If a heading has two pipes, it's a subheading of the previous
#    heading with one pipe.
#    Match all second-level headings (two pipes) in the text
#    (not only the tags but also the title)
#    NB: remember that the pipe is a special character in regular expressions!

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 6. Replace all double line breaks in the text with single line breaks. 

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 7. Match all occurrences of سلام in the text
#    (but make sure you're not matching اسلام)

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 8. Make sure the page numbers all follow the following pattern: PageVxxPxxx           

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 9. Write a regex that matches all persons in al-Ṭabarī
#    whose father's name was Muḥammad. 

## WRITE YOUR SOLUTION ON THE NEXT LINE


# 10. Match all perfect forms of the eighth form (iftaʿala) of the verb manaʿa

## WRITE YOUR SOLUTION ON THE NEXT LINE


