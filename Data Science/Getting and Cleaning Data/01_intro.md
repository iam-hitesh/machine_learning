Raw Data -> Processing Script -> Tidy Data -> Data Analysis -> Data Communication


Raw Data to Processed Data is the First Step

Get Data from https://data.baltimorecity.gov

Important Commands for Data Processing

getwd() // for Getting working directory

set("/Desktop/") // For setting other working directory


## For creating a file

if(!file.exists("data")){
    dir.create("data")
}

## For Downloading a File from Internet

download.file(fileURL,destFile,method)


fileURL <- "https://data.baltimorecity.gov/api/views/aqgr-xx9h/rows.csv?accessType=DOWNLOAD"
download.file(fileURL,'data/camera.csv',method="curl")


### Now read the local file using read.table()
This is little bit slower as it takes a lot of parameters and working on RAM so can cause problem on Big data
Other Options are read.csv() or read.csv2()

cameraData <- read.table("data/speed.csv") #Will not work

cameraData <- read.table('data/speed.csv',sep=",",header=TRUE)
head(cameraData)


## For Reading Excel Files
library(xlsx)
camData <- read.xlsx('data/speed_excel.xlsx',sheetIndex=1,header=TRUE)
head(camData)

colIndex <- 2:3
rowIndex <- 1:4
camData <- read.xlsx('data/speed_excel.xlsx',sheetIndex=1,colIndex=colIndex,rowIndex=rowIndex)

### write.xlsx() for writing Excel file
### xlsx2, XLConnect are other better options

