import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("Market_Basket_Transations_50Samples.csv")

# Preview the first few rows
print(df.head())
print(f"\nTotal transactions: {len(df)}")

# ----- Count Frequency of Each Individual Item -----

# Split each transaction string into a list of items
transactions = df["Items Bought"].apply(lambda x: [item.strip() for
                                                   item in x.split(",")])


# Flatten all lists into a single list with all purchased items
all_items = [item for sublist in transactions for item in sublist]

print(all_items)

# Use pandas value_counts to count item frequency
item_counts = pd.Series(all_items).value_counts()

print("\nFrequency of Individual Goods Purchased:")
print(item_counts)

# Plot bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(item_counts.index, item_counts.values, color='cornflowerblue')
plt.title('Frequency of Individual Goods Purchased')
plt.xlabel('Goods')
plt.ylabel('Frequency')

# Annotate frequency on each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{int(bar.get_height())}', ha='center', va='bottom')

plt.tight_layout()
plt.show()


