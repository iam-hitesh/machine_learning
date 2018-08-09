# Reading Tabular Data
# There are few principle functions reading data into R
# 1.) read.table , read.csv for reading tabular data
# 2.) readLines, for reading lines of text files
# 3.) source, for reading R code files (inverse of dump)
# 4.) dget, for reading in R code files (inverse of dput)
# 5.) load, for reading in saved workspaces
# 6.) unserialize, for reading single R objects in binary form
 
# read.table() is an important function and most commonly used function for reading table data. It has few arguments
# 1.) file - Then name of file or a connection
# 2.) header - the logical indicating if the file has a header line
# 3.) sep - a string indicating how the columns are separated.
# 4.) colClasses - A character vector indicating the class of each column in the dataset.
# 5.) nrows - The number of rows in the dataset.
# 6.) comment.char - A character string indicating the comment character.
# 7.) skip - Number of lines to skip from beginnning
# 8.) stringsAsFactors - should character variables be coded as factors.
