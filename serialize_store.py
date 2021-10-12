# ipfs: 0.8.0
# ipfshttpclient: pip install ipfshttpclient==0.8.0a2
import json

import ipfshttpclient
import sys
import pickle
import time
import os
import numpy as np
import matplotlib.pyplot as plt

client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")

FILE = "testfile.txt"
IMG = "bunny.jpg"


# type:"text", "image"
def plot_time_elapsed_serialize_text(t_t_pickle, t_t_csv, file_type):
    x = [i for i in range(len(t_t_pickle))]

    plt.plot(x, t_t_pickle, label="Pickle {} serialization".format(file_type))
    plt.plot(x, t_t_csv, label="CSV {} serialization".format(file_type))

    plt.title("Time elapsed to serialize and store for {}".format(file_type))
    plt.xlabel("# run")
    plt.ylabel("time")

    plt.legend()
    plt.savefig("Serialization.png")
    plt.show()

def plot_time_elapsed_serialize_image(x_array, t_t_csv, file_type):
    x = [i for i in range(len(x_array))]

    plt.plot(x, t_t_csv, label="CSV {} serialization".format(file_type))

    plt.title("Time elapsed to serialize and store for {}".format(file_type))
    plt.xlabel("# run")
    plt.ylabel("time")

    plt.legend()
    plt.savefig("img.png")
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
        if type == "json":
            serialized = bytes(json.dumps({"data": str(in_file.read())}), encoding="utf-8")
        if type == "csv":
            serialized = b""
            for line in in_file.readlines():
                serialized += line + b','
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
    return t_t

# run_measurement(FILE, 10, "pickle")
print("---------------")
# run_measurement(FILE, 10, "json")
serializations = ["csv", "pickle"]

tt_csv = run_measurement(FILE, 10, "csv")
tt_pickle = run_measurement(FILE, 10, "pickle")
tt_img = run_measurement(IMG, 10, "csv")

# try with random numbers
p1 = plot_time_elapsed_serialize_text(tt_pickle, tt_csv, "text")
p2 = plot_time_elapsed_serialize_image([0] * len(tt_img),tt_img, "image")

