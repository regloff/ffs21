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

FILE = "testfile.txt"
IMG = "logo.png"


# type:"text", "image"
def plot_time_elapsed_serialize_text(t_t_pickle, t_t_csv, file_type):
    x = [i for i in range(len(t_t_pickle))]

    plt.plot(x, t_t_pickle, label="Pickle {} serialization".format(file_type))
    plt.plot(x, t_t_csv, label="CSV {} serialization".format(file_type))

    plt.title("Time elapsed to serialize and store for {}".format(file_type))
    plt.xlabel("# run")
    plt.ylabel("time")

    plt.legend()
    plt.show()


def run_measurement(document, runs, type):

    t_s = []
    t_t = []

    print("Running measurements for {} with {} serialization".format(document, type))
    for i in range(runs):

        start = time.time()

        # serialize
        in_file = open(os.path.join(sys.path[0], document), "rb")
        if type == "pickle":
            serialized = pickle.dumps(in_file.read())

        in_file.close()
        end1 = time.time()

        # upload to ipfs
        res = client.add_bytes(serialized)
        end2 = time.time()

        t_s.append(end1 - start)
        t_t.append(end2 - start)
        print("Run {}: serialize {}, total {}".format(i+1, round(t_s[i], 8), round(t_t[i], 8)))
    print("Avg: serialize {}, total {}".format(np.mean(t_s), np.mean(t_t)))
    print(res)

run_measurement(FILE, 10, "pickle")
print("---------------")
run_measurement(IMG, 10, "pickle")

# try with random numbers
plot_time_elapsed_serialize_text([1.3, 1.6, 0.04, 3.66, 4.52, 0.02], [0.34, 4.09, 5.23, 7.32, 0.01, 6.4], "text")