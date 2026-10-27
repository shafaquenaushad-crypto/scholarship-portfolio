# DNA SEQUENCE ANALYSIS


# 1. Counting A, T, G, C

nucleotide <- c("A","T","G","C")
dna <- sample(nucleotide, 10, replace = TRUE)
dna

lengthl <- length(dna)
print(lengthl)

a=0; t=0; g=0; c=0;

for(i in 1:lengthl){
  if(dna[i]=="A"){a=a+1}
  if(dna[i]=="T"){t=t+1}
  if(dna[i]=="G"){g=g+1}
  if(dna[i]=="C"){c=c+1}
}

cat("a,t,g,c  ",a,t,g,c)


# 2. Complementary DNA Sequence Analysis

DNAseq <- function(x) {
  basepair <- c("A", "T", "C", "G")
  abc <- unlist(strsplit(toupper(x), NULL))
  
  paste(unlist(lapply(abc, function(DNAseq) {
    if (DNAseq == "A") strings <- "T"
    if (DNAseq == "T") strings <- "A"
    if (DNAseq == "C") strings <- "G"
    if (DNAseq == "G") strings <- "C"
    if (!(DNAseq %in% basepair)) strings <- "N"
    
    return(strings)
  })), collapse = "")
}

DNAseq("ATCCGGATGACTCGTAAT")
DNAseq("ATCCGGCDDDTTTVHJA")


# 3. Counting DNA Composition

nucleotide <- c("A","T","G","C")
dna <- sample(nucleotide, 10, replace = TRUE)
dna

lengthl <- length(dna)
print(lengthl)

a=0; t=0; g=0; c=0;

for(i in 1:lengthl){
  if(dna[i]=="A"){a=a+1}
  if(dna[i]=="T"){t=t+1}
  if(dna[i]=="G"){g=g+1}
  if(dna[i]=="C"){c=c+1}
}

cat("a,t,g,c  ",a,t,g,c)

AT <- ((a+t)/lengthl)*100
GC <- ((g+c)/lengthl)*100

cat("\nAT composition =",AT,"%")
cat("\nGC composition =",GC,"%")


# 4. Reverse DNA Sequence

reverse_dna <- paste(rev(dna), collapse = "")
cat("\nReverse DNA sequence:", reverse_dna)