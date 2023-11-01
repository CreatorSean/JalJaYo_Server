import numpy as np
import pickle

# subject_path = "processed_data/{subject_id}/feature.csv"
subject_path = "processed_data/46343/feature.csv"

test_data = np.loadtxt(subject_path, delimiter=",")
print("test_data shape{}".format(test_data.shape) )

# shuffle data
np.random.shuffle(test_data)

# split x and y
x_test = test_data[:, 1:]
y_test = test_data[:, 0]

print("test data shape: {}".format(x_test.shape))

with open("rf_model", "rb") as f:
    clf = pickle.load(f)

y_pred = clf.predict(x_test)
print(y_pred)