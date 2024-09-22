import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

titanic = pd.read_csv("titanic.csv")
titanic_train = pd.read_csv("titanic_train.csv")
titanic_test = pd.read_csv("titanic_test.csv")

classifier = RandomForestClassifier(random_state=0)
titanic_train_labels = titanic_train["Survived"]
titanic_train = titanic_train.drop(columns=["Survived"])

model = classifier.fit(titanic_train, titanic_train_labels)

titanic_test_labels = titanic_test["Survived"]
titanic_test = titanic_test.drop(columns=["Survived"])

predictions = model.predict(titanic_test)
print(accuracy_score(predictions, titanic_test_labels))

person = {"female": [0], "male": [1], "Age": [34.0], "Fare": [13], "Family_Size": [0], "Pclass": [2]}
person_df = pd.DataFrame(person)
print(model.predict(person_df))