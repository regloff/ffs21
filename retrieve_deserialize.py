# ipfs: 0.8.0
# ipfshttpclient: pip install ipfshttpclient==0.8.0a2

import ipfshttpclient
import sys
import pickle
import time
import os
import numpy as np
import matplotlib.pyplot as plt

client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")

PICKLE_FILE_HASH = "QmVaeSaXaeMw5XFgibRUBD45LRYbuprQtYMEdWy1aZN3qB"
PICKLE_IMG_HASH = "QmZMHFcNFEknmjtTLpUX8pKvrasfWHYSxLRB2yQawfsiCp"


def plot_time_elapsed_serialize_text(t_t_pickle, t_t_csv, file_type):
    x = [i for i in range(len(t_t_pickle))]

    plt.plot(x, t_t_pickle, label="Pickle {} deserialization".format(file_type))
    plt.plot(x, t_t_csv, label="CSV {} deserialization".format(file_type))

    plt.title("Time elapsed to retrieve and deserialize for {}".format(file_type))
    plt.xlabel("# run")
    plt.ylabel("time")

    plt.legend()
    plt.show()


def run_measurement(document, runs, type):

    t_d = []
    t_t = []

    print("Running measurements for {} with {} serialization".format(document, type))
    for i in range(runs):

        start1 = time.time()

        # download from ipfs
        client.get(document)
        start2 = time.time()

        # deserialize
        out_file = open(os.path.join(sys.path[0], document), "rb")
        if type == "pickle":
            serialized = pickle.loads(out_file.read())
        elif type == "numpy":
            serialized = np.frombuffer(out_file.read())
        out_file.close()
        end = time.time()

        t_d.append(end - start2)
        t_t.append(end - start1)
        print("Run {}: deserialize {}, total {}".format(i+1, round(t_d[i], 8), round(t_t[i], 8)))
    print("Avg: deserialize {}, total {}".format(np.mean(t_d), np.mean(t_t)))

run_measurement(PICKLE_FILE_HASH, 10, "pickle")
print("---------------")
run_measurement(PICKLE_IMG_HASH, 10, "pickle")