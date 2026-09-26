---
title: "Introduction to R for Stata Users"
author: "Diego Martin"
date: 2022-08-31
description: "First steps to move from Stata to R."
categories: ["General"]
image: images/0966f0_34dcfa5bc3e34ffd8c29396b098af976.webp
wix-url: https://www.datainsightonline.com/post/introduction-to-r-for-stata-users
---
**Let's set the software**

**R** is a programming environment

- Robert Gentleman and Ross Ihaka developed **R** at the University of Auckland, New Zealand in 1996.
- They designed the language to combine the strengths of two existing languages, S and Scheme.
- Tools are distributed as packages, which any user can download to customize the R environment.

https://cran.r-project.org/

- Free Software.

**RStudio** is a better view (Similar to Stata). Problematic with an extensive database.

https://www.rstudio.com/products/rstudio/download/

**Data Type**

1. Vector

**Definition:**  A vector is asequence of elements that share the same data type. A vector supports logical, integer, double, character, complex, or raw data [types](https://www.tutorialspoint.com/r/r_vectors.htm).

**Example code**

```python
#Generating scalar
x<-2

#Generating a vector
x1 <- c(1,2,3)
x2 <- c(1,2,5.3,6,-2,4) # numeric vector
x3<- c("one","two","three") # character vector
x4 <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #logical vector
x2
x2[c(2,4)] # 2nd and 4th elements of vector
```

Operations with vectors

- x[c(posituin1, position)] subsetting
- vectors rep(a, repetitions)
- seq(from =,to =,by =)
- a : b patterned Vectors

Exercise 1 - Practice with vectors

Let's put in practice what we learn from vectors.

1 Generate the next vector: x= (1.8 3.14 4 88.169 13)

2 Multiple the vector x by 2 and add 3.

3 Generate a vector x1 equal to multiple the first component of x by 5, the second by 4 until the fifth by 1.

4 Generate a vector x2 equal to add the first component of x 1, the second by 2 until the fifth by 5.

5 Replace x equal to x=x1\*x+x2.

6 How can do the last three steps in on line?

Suggested solution - 1 (Try yourself first)

**Example code:**

```python
#1)
x <- c(1.8, 3.14, 4, 88.169, 13)
length(x)
#2)
2*x + 3
#3)
x1<-c(5:1)
x1
#4)
x2<-c(1:5)
x2
#5)
x<-x1*x+x2
#6)
x <- c(1.8, 3.14, 4, 88.169, 13)
5:1*x + 1:5
```

2. Matrix

**Definition:** Matrices are the **R** objects in which the elements are arranged in a two-dimensional rectangular [layout](https://www.tutorialspoint.com/r/r_matrices.htm).

**Example code**

```python
# Generating a Matrix
A <- matrix(c(1,2,3,4),2,2)
B <- matrix(c(1,2,3,4,5,6),3,2, byrow=TRUE)
B
C <- matrix(c(1,2,3,4,5,6),3,2, byrow=FALSE)
C
# generates 5 x 4 numeric matrix
y<-matrix(1:20, nrow=5,ncol=4)
y
# another example
cells <- c(1,26,24,68)
rnames <- c("R1", "R2")
cnames <- c("C1", "C2")
mymatrix <- matrix(cells, nrow=2, ncol=2, byrow=TRUE,
dimnames=list(rnames, cnames))
mymatrix

# Identify rows, columns or elements using subscripts.
z<-matrix(1:12, nrow=3,ncol=4)
z
z[,4] # 4th column of matrix
z[3,] # 3rd row of matrix
z[1:2,3:4] # rows 2,3,4 of columns 1,2,3

# Diagonal Matrix
D <- diag(c(1,2,3,4))
diag(D)
I <- diag(4) #identity 4th order

diag # the function without parenthesis shows the source code
```

Operation and properties for vectors

- matrix(i : j, nrow = 2)
- t(A) transposed
- dim(a) Dimensions
- ncol(A) number of columns
- A[a : b, c(takerow1, takerow2)] subtracting a square matrix
- det(A1) Determinant
- solve(A1) Inverse of A1
- A1% ∗ %solve(A1) % ∗ % matrix multiplication diag(4) Matrix diagonal
- cbind(1, A1) combining matrices columns
- rbind(A1, diag(4, 2)) combining matrices diagonal

3. Arrays

**Definition:** An array is a data structure that can hold multi-dimensional data. The arrays can hold two or more two-dimensional [data](https://www.datacamp.com/tutorial/arrays-in-r).

**Example code:**

```python
dim(as.array(letters)) # Read a object as an array

#Z <- array(data_vector, dim_vector)
array(1:3, c(2,4)) # recycle 1:3 "2 2/3 times"
```

4. Data Frame

**Definition:** Data Frames are data displayed in a format like a table. Data Frames can have different types of objects. For example, the first column can be a character, the second and third can be numeric or logical. However, each column should have the same type of [data](https://www.w3schools.com/r/r_data_frames.asp#:~:text=Data%20Frames%20are%20data%20displayed,the%20same%20type%20of%20data.).

**Example code:**

```python
d <- c(1,2,3,4)
e <- c("red", "white", "red", NA)
f <- c(TRUE,TRUE,TRUE,FALSE)
mydata <- data.frame(d,e,f)
names(mydata) <- c("ID","Color","Passed") # variable names
mydata
```

**Save and load table**

Need to set your directory and use the following document [Journals.csv](https://purdue0-my.sharepoint.com/:x:/g/personal/dmartinl_purdue_edu/ETDxKzGxgVhHmbITK7pDaD0Bc8ppu5cwrmPlbwtbQgwX5A?e=I86ilU)

**Example code:**

```python
# Save an object
write.table(Journals, "Journals.csv", sep=";")
#rm(list=ls(all=TRUE)) # remove all the objects in the memmory

# load an object
data <- read.table("Journals.csv",sep=";", dec=".", row.names=1, header=TRUE)
#setwd("C:\\Users\\mmarin\\Desktop") #Change working directory
```

Exercise 2 - Data frame

1. Generate a data frame with five types of individuals.
2. Assign the ID, Age, Country, Education, and a variable X1 with the salary.

Suggested solution - 2 (Try yourself first)

**Example code:**

```python
a <- c(1,2,3,4,5)
b <- c(18,20,21,22,5)
c <- c("Colombia","Argentina","Peru","Bolivia","Chile")
d <- c("Secondary","University","Secondary","Secondary","Primary")
e <- c(100,200,400,150,NA)
myframe<- data.frame(a,b,c,d ,e)
names(myframe)<-c("ID","Age","Country","Education ","x1") # variable names
myframe

#There are a variety of ways to identify the elements of a data frame .

myframe[3:5] # columns 3,4,5 of data frame
myframe[c("ID","Age")] # columns ID and Age from data frame
myframe$x1 # variable x1 in the data frame
```

5. List

**Definition:** An ordered collection of objects (components). A list allows you to gather various (possibly unrelated) objects under one name.

**Example code:**

```python
# example of a list with 4 components -
# a string, a numeric vector, a matrix, and a scaler
w <- list(name="Fred", mynumbers=a, mymatrix=y, age=22)

#Identify elements of a list using the [[]] convention.
w[[2]] # 2nd component of the list
w[[3]] # 2nd component of the list
w[["mynumbers"]] # component named mynumbers in list

# example of a list containing two lists
list1 <- list(example_data_frame=mydata)
list2 <- list(exercise1=myframe)

v <- c(list1,list2)
v

#Other example, it can be skip
lista <- vector("list",4)
lista[[1]] <- Journals
lista[[2]] <- "a"
lista[[3]] <- I
lista
```

6. Factor

**Definition:** The factor stores the nominal values as a vector of integers in the range [ 1... k ] (where k is the number of unique values in the nominal variable), and an internal vector of character strings (the original values) mapped to these integers. **R** will treat, in statistical procedures and graphical analyses:

- Factors as nominal variables.
- Ordered factors as ordinal variables.
- Class of files class().

A **factor** is similar to the **encode** function in Stata.

**Example code:**

```python
# variable gender with 20 "male" entries and  30 "female" entries
# rep() replicates a vector
gender <- c(rep("male",20), rep("female", 30))
            gender
gender <- factor(gender)
            gender
# stores gender as 20 1s and 30 2s and associates
# 1=female, 2=male internally (alphabetically)
# R now treats gender as a nominal variable
summary(gender)

#An ordered factor is used to represent an ordinal variable.

# variable rating coded as "large", "medium", "small'
rating <- c("large", "medium", "small")
rating <- ordered(rating)
rating
# recodes rating to 1,2,3 and associates
# 1=large, 2=medium, 3=small internally
# R now treats rating as ordinal
```

**Some functions to start**

1. Get help

There are multiple blogs and help sources on the Internet. Try to google it and look for specific code.

**R** also can give you some advice using the following code

```python
?options ## To Internet
help(options)
example(option)
example(lm)

# If the exact name of the command is not know
help.search("sum") # To Internet list of commands
apropos("sum")
```

2. Loops

R calls loops as controls. In Stata, we use *foreach* and *forvalue.*

**Example code:**

```python
?Control # Help for loops

# Let's start with a vector
x <- c(1.8, 3.14, 4, 88.169, 13)
sum(x)
mean(x)

if(rnorm(1) > 0) sum(x) else mean(x) ##

ifelse(x > 4, sqrt(x), x^2) ## This computes the square root for those values in x that are greater than 4 and the square for the remaining ones.
```

We can use the function *for* in loops. This function is the closest to *foreach*

**Example code:**

```python
for(i in 2:5) {
 		x[i] <- x[i] - x[i-1]
		 }
x[-1]  ## Show all the vector exept the first position

x1<-3.14-1.8
x1
```

You can also use *while* function to create conditionals

**Example code:**

```python
i=1

while(sum(x) < 100) {

			 x <- 2 * x
       i=i+1
			 }
x ## Doing the same until bidding the condition.
i
```

3. Export and import

In Stata, we use *cd* to set the path of the files. In R, we use *setwd().* Check how the paths should go. In Windows use *//* and IOS */.*

**Example code:**

```python
#Direction
setwd("G:\\Courses\\Casual Inference and Impact Evaluation\\1. R\\import")
```

We use *read.table( )* to import data frames.

**Example code:**

```python
write.table(mydata, file = "mydata.txt", col.names = TRUE) # Export
newdata <- read.table("mydata.txt", header = TRUE) # Import a table that you export before
newdata
```

To import data, we need to consider the type of extension.

1. csv. read.table(”c : /mydata.csv”, sep = ”, ”)
2. xlsx. library(xlsx) and then
   read.xlsx(”c : /myexcel.xlsx”, 1)
3. dta. library(f oreign) and then
   read.dta(import − stata.dta)
4. rda. save(mydata, f ile = ”mydata.rda”) it makes all objects stored in mydata.rda directly available within the current environment. The advantage of using .rda files is that several arbitrary R objects can be stored, including functions or fitted models, without loss of information.
5. Similarly functions to export

**Example code:**

```python
## Diferent type of import

#1)csv
# first row conains variable names, comma is separator
# assign the variable id to row names
# note the / instead of \ on mswindows systems

#mydata <- read.table("c:/mydata.csv", header=TRUE,
#  	sep=",", row.names="id")

mydata <- read.table("primero.csv", header=TRUE,  sep=",")
mydata

#2) xlsx

# read in the first worksheet from the workbook myexcel.xlsx
# first row contains variable names

#install.packages("xlsx")
library(xlsx)
#mydata <- read.xlsx("c:/myexcel.xlsx", 1)
#mydata <- read.xlsx("c:/myexcel.xlsx", sheetName = "mysheet")

#3) stata
library(foreign)

mydata<-read.dta("tercero.dta") # Error
mydata<-read.dta("tercero2012.dta")

#4) In R .rda save all
save(mydata, file = "mydata.rda") #saves the data in R binary format
load("mydata.rda")

data("Journals", package = "AER")

dir() ##Files available in a directory or folder can be queried via dir

newobject <- read.table("mydata.txt", na.strings = "-999") #export with -999 in NA

file.remove("tercero2012.dta")
```

4. Merge function

**Definition:** To merge two data frames (datasets) horizontally, use the merge function. In most cases, you join two data frames by one or more common key variables (i.e., an inner join).

**Additional step:** For example, we need to create two databases to merge, but in real life, you should have the data already (this step is also good practice in creating Data Frame).

**Example code**

```python
#i) Generate a dataframe authors
authors <- data.frame(
  surname = I(c("Tukey", "Venables", "Tierney", "Ripley", "McNeil")),
  nationality = c("US", "Australia", "US", "UK", "Australia"),
  deceased = c("yes", rep("no", 4)))
```

```python
  #ii) Generate a dataframe books
books <- data.frame(
  name = I(c("Tukey", "Venables", "Tierney",
             "Ripley", "Ripley", "McNeil", "R Core")),
  title = c("Exploratory Data Analysis",
            "Modern Applied Statistics ...",
            "LISP-STAT",
            "Spatial Statistics", "Stochastic Simulation",
            "Interactive Data Analysis",
            "An Introduction to R"),
  other.author = c(NA, "Ripley", NA, NA, NA, NA,
                   "Venables & Smith"))
```

Now, let's do merge

```python
#iii) Merge
(m1 <- merge(authors, books, by.x = "surname", by.y = "name"))
(m2 <- merge(books, authors, by.x = "name", by.y = "surname"))
## "R core" is missing from authors and appears only here :
merge(authors, books, by.x = "surname", by.y = "name", all = TRUE)
```

Finally, we could play with different data structures and still run a merge.

```python
merge(p, q, by = c("k1","k2")) # NA's match
merge(p, q, by = "k1") # NA's match, so 6 rows
merge(p, q, by = "k2", incomparables = NA) # 2 rows
```

Stata users might wonder where is the n:1, 1:n, n:n structure. The merge function in Stata asked you for the type of merge you aim at. Here, R uses the type of merge (from n:1, 1:n, n:n) that better fits your data. The good news is that Stata users wouldn't get an error saying, "ID is repeated in the using data." The bad news is that you wouldn't know directly what type of merge R performs. You can still check the data to see the type of merge and tell R what type of merge you want.

5. More functions

An example of the functions you might need to use at the beginning.

**Example code:**

```python
## Class of files
class(Journals)
class(myframe)
class(a)
class(c)
class(A)
class(gender)
class(rating)

class(Journals$field) # Inside class show the column field

## Useful Function
length(Journals) # number of elements or components
str(Journals)    # structure of an object
class(Journals)  # class or type of an object
names(Journals)  # names

mydataframe <- c(mydata,myframe) # combine objects into a vector
mydataframe

cbind(a, b) # combine objects as columns, it has to have same dimensions
rbind(c, d) # combine objects as rows

myframe    # prints the object

ls(myframe)       # list current objects
#rm(mydata)		 # delete an object
x
remove(x)		# Remove an object
```

6. Random variables

- Object “normsample” then contains a sample from a normal distribution.
- Creating function normsample.
- This function takes a required argument n (the sample size) and further arguments ..., which are passed on to rnorm(), the function for generating normal random numbers.
- In addition to the sample size, it takes further arguments—the mean and the standard deviation.
- After the generation of the vector of normal random numbers, it is assigned the class “normsample” and then returned.

**Example code:**

```python
# Defining the object

normsample <- function(n, ...) {
rval <- rnorm(n, ...)
class(rval) <- "normsample"
return(rval)
}

p<-rnorm(20)

#This function takes a required argument n (the sample size) and further
# arguments ..., which are passed on to rnorm(), the function for
#generating normal random numbers. In addition to the sample size,
#it takes further arguments?the mean and the standard deviation

set.seed(123)
x <- normsample(10, mean = 5)
x
class(x)

#To define a summary() method, we create a function summary.normsample()
summary.normsample <- function(object, ...) {
rval <- c(length(object), mean(object), sd(object))
names(rval) <- c("sample size","mean","standard deviation")
return(rval)
}

summary.normsample(x)
```

**Linear Regression** **(Economists,** **such** **as myself, love regressions)**

Let's study the demand for economics journals.

We begin with a small data set taken from Stock and Watson (2007) that provides information on the number of library subscriptions to economic journals in the US in 2000. The data set, collected initially by Bergstrom (2001), is available in package AER under the name Journals.

1. Upload database

We will need to install the package AER.

R has millions of packages that people create to run multiple statistical processes. Uploading packages in Windows is more straightforward than in IOS. In RStduio, I usually upload packages [manually](https://derekogle.com/IFAR/supplements/installations/InstallPackagesRStudio.html)

**Example code:**

```python
install.packages("AER") ## install packages
library(AER) ## Loaded a package
data ("Journals", package="AER") ## Call the date
```

Let's check the data before continuing

```python
dim(Journals)
names(Journals)
```

2. Simple graphs

We plot the number of subscribers against the share of price and citations. We use logs to reduce outliers and make the graph smoother.

We use the symbol ~ as the math expression equal (=) in R. For Stata users this symbol is a little strange. In Stata, *~* is like the space in between y and x in the following Stata code *line y x*

**Example code:**

```python
plot(log(subs) ~ log(price/citations), data = Journals)
```

3. Estimations

Now, we run an Ordinary Lineal Square (OLS).

**Example code:**

```python
# OLS
j_lm <- lm(log(subs) ~ log(price/citations), data = Journals)
abline(j_lm) # The abline() command adds the least-squares line to the existing scatterplot
summary(j_lm)
```

In Stata, there are post-command functions for getting. In R, we can also get post-command estimators.

```python
coef(j_lm) # coeficients
residuals(j_lm) # estimate residuals by individual (e)
fitted(j_lm) # \hat{Y} estimate data
vcov(j_lm) # covariance matrix
diag(vcov(j_lm))^0.5 #standar deviation

coeficient <- coef(j_lm)
DesStandar<- diag(vcov(j_lm))^0.5

rbind(coeficient , DesStandar)
```

Economists love to estimate by subsamples. The following code runs the estimation for a set of journals.

```python
j_lm <- lm(log(subs)~log(price/citations), data=Journals, subset=c(1,2,3,4,5,10,20))
summary(j_lm)
```

Exercise 3 - Wage Equation

Estimating a wage equation in semi-logarithmic form is based on data taken from Berndt (1991).

1. Loading the data set CPS1985 from the package AER.
2. Generate a data cps equal to CPS1985.
3. Estimate a Mincer equation (1958) with experience squared and education with OLS.
4. Graph Wage with experience, experience squared and education.
5. Install the package ”quantreg”.
6. Estimate with quantile regressions the Mincer equation (1956). Hint: use the help.

Suggested solution - 3 (Try yourself first)

**Example code**

```python
#1)
data("CPS1985", package = "AER")
#2) Create another data.frame with other name
cps <- CPS1985
objects()

#3) OLS
cps_lm <- lm(log(wage) ~ experience + I(experience^2) + education, data = cps)
summary(cps_lm)

coef(cps_lm) # coeficients
residuals(cps_lm) # estimate residuals by individual (e)
fitted(cps_lm) # \hat{Y} estimate data
vcov(cps_lm) # covariance matrix
diag(vcov(cps_lm))^0.5 #standar deviation

coeficient <- coef(cps_lm)
DesStandar<- diag(vcov(cps_lm))^0.5

cps_lm_result<-rbind(coeficient , DesStandar)
cps_lm_result

#4)Graph
plot(log(wage) ~ experience, data = cps)
abline(cps_lm)

#5) Instal quantreg
# Be carful it may install manually

#install.packages("quantreg")
library("quantreg")

#detach("package:quantreg", unload=FALSE)
#library("quantreg", lib.loc="~/R/win-library/3.2")

# 6) tau the set of quartiles

cps_rq <- rq(log(wage) ~ experience + I(experience^2) ++ education, data = cps, tau = seq(0.2, 0.8, by = 0.15))
summary(cps_rq)
```

Exercise 4 - Wages and year of experience

- Generate data cps2, where education is held constant, and experience varies over a range.
- Add predicted values (βˆ), lower and upper bound.
- Add predicted values for percentiles.
- Visualize a result from wage to experience.

Suggested solution - 4 (Try yourself first)

**Example code:**

```python
# 2 Columns with mean education and vary experience
# Held education in the mean.
cps2 <- data.frame(education = mean(cps$education), experience = min(cps$experience):max(cps$experience))
cps2
# Add 3 Columns with fitted values, lower bound and upper bound
cps2 <- cbind(cps2, predict(cps_lm, newdata = cps2, interval = "prediction"))
cps2
# Add 5 Columns for tau (quantiles)
cps2 <- cbind(cps2, predict(cps_rq, newdata = cps2, type = ""))
cps2

plot(log(wage) ~ experience, data = cps)

for(i in 6:10) {
 lines(cps2[,i] ~ experience,data = cps2, col = "red") #loop, plot the last 4 columns, which are the quantiles.
}

# Other way to see - Optionaly
plot(summary(cps_rq)) # Plot the results dor quantile
```

Boom! The graph should show higher wages for individuals with more experience (not surprising). The curvature of the regression lines is more marked at lower quartiles, whereas the relationship is much flatter for higher quantiles.

Exercise 5 - Prices and subscripts

1. Use data “Journals” from “AER”.
2. Create a data “journals”, with data with two columns
   subscriptions (“subs”) and Price “price”, from “Journals”.
3. Create citeprice as price/citations and adding to journals.
4. Graph the log of “subs” against the log of “citeprice”.
5. Run the same regression as step 4 and add the fitted line to the graph in that step.
6. And with Matrix

Suggested solution - 5 (Try yourself first)

**Example code:**

```python
#1)
library("AER")
data("Journals")

#2)
journals <- Journals[, c("subs", "price")] # Take only subs an price in a data.frame

#3)
journals$citeprice <- Journals$price/Journals$citations # Taking a colummn from journal
summary(journals)

#4)
plot(log(subs) ~ log(citeprice), data = journals)

#5)
jour_lm <- lm(log(subs) ~ log(citeprice), data = journals)
abline(jour_lm)
```

4. Dichotomous variables (Dummy variables)

**Definition:** Variables with only two categories or levels. For example, if we were looking at gender, we would probably categorize somebody as either "male" or ["female](https://statistics.laerd.com/statistical-guides/types-of-variable.php#:~:text=Dichotomous%20variables%20are%20nominal%20variables,and%20also%20a%20nominal%20variable).)."

Typical econometric examples of categorical variables include gender, union membership, or ethnicity. Encoding (e.g., 0 for males and 1 for females).

**Example code**

```python
g < − factor(g, levels = 0 : 1, labels = c(”male”, ”f emale”))
```

5. Non-Linear regressions

We can estimate a quadratic polynomial.

**Example code:**

```python
#1)
data("CPS1988")
summary(CPS1988)

#2)
cps_lm <- lm(log(wage) ~ experience + I(experience^2) +
               education + ethnicity, data = CPS1988)

#3)
summary(cps_lm)
```

*I()* returns its argument “as is.” This is one way to calculate a quadratic model.

6. Comparison of models

With more than a single explanatory variable, it is interesting to test for the relevance of subsets of regressors. For any two nested models.

For example, it might be desired to test for the relevance of the variable ethnicity, i.e., whether there is a difference in the average log-wage (controlling for experience and education) between Caucasian and African-American men.

We can use the command anova (the command is similar in State).

- anova(cpsnoeth,cpslm) Test that the RSS of both models is equal.
- anova(cpslm) the same test as before. When there is just one model, it adds one variable at a time and does the same test.
- update instead to write the equation without ethnicity
- waldtest() this produces the same F test as anova() but does not report the associated RSS.

**Example code:**

```python
attach(CPS1988)
summary(ethnicity)
detach(CPS1988)

# ----------------------
# Comparision of models
# ----------------------

#i) Estimate a model without ethnicity
cps_noeth <- lm(log(wage) ~ experience + I(experience^2) +
                  education, data = CPS1988)

#ii)Test that including the variable ethnicity is relevant
anova(cps_noeth, cps_lm)

# It tests the different in RSS, in this case the effect of including
# the variable is sgnificant.

anova(cps_lm) #Test adding variable by variable, depending on the formula

#There is also a more elegant way to fit the latter model given the former.
#It is not necessary to type in the model formula again
cps_noeth <- update(cps_lm, formula = . ~ . - ethnicity)

# Test de Wald
waldtest(cps_lm, . ~ . - ethnicity)
```

**Descriptive Statistics**

In Stata, we can use the command summarize to calculate the descriptive statistics of the database. We can do the same in R with the following commands.

1. Mean, Median, and Standard Deviation

**Example code:**

```python
rm(list=ls(all=TRUE)) # remove all the objects in the memory

data("CPS1985")
str(CPS1985)
head(CPS1985)

levels(CPS1985$occupation)[c(2, 6)] <- c("techn", "mgmt") #
attach(CPS1985) # to use column wage

summary(wage)
mean(wage)
median(wage)
var(wage)
sd(wage)
```

2. Histograms

**Example code:**

```python
hist(wage, freq = FALSE)
hist(wage, freq = TRUE)

hist(log(wage), freq = FALSE)
lines(density(log(wage)), col = 4)
```

3. More sophisticated graphs

**Example code:**

```python
barplot(tab)
barplot(table(occupation))

pie(tab)

xtabs(~ gender + occupation, data = CPS1985) # tab two categories

plot(gender ~ occupation, data = CPS1985)

cor(log(wage), education) # correlation

cor(log(wage), education, method = "spearman")

plot(log(wage) ~ education)

xtabs(~ gender + wage, data = CPS1985)

class(wage)
class(gender)

tapply(log(wage), gender, mean) # Another kind of tab
plot(log(wage) ~ gender) #Given x is a factor

mwage <- subset(CPS1985, gender == "male")$wage
fwage <- subset(CPS1985, gender == "female")$wage
qqplot(mwage, fwage, xlim = range(wage), ylim = range(wage),
xaxs = "i", yaxs = "i", xlab = "male", ylab = "female")
abline(0, 1)
```

**Interactions, Separate, and Weights**

- y a + x Model without interaction. Identical slopes to x but different intercepts to a.
- y a ∗ x Model with interaction. This interaction included ethnicity, education and the interaction between the two.
- y a + x + a : x, the term a:x gives the difference in slopes compared with the reference category, in other words, just the interaction.

**Example code:**

```python
#Interaction
cps_int <- lm(log(wage) ~ experience + I(experience^2) +
                education * ethnicity, data = CPS1988)
# Test of coeficients
coeftest(cps_int)

cps_int <- lm(log(wage) ~ experience + I(experience^2) +
                education + ethnicity + education:ethnicity,
              data = CPS1988)
coeftest(cps_int)  ## Both models are the same.
```

Separate regression for each level

As a further variation, it may be necessary to fit separate regressions for African-Americans and Caucasians.

- This model specifies that the terms within parentheses are nested within ethnicity.
- The term -1 removes the intercept of the nested model. A matrix to see results for both ethnicity
- anova(model1, model2) the model where ethnicity interacts with every other regressor fits significantly better, at any reasonable level than the model without any interaction term.

**Example code:**

```python
cps_sep <- lm(log(wage) ~ ethnicity /
                (experience + I(experience^2) + education) - 1,
                 data = CPS1988)

#Estimate two models for separate
summary(cps_sep)

# To compare both models
cps_sep_cf <- matrix(coef(cps_sep), nrow = 2)
rownames(cps_sep_cf) <- levels(CPS1988$ethnicity)
colnames(cps_sep_cf) <- names(coef(cps_lm))[1:4]
cps_sep_cf

anova(cps_sep, cps_lm)
```

Weighted least squares

Cross-section regressions are often plagued by *heteroskedasticity*. Weighted least squares (WLS) is one of the remedies.

**Example code:**

```python
# Change of the reference category
CPS1988$region <- relevel(CPS1988$region, ref = "south")
cps_region <- lm(log(wage) ~ ethnicity + education +
                   experience + I(experience^2) + region, data = CPS1988)
coef(cps_region)

# ----------------------------
# Weighted least squares (WLS)
# To solve heteroskedasticity
# ----------------------------

jour_wls1 <- lm(log(subs) ~ log(citeprice), data = journals,
                weights = 1/citeprice^2)

jour_wls2 <- lm(log(subs) ~ log(citeprice), data = journals,
                weights = 1/citeprice)

# To see the problem in the variance and how WLS solves.
plot(log(subs) ~ log(citeprice), data = journals)
abline(jour_lm)
abline(jour_wls1, lwd = 2, lty = 2)
abline(jour_wls2, lwd = 2, lty = 3)
legend("bottomleft", c("OLS", "WLS1", "WLS2"),
       lty = 1:3, lwd = 2, bty = "n")
```

**References**

- A Modern Approach to Regression with R.
- An Introduction for R for Quantitative Economics.
- R for STATA users.
- Applied Econometric with R.
