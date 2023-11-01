from glob import glob
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score

glob_path = "processed_data/*/feature.csv"

data_bunch = []
for data_path in glob(glob_path):
    new_data = np.loadtxt(data_path, delimiter=",")
    if len(data_bunch) == 0:
        data_bunch = new_data
    else:
        data_bunch = np.concatenate([data_bunch, new_data], axis=0)


print("data bunch shape: {}".format(data_bunch.shape))

print("shuffle and split data...")
# shuffle data
np.random.shuffle(data_bunch)

# split data
train_data = data_bunch[: int(len(data_bunch) * 0.8)] 
test_data = data_bunch[int(len(data_bunch) * 0.8) :] 
# split x and y
x_train = train_data[:, 1:]
y_train = train_data[:, 0]

# do SMOTE to balance data
sm = SMOTE(random_state=42)
x_res, y_res = sm.fit_resample(x_train, y_train)

x_train = x_res
y_train = y_res

print("train data shape (after SMOTE): {}".format(x_train.shape))

x_test = test_data[:, 1:]
y_test = test_data[:, 0]

print("test data shape: {}".format(x_test.shape))

clf =  RandomForestClassifier(
        random_state = 42,
        n_estimators = 1000,
        n_jobs=-1,
    )

 # train model
print("training rf model...")
clf.fit(x_train, y_train,)

# test model
print("rf test result as below:")
print("accuracy: {}".format(clf.score(x_test, y_test)))

y_pred = clf.predict(x_test)

# specificity and sensitivity
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("specificity: {}".format(tn / (tn + fp)))
print("sensitivity: {}".format(tp / (tp + fn)))

# F1 score
print("F1 score: {}".format(f1_score(y_test, y_pred, average = "weighted")))