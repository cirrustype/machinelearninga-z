#section 2, part 1: Data Preprocessing 

#importing the dataset 
dataset = read.csv('Data.csv')
dataset

#imputing missing data
dataset$Age =ifelse(is.na(dataset$Age),
                    ave(dataset$Age, FUN = function(x)
                      mean(x, na.rm = TRUE)), 
                    dataset$Age)

dataset$Salary =ifelse(is.na(dataset$Salary),
                    ave(dataset$Salary, FUN = function(x)
                      mean(x, na.rm = TRUE)), 
                    dataset$Salary)

#encoding cat var

#x

dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3))
#y
dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0,1))






