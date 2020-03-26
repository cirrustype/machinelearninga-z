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

dataset








