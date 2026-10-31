
data <- read.csv(file.choose(), header = TRUE)


print(dim(data))
print(head(data))
print(colnames(data))
str(data)


print(sum(is.na(data)))
print(sum(duplicated(data)))

numeric_data <- data[, sapply(data, is.numeric), drop = FALSE]


print(sum(as.matrix(numeric_data) < 0, na.rm = TRUE))
print(sum(as.matrix(numeric_data) == 0, na.rm = TRUE))


print(summary(numeric_data))


if (ncol(numeric_data) > 0) {
  boxplot(numeric_data,
          main = "Gene Expression Distribution",
          xlab = "Samples",
          ylab = "Expression Value",
          las = 2)
} else {
  print("No numerical columns found in the dataset.")
}
