# In this class, we're going to learn how to draw graphs
# using plotly express
# AND we're going to learn how to teach ourselves to do this

##########
# STEP 1 #
##########

# Find online how to install plotly express; now, install it on your computer

##########
# STEP 2 #
##########

# Find a tutorial for Plotly Express online and follow it
# until you learn how to draw your first graph
# (using the data provided in the tutorial).
# Once you manage to draw your first graph,
# abandon the tutorial and move to step 3.
# Write the code here (don't copy it, type it!)







# All plotly express plots are basically built in the same way. 


##########
# STEP 3 #
##########

# Search online how to create a bar graph in plotly express.
# First, use the same data as in the instructions you found
# to draw your first bar chart: (write your code here):






# Now, create a bar chart with the following data
# to visualize the number of words in the works of three authors








# once the graph is displayed, try printing the variable that contains the graph
# (this is conventionally called `fig`) to see what it contains:





##########
# STEP 4 #
##########

# In order for others to understand your graphs, it's important
# to guide the reader by providing a title for your graphs
# and useful labels to the X and Y axes.
# Search online how you can add a title to a graph in plotly express.







# (as often, there is more than one way to do this;
# fig.update_layout() allows you to change many layout features of your graph






##########
# STEP 5 #
##########

# search how you can save a plotly express file as a png (image) file,
# and store your last graph as a png file:




##########
# STEP 6 #
##########

# Let's put this into practice for some real research questions.
# The OpenITI corpus contains more than 10.000 Islamicate texts
# (currently almost all in Arabic, but soon also in other Islamicate languages).
# They date from the first Islamic century to today,
# and range from very short texts (less than 100 words)
# until multivolume giants of millions of words.
# The entire corpus contains more than 2 billion words. 
# To wrap our heads around the contents of the corpus, we often use data visualization. In this exercise, we’ll focus on two questions: 
# 1. How are books distributed in the corpus across time?
# 2. How does the length of books vary across the corpus?

# We’ll be using a slimmed down version of the OpenITI metadata
# that includes only the primary version of each book
# (the corpus contains several secondary versions,
# e.g., different editions, of some books).
# The metadata is in a tsv file in the the DH23/session_10 folder
# (you'll have to pull the changes from GitHub)

# Use the pandas library to load the tsv file and assign it to a variable `df`.
# Use your cheat sheet (or Google) to remind yourself of how we did that




# After loading the tsv file, print the dataframe:



###########
# STEP 6b #
###########

# A first step when working with a new dataset is
# understanding what each column and each row represents. 
# Use the command print(df.info()):




# Take a look at the output and think about the following questions: 
# 1. What does each row in the data represent?
#    (in statistics, a row in a dataset is called an “observation”)
#
# 2. What are the names of the columns? Describe in your own words
#    which data you think each column contains.
#   (in statistics, a column in a dataset is called a “variable”)
# 3. What type of data do you think each column contains
#    (categorical, discrete, continuous)?


###########
# STEP 6c #
###########

# Let's try to graph the distribution of texts in the corpus over time;
# that is: we want to see whether the corpus has more texts
# for some periods than others.

# Which variable (column) would you use for this?

# Use the graph selection aid on https://www.data-to-viz.com/
# to find out which graphs are considered most suitable
# for this situation, where you have one numeric variable
# you want to represent (click the graph types to see
# some explanations); then search the internet for
# how you create that kind of graph using plotly express.









###########
# STEP 6d #
###########

# If you used a histogram, that's great. If you didn't,
# search how to create a histogram to display the distribution
# of texts over time and write the code here:







# Now adapt the code you wrote above to visualize
# the distribution over 25-year periods
# (that is, you'll need to make sure that the bins
# (represented in the graph by bars) cover about 25 years):





# What does this tell you about the distribution of OpenITI texts?
# Is there a difference in the interpretation when you use
# 25-year periods instead of centuries?



