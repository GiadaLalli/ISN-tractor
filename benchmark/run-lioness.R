library(lionessR)

args <- commandArgs(trailingOnly = TRUE)
sample_size <- as.integer(args[1])
variables <- as.integer(args[2])

data_simulation <- function(nind, ngeni){
  exp <- matrix(rnorm(nind*ngeni, 0, 15), nind, ngeni)
  colnames(exp) <- paste("sample", c(1:ncol(exp)), sep="_")
  rownames(exp) <- paste("gene", c(1:nrow(exp)), sep="_")
  return(exp)
}

df <- data_simulation(nind = sample_size, ngeni = variables)
invisible(lioness(df, netFun))