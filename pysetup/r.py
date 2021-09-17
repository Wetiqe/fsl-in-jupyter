# r functions which can be used in Python scripts 
import rpy2.robjects as robjects # use basic R function


def to_csv_r(df, group_name, arrtribute):
    """
    save the dataframe as csv file in cache folder
    
    args:
        df: dataframe that is about to transform
        group_name: str, the group name
        arrtribute: str, what the dataframe is about
    
    returns:
        fnmae: str, name of the csv file
    """
    save_fname = './cache/{}_{}'.format(arrtribute,group_name)
    fname = save_fname[8:]
    df[arrtribute].to_csv(save_fname,index=None)
    
    return fname

# R permutation test
# usage: rpy2.robjects.r['func_name'](args)
## R permutation indpendent t
robjects.r(
'''
perm_ind_t <- function(group1_name,group2_name,stop_num, nreps=5000, seed=1086){
test_name <- substr(group1_name,4,as.numeric(stop_num))
g1 <- as.vector(read.csv(paste('./cache/',group1_name, sep=""))[,1])
g2 <- as.vector(read.csv(paste('./cache/',group2_name, sep=""))[,1])
n1 <- length(g1)
n2 <- length(g2)
N <- n1 + n2

meanNW <- mean(g1) 
meanW <- mean(g2) 
diffObt <- (meanW - meanNW)

ttest <- t.test(g2, g1)
tObt <-  ttest$statistic

Combined <- c(g1, g2)     # Combining the samples
meanDiff <- numeric(nreps)   #Setting up arrays to hold the results
t <- numeric(nreps)
set.seed(1086)        
    
for ( i in 1:nreps) {
      data <- sample(Combined, N,  replace = FALSE)
      grp1 <- data[1:n1]
      grp2 <- na.omit(data[n1+1: N])
      meanDiff[i] <- mean(grp1) - mean(grp2)
      test <- t.test(grp1, grp2)
      t[i] <- test$statistic
      }


absMeanDiff <- abs(meanDiff)
absDiffObt = abs(diffObt)
abst <- abs(t)
abstObt <- abs(tObt)
p <- length(abs(absMeanDiff[absMeanDiff >= absDiffObt]))/nreps

return(p)  
}

''')

## R paired t permutation test
robjects.r(
'''
perm_matched_t <- function(group1_name, group2_name, stop_num, nreps=5000, seed=1086){
test_name <- substr(group1_name,5,as.numeric(stop_num))
group1 <- as.vector(read.csv(paste('./cache/',group1_name, sep=""))[,1])
group2 <- as.vector(read.csv(paste('./cache/',group2_name, sep=""))[,1])
diffObt <- mean(group1) - mean(group2) # 差的均值
difference <- group1 - group2  # 每对的差值组成的向量

set.seed(seed)
resampMeanDiff <- numeric(nreps)

for (i in 1:nreps) {
  signs <- sample( c(1,-1),length(difference), replace = T)
  resamp <- difference * signs
  resampMeanDiff[i] <- mean(resamp)
}

data <- as.data.frame(group1)
diffObt <- abs(diffObt)
highprob <- length(resampMeanDiff[resampMeanDiff >= diffObt])/nreps
lowprob <- length(data$resampMeanDiff[data$resampMeanDiff <= (-1)*data$diffObt])/nreps
prob2tailed <- lowprob + highprob

               
tt <- paste("Distribution of Mean Differences:",substr(group1_name,5, as.numeric(stop_num)))
hist(resampMeanDiff, breaks = 30, main = tt, xlab = "Mean Difference", freq = FALSE)
text(7,.08,"Diff. obt")
text(7,.07,round(diffObt,2))
arrows(7, .07, diffObt, 0, length = .125)
text(-7,.08,"p-value")
text(-7,.07, prob2tailed)
               
return(prob2tailed)
}
''')

## A test on a correlation coefficient.
robjects.r(
'''
perm_corr <- function(group1_name, group2_name, stop_num, nreps=5000, seed=1086){
test_name <- substr(group1_name,5,as.numeric(stop_num))
group1 <- as.vector(read.csv(paste('./cache/',group1_name, sep=""))[,1])
group2 <- as.vector(read.csv(paste('./cache/',group2_name, sep=""))[,1])
r.obt <- cor(group1, group2)
r.random <- numeric(nreps)
for (i in 1:nreps) {
Y <- group1
X <- sample(group2, length(group2), replace = FALSE)
r.random[i] <- cor(X,Y)
   }
prob <- length(r.random[r.random >= r.obt])/nreps
cat("Probability randomized r >= r.obt",prob)
hist(r.random, breaks = 50, main =  expression(paste("Distribution around ",rho, "= 0")), xlab = "r from randomized samples")
r.obt <- round(r.obt, digits = 4)
legend(.40, 200, r.obt, bty = "n")
arrows(.5,150,.53, 10)

return(prob) 
}
''')
