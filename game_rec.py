import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('C:\\Users\\Sujit Layek\\Desktop\\BCT_Project\\game_data1.csv')

# Encode the categorical features
label_encoder = LabelEncoder()
data['Gen'] = label_encoder.fit_transform(data['Gen'])

# Split the dataset into training and test sets
X = data[['Gen', 'Age']]
y = data[['Game1', 'Game2', 'Game3']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build and train the KNN model
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

name = input("Enter your name: ")
p = int(input("Your gender (0 for male 1 for female):"))
q = int(input("Your age: "))


# Predict game recommendations for a sample input
sample_input = pd.DataFrame([[p,q]], columns=['Gen', 'Age'])
sample_input['Gen'] = label_encoder.transform(sample_input['Gen'])  # Encode the gender
recommendations = classifier.predict(sample_input)


print( "Hey", name , "here are few Recommended games:")
for game in recommendations[0]:
    print(game)



