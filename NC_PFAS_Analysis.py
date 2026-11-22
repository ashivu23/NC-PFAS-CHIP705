# CHIP 705 - PFAS Project
# Student: Shivani
# University of North Carolina at Chapel Hill

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Open the Excel file
data = pd.read_excel("Download Contaminant Results.xlsx")

# Step 3: Look at the dataset
print("First five rows:")
print(data.head())

# Step 4: Count records, water systems, and compounds
print("\nTotal records:", len(data))
print("Number of water systems:", data["PWS ID"].nunique())
print("Number of PFAS compounds:", data["Contaminant"].nunique())

# Step 5: Separate numeric results from results below MRL
data["Numeric Result"] = pd.to_numeric(data["Result (µg/L)"], errors="coerce")

numeric = data["Numeric Result"].count()
below_mrl = len(data) - numeric

print("\nNumeric results:", numeric)
print("Below MRL:", below_mrl)

# Step 6: Calculate percentages
print("Numeric results (%):", round(numeric / len(data) * 100, 2))
print("Below MRL (%):", round(below_mrl / len(data) * 100, 2))

# Step 7: Graph 1 - Top six PFAS compounds
top_six = data[data["Numeric Result"].notna()]["Contaminant"].value_counts().head(6)

top_six.plot(kind="bar", color="purple")

plt.title("Top Six PFAS Compounds by Number of Numeric Results")
plt.xlabel("PFAS Compound")
plt.ylabel("Number of Numeric Results (records)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Graph_1.png")
plt.show()

# Step 8: Graph 2 - Reporting status
plt.pie(
    [numeric, below_mrl], labels=["Numeric Results", "Below MRL"], autopct="%1.2f%%"
)

plt.title("Distribution of PFAS Results by Reporting Status")
plt.savefig("Graph_2.png")
plt.show()

# Step 9: Finish
print("\nPFAS analysis completed!")
