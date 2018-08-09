## R has five basic/atomic classes of Object
# 1.) Character
# 2.) numeric(real numbers)
# 3.) integer
# 4.) Complex
# 5.) logical/boolean(True/False)

#The most basic object is vector
#A Vector can contains objects of same class
# BUT : the one exception is a list, which is represented as a vector but can contain objects of different classes(indeed,that's usually why we use them)
# Empty vector can be created with vector() function


x<-vector("numeric",10)
x
#Don't use X R is case sensitive

y<-0:6
class(y)
#Output : "integer"

as.numeric(y)
#Output : 0 1 2 3 4 5 6

as.logical(y)
#Output : FALSE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE

as.character(y)
#Output : "0" "1" "2" "3" "4" "5" "6"


x<-list(1,"a",TRUE,1+4i)
x
#Output :
# [[1]]
# [1] 1

# [[2]]
# [1] "a"

# [[3]]
# [1] TRUE

# [[4]]
# [1] 1+4i

x[1]
# [[1]]
# [1] 1


x[[4]]
# [1] 1+4i



#### Matrices ####

m<-matrix(nrow=2,ncol=3)
m
#Output :
# This will create a matrix of row = 2 and column = 3 with NaN values
#       [,1] [,2] [,3]
# [1,]   NA   NA   NA
# [2,]   NA   NA   NA


dim(m)
# Output : [1] 2 3

attributes(m)
# Output : $dim
# [1] 2 3



m<-matrix(1:6,nrow=2,ncol=3)
m

#This will create a matrix of row = 2 and column = 3 and give values to each matrix from 1 to 6

#Output will be
#       [,1] [,2] [,3]
# [1,]   1    2    3
# [2,]   4    5    6


m<- 1:10
dim(m) <- c(2,5)

#Other way of creating a matrix

#       [,1] [,2] [,3] [,4] [,5]
# [1,]    1    3    5    7    9
# [2,]    2    4    6    8   10

x<-1:3
y<-10:12
cbind(x,y) # Matrice creation using binding function

# In binding the objects will work as columns

#        x  y
# [1,]   1 10
# [2,]   2 11
# [3,]   3 12

rbind(x,y)

#in rbinding the objects will work as rows
#    [,1] [,2] [,3]
# x    1    2    3
# y   10   11   12
