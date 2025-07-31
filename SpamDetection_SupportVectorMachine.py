import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# 1. Load Data
df = pd.read_csv('SpamMessageDetection.csv')

# 2. Convert label to binary
df['label'] = df['label'].map({'NoSpam': 0, 'Spam': 1})

# 3. Vectorize Text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])

# 4. Split into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, df['label'], test_size=0.25, random_state=0, stratify=df['label']
)

# 5. Train the SVM Model
svm_model = SVC(kernel = 'rbf', C = 10.0, gamma = 0.1, random_state=0)
svm_model.fit(X_train, y_train)

# 6. Predict on Train and Test Set
y_train_pred = svm_model.predict(X_train)
y_test_pred = svm_model.predict(X_test)

# 7. Training and Testing Accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")

# 8. Compute Confusion Matrix on Test Set
cm = confusion_matrix(y_test, y_test_pred, labels=[0,1])   # 0: NoSpam, 1: Spam
tn, fp, fn, tp = cm.ravel()

# True Positive Rate (Recall for Spam): TP / (TP + FN)
tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
# False Positive Rate: FP / (FP + TN)
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0

print(f"True Positive Rate (Recall for Spam): {tpr:.4f}")
print(f"False Positive Rate: {fpr:.4f}")

print("\nTest Set Classification Report:")
print(classification_report(y_test, y_test_pred, target_names=['NoSpam', 'Spam']))

# Compute confusion matrices
cm_train = confusion_matrix(y_train, y_train_pred, labels=[0,1])
cm_test = confusion_matrix(y_test, y_test_pred, labels=[0,1])

# Display results
print("Confusion Matrix - Training Phase:")
print("         Pred_NoSpam  Pred_Spam")
print("Actual_NoSpam   {:4d}      {:4d}".format(cm_train[0,0], cm_train[0,1]))
print("Actual_Spam     {:4d}      {:4d}".format(cm_train[1,0], cm_train[1,1]))
print("\nConfusion Matrix - Testing Phase:")
print("         Pred_NoSpam  Pred_Spam")
print("Actual_NoSpam   {:4d}      {:4d}".format(cm_test[0,0], cm_test[0,1]))
print("Actual_Spam     {:4d}      {:4d}".format(cm_test[1,0], cm_test[1,1]))
