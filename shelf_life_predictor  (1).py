# Shelf-Life Grocery Predictor - Final Correct Code

import pandas as pd
from datetime import datetime
from sklearn.preprocessing import LabelEncoder

# Load Dataset
file_path = "grocery_dataset_project.xlsx"
df = pd.read_excel(file_path)

# Convert Purchase Date to datetime
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Calculate Days Used
current_date = datetime.today()
df["Days_Used"] = (current_date - df["Purchase_Date"]).dt.days

# Calculate Remaining Days
df["Remaining_Days"] = df["Avg_Shelf_Life_Days"] - df["Days_Used"]
df["Remaining_Days"] = df["Remaining_Days"].apply(lambda x: max(x, 0))

# Encode Category and Storage
le_category = LabelEncoder()
le_storage = LabelEncoder()

df["Category_Encoded"] = le_category.fit_transform(df["Category"])
df["Storage_Encoded"] = le_storage.fit_transform(df["Storage"])

print("Dataset Loaded Successfully!\n")

# Prediction Function
def predict_shelf_life():
    item = input("Enter Item Name: ").title()
    category = input("Enter Category: ").title()
    storage = input("Enter Storage Type: ").title()
    avg_life = int(input("Enter Avg Shelf Life: "))
    days_used = int(input("Enter Days Used: "))

    # Simple Accurate Formula
    remaining_days = avg_life - days_used
    if remaining_days < 0:
        remaining_days = 0

    print(f"\nPredicted Remaining Shelf Life: {remaining_days} days")

    # Repeat Option
    choice = input("\nAgain? (yes/no): ").lower()
    if choice == "yes":
        predict_shelf_life()
    else:
        print("\nThank you for using Shelf-Life Grocery Predictor!")

# Run Program
if __name__ == "__main__":
    predict_shelf_life()
