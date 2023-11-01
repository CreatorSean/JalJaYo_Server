import numpy as np
import pickle

def sleep_wake_classification(subject_id):
    print("subject_id: ", subject_id)
    subject_path = "processed_data/{}/feature.csv".format(subject_id)

    test_data = np.loadtxt(subject_path, delimiter=",")
    print("test_data shape{}".format(test_data.shape) )

    # shuffle data
    np.random.shuffle(test_data)

    # split x and y
    x_test = test_data[:, 1:]
    y_test = test_data[:, 0]

    # load modelE
    with open("rf_model", "rb") as f:
        clf = pickle.load(f)

    # predict
    sleep_list = clf.predict(x_test)

    # sleep indicators
    # 잠이 든 순간부터 깨기 전까지
    sleep_data = sleep_list[(sleep_list != 0).argmax() :][::-1][
        (sleep_list[::-1] != 0).argmax() :
    ][::-1]

    sleep_time = len(sleep_data) * 30

    # WASO(sec)
    find_WASO = np.where(sleep_data == 0.0)
    WASO = len(find_WASO[0]) * 30

    # TST(sec)
    TST = (len(sleep_data) * 30) - WASO

    # SE(%)
    SE = TST / sleep_time * 100

    print("WASO: ", WASO)
    print("TST: ", TST)
    print("SE: ", SE)

    sleep_dict = {"sleep_list": sleep_list.tolist(), "tst_hour" : TST//3600, "tst_minute" : (TST//60)%60, "waso_minute": WASO//60, "se: ": SE}

    return sleep_dict


