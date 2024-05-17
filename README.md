

---

# Video Game Recommendation System

## Overview
This system utilizes machine learning techniques to recommend video games based on user demographics. It employs the K-Nearest Neighbors algorithm to predict suitable game recommendations for users based on their gender and age.

## Files
- **game_data1.csv**: This CSV file contains the dataset used for training the recommendation system. It includes information about different games, such as their genres, and the target audience's age group.
- **game_rec.py**: This Python script contains the code for loading the dataset, preprocessing the data, training the KNN model, and generating game recommendations based on user input.

## Setup
1. Ensure you have Python installed on your system.
2. Install the required Python packages by running:
   ```
   pip install pandas scikit-learn
   ```
3. Download the provided CSV file (`game_data1.csv`) and place it in the same directory as `game_rec.py`.

## Usage
1. Run the `game_rec.py` script.
2. Enter your name, gender (0 for male, 1 for female), and age when prompted.
3. The system will generate recommended games based on your input and display them on the console.

## Code Overview
- The script loads the dataset from `game_data1.csv` and encodes categorical features using LabelEncoder.
- It splits the dataset into training and test sets using a 80-20 split.
- The KNN model is built and trained using the training data.
- User input for name, gender, and age is taken, and game recommendations are generated based on this input.

## Example Usage
```
python game_rec.py
```
```
Enter your name: John
Your gender (0 for male 1 for female): 0
Your age: 25
```
```
Hey John, here are a few Recommended games:
Fortnite
Call of Duty
Minecraft
```

---
