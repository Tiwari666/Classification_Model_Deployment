import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
df = pd.read_csv('../data/Restaurant_Reviews.csv')

# Prepare the data
X = df['text']
y = df['sentiment']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Convert text data to numerical data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Transform the test data using the saved vectorizer
X_test_transformed = vectorizer.transform(X_test)

# Predict using the trained model
y_pred = model.predict(X_test_transformed)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(vectorizer, '../models/vectorizer.joblib')
joblib.dump(model, '../models/model.joblib')

# Load and evaluate the saved model
loaded_vectorizer = joblib.load('../models/vectorizer.joblib')
loaded_model = joblib.load('../models/model.joblib')
y_pred_loaded = loaded_model.predict(X_test_transformed)
print(f"Accuracy of loaded model: {accuracy_score(y_test, y_pred_loaded)}")

# Save the evaluation results
with open('../results/evaluation_results.txt', 'w') as f:
    f.write(f"Accuracy: {accuracy}\n")
    f.write(f"Classification report:\n{classification_report(y_test, y_pred)}")
    f.write(f"Accuracy of loaded model: {accuracy_score(y_test, y_pred_loaded)}")
    