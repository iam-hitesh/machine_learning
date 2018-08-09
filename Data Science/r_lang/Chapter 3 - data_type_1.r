# Data Types Continues

#Factors : Factors are used to represent categorical data. Factors can be unordered or ordered. One can think of a factor as an
# integer vector where each integer has label.

# Factors are treated specially by modelling functions like lm() and glm()


x<-factor(c('yes','yes','no','yes','no'))
x
# Output : yes yes no  yes no 
# Levels: no yes

table(x)
x
#Output : x
#  no yes 
#  2   3 

unclass(x)
##  [1] 2 2 1 2 1
##  attr(,"levels")
##  [1] "no"  "yes"


# Missing Values
# is.na() is used to test objects if they are NA
# is.nan() is used to test for NaN
# A NaN value is NA but converse is not true


### DATA FRAMES
# Data frames are used to tabular data
# Data frames also have special attributes called row.names
# Data frames are usually created by calling read.table() or read.csv()
# Can be converted to a matrix by calling data.matrix()

#coerced

 y <- data.frame(foo = 1:4,bar=c(T,T,F,F))
 y
 nrow(y)
 ncol(y)
 
 #Output : 
#    foo   bar
# 1   1  TRUE
# 2   2  TRUE
# 3   3 FALSE
# 4   4 FALSE

#[1] 4 - 4 Numbers of rows
#[1] 2 - 2 Numbers of columns


#Names in R

names(x)
#Output : NULL

names(x)<- c("foo","bar","norf")
x

#Output 
#  foo  bar norf 
#   1    2    3 

names(x)
#Output : [1] "foo"  "bar"  "norf" 


x <- list(a=1,b=2,c=3)
x

# Output :
# $a
# [1] 1
# $b
# [1] 2
# $c
# [1] 3



m <- matrix(1:4,nrow=2,ncol=2)
dimnames <- list(c("a","b"),c("c","d"))
m

# Output :

#    c d
#  a 1 3
#  b 2 4



# What we learn about Data Types
# Atomic Classes: numeric,logical,character,integer,complex
# vectors,lists
# Factors,matrices
# missing values
# Data frames
# names 

