import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import mmread
import gzip
import glob
print("Starting Task 2 analysis...")


matrix_files = glob.glob("*matrix.mtx.gz")
features_files = glob.glob("*features.tsv.gz")
barcodes_files = glob.glob("*barcodes.tsv.gz")

print("\nFiles found:")
print("Matrix:", matrix_files)
print("Features:", features_files)
print("Barcodes:", barcodes_files)


if not matrix_files:
    raise FileNotFoundError("Matrix file was not found.")

if not features_files:
    raise FileNotFoundError("Features file was not found.")

if not barcodes_files:
    raise FileNotFoundError("Barcodes file was not found.")


matrix_file = matrix_files[0]
features_file = features_files[0]
barcodes_file = barcodes_files[0]

print("\nSelected files:")
print(matrix_file)
print(features_file)
print(barcodes_file)


print("\nReading expression matrix...")

with gzip.open(matrix_file, "rb") as f:
    matrix = mmread(f).tocsr()
if matrix.shape[0] == 0 or matrix.shape[1] == 0:
     raise ValueError("The expression matrix is empty.")


print("Matrix loaded successfully.")


print("Reading features...")

features = pd.read_csv(
    features_file,
    sep="\t",
    header=None,
    compression="gzip"
)

print("Features loaded successfully.")


print("Reading barcodes...")

barcodes = pd.read_csv(
    barcodes_file,
    sep="\t",
    header=None,
    compression="gzip"
)

print("Barcodes loaded successfully.")

print("Basic data information")
print("Matrix shape:", matrix.shape)
print("Number of genes:", len(features))
print("Number of barcodes:", len(barcodes))


print("\nDimension check")
print("Matrix shape:", matrix.shape)

if matrix.shape == (len(features), len(barcodes)):
    print("Genes are in rows and barcodes are in columns.")
    counts_per_barcode = matrix.sum(axis=0).A1
    genes_per_barcode = (matrix > 0).sum(axis=0).A1

elif matrix.shape == (len(barcodes), len(features)):
    print("Barcodes are in rows and genes are in columns.")
    counts_per_barcode = matrix.sum(axis=1).A1
    genes_per_barcode = (matrix > 0).sum(axis=1).A1

else:
    raise ValueError("Matrix dimensions do not match the files.")

print("\nMATRIX STATISTICS")

print("Total number of entries:", matrix.shape[0] * matrix.shape[1])

print("Number of non-zero entries:", matrix.nnz)

print("Total expression/counts:", matrix.sum())

print("Minimum value:", matrix.min())

print("Maximum value:", matrix.max())


print("\nBARCODE/SPOT STATISTICS")



print("Minimum counts per barcode:", counts_per_barcode.min())

print("Maximum counts per barcode:", counts_per_barcode.max())

print("Mean counts per barcode:", counts_per_barcode.mean())

print(
    "Median counts per barcode:",
    pd.Series(counts_per_barcode).median()
)




print("\nDETECTED GENES")

print("Minimum detected genes:", genes_per_barcode.min())

print("Maximum detected genes:", genes_per_barcode.max())

print("Mean detected genes:", genes_per_barcode.mean())

print(
    "Median detected genes:",
    pd.Series(genes_per_barcode).median()
)


quality_summary = pd.DataFrame({
    "Barcode": barcodes.iloc[:, 0],
    "Total_Counts": counts_per_barcode,
    "Detected_Genes": genes_per_barcode
})

print("QUALITY SUMMARY")

print(quality_summary.head())


quality_summary.to_csv(
    "quality_summary.csv",
    index=False
)

print("\nQuality summary saved as: quality_summary.csv")




plt.figure(figsize=(10, 5))
plt.hist(counts_per_barcode, bins=50)
plt.xlabel("Total Counts per Barcode")
plt.ylabel("Number of Barcodes")
plt.title("Distribution of Total Counts per Barcode")
plt.tight_layout()
plt.savefig("total_counts_distribution.png")
plt.show()


plt.figure(figsize=(10, 5))
plt.hist(genes_per_barcode, bins=50)
plt.xlabel("Detected Genes per Barcode")
plt.ylabel("Number of Barcodes")
plt.title("Distribution of Detected Genes per Barcode")
plt.tight_layout()
plt.savefig("detected_genes_distribution.png")
plt.show()

print("Graphs created successfully.")
print("Analysis completed.")