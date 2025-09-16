import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.read_csv("train.csv")

# Select simple features
data = data[["OverallQual", "GrLivArea", "GarageCars", "YearBuilt", "SalePrice"]].dropna()

X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("house_price_model.pkl", "wb"))

print("✅ Model trained and saved as house_price_model.pkl")
