from glob import glob
import numpy as np
import pickle
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier

glob_path = "processed_data/*/feature.csv"

train_data = []
for data_path in glob(glob_path):
    new_data = np.loadtxt(data_path, delimiter=",")
    if len(train_data) == 0:
        train_data = new_data
    else:
        train_data = np.concatenate([train_data, new_data], axis=0)

print("train_data shape: {}".format(train_data.shape))

print("shuffle data...")

# shuffle data
np.random.shuffle(train_data)

# split x and y
x_train = train_data[:, 1:]
y_train = train_data[:, 0]

# do SMOTE to balance data
sm = SMOTE(random_state=42)
x_res, y_res = sm.fit_resample(x_train, y_train)

x_train = x_res
y_train = y_res

print("train data shape (after SMOTE): {}".format(x_train.shape))

clf =  RandomForestClassifier(
        random_state = 42,
        n_estimators = 1000,
        n_jobs=-1,
    )

 # train model
print("training rf model...")
clf.fit(x_train, y_train,)

# save model
print("save model...")
with open("rf_model", "wb") as f:
    pickle.dump(clf, f)

print("save done!")