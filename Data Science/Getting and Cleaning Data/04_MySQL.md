# Database (MySQL) 

* Free and widely used open source database software
* Widely used in internet based applications
* Data are structured in 
  * Databases
  * Tables within databases
  * Fields within tables
  * Each row is called a record


Install dbConnect before using these functions and use library(dbConnect)

ucscDb <- dbConnect(MySQL(),user='genome',host='genome-mysql.cse.ucsc.edu')
result <- dbGetQuery(ucscDb,"Show Database:");
dbDisconnect(ucscDb)
