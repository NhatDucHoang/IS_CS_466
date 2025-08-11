import matplotlib
print(matplotlib.__version__)
# -------------------------------------------------------
import matplotlib.pyplot as plt

# Data
items = ['Bread', 'Milk', 'Eggs', 'Butter']
frequencies = [3, 4, 2, 3]

# Plot
plt.figure(figsize=(6, 4))
bars = plt.bar(items, frequencies, color=['saddlebrown', 'skyblue', 'lightgreen', 'gold'])
plt.title('Frequency of Goods Purchased')
plt.xlabel('Goods')
plt.ylabel('Frequency')

# Annotate each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# -------------------------------------------------------
New_List = [1, 3, 5, 7, 9]
print('Number of items in the list: ', len(New_List))
print('The second item the list: ', New_List[1])
print('Sum of items the list: ', sum(New_List))
print('Max of items the list: ', max(New_List))
print('Min of items the list: ', min(New_List))

# -------------------------------------------------------
import matplotlib.pyplot as plt

pairs = [
    'Bread & Milk',
    'Milk & Butter',
    'Bread & Butter',
    'Bread & Eggs',
    'Milk & Eggs',
    'Eggs & Butter'
]
frequencies = [2, 3, 1, 1, 1, 1]

plt.figure(figsize=(7, 4))
bars = plt.bar(pairs, frequencies, color='skyblue')
plt.title('Frequency of Pairwise Itemsets')
plt.xlabel('Item Pair')
plt.ylabel('Frequency')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{int(bar.get_height())}', ha='center', va='bottom')

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
# -------------------------------------------------------
# List of transactions
transactions = [
    ['Bread', 'Milk'],
    ['Bread', 'Eggs'],
    ['Milk', 'Eggs', 'Butter'],
    ['Bread', 'Milk', 'Butter'],
    ['Milk', 'Butter']
]

# Define the itemset we want to check
itemset = {'Milk', 'Butter'}

# Initialize counter for itemset occurrences
count = 0

# Loop over each transaction
for transaction in transactions:
    # Check if both 'Milk' and 'Butter' are present
    if itemset.issubset(transaction):
        count += 1

# Calculate support: count divided by total transactions
support = count / len(transactions)
print(f"Support(Milk & Butter) = {support:.2f}")
# -------------------------------------------------------
# List of transactions
transactions = [
    ['Bread', 'Milk'],
    ['Bread', 'Eggs'],
    ['Milk', 'Eggs', 'Butter'],
    ['Bread', 'Milk', 'Butter'],
    ['Milk', 'Butter']
]

# Define the itemset we want to check
itemset = {'Milk'}

# Initialize counter for itemset occurrences
count = 0

# Loop over each transaction
for transaction in transactions:
    # Check if both 'Milk' and 'Butter' are present
    if itemset.issubset(transaction):
        count += 1

# Calculate support: count divided by total transactions
support = count / len(transactions)
print(f"Support(Milk) = {support:.2f}")
# -------------------------------------------------------
support = 0.60     
confidence = 0.75

if support >= 0.6 and confidence >= 0.6:
    print("High support - high confidence")
    
if support < 0.6 and confidence >= 0.6:
    print("Low support - high confidence")
    
if support >= 0.6 and confidence < 0.6:
    print("High support - low confidence")
    
if support < 0.6 and confidence < 0.6:
    print("Low support - low confidence")
# -------------------------------------------------------
import pandas as pd
df = pd.read_csv("Market_Basket_Transations_30Samples.csv")
print(df.head())
print(f"\nTotal transactions: {len(df)}")

# Extract transactions as list of lists
transactions = df["Items Bought"].apply(lambda x: [item.strip() for item in x.split(",")]).tolist()

print(transactions[0])
print(transactions[1])
