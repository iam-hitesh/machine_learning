# JSON Files

### About json

* Javascript Object Notation
* Lightweight data storage
* Common format for data from application programming interfaces (APIs)
* Similar structure to XML but different syntax/format
* Data stored as
  * Numbers (double)
  * Strings (double quoted)
  * Boolean (true or false)
  * Array (ordered, comma separated enclosed in square brackets [])
  * Object (unorderd, comma separated collection of key:value pairs in curley brackets {})

[http://en.wikipedia.org/wiki/JSON](http://en.wikipedia.org/wiki/JSON)




library(jsonlite)

jsonData <- fromJSON('https://api.github.com/users/ihiteish/repos')

names(jsonData)
names(jsonData$owner)
jsonData$owner$login
myjson <- toJSON(iris,pretty=TRUE)
cat(myjson)


# Using data.table


* Inherets from data.frame
* All functions that accept data.frame work on data.table
* Written in C so it is much faster
* Much, much faster at subsetting, group, and updating


# data.table

library(data.table)

DF = data.frame(x=rnorm(9),y=rep(c(&quot;a&quot;,&quot;b&quot;,&quot;c&quot;),each=3),z=rnorm(9))

head(DF,3)


       x y        z
1 0.4159 a -0.05855
2 0.8433 a  0.13732
3 1.0585 a  2.16448
