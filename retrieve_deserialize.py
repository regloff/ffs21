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

PICKLE_FILE_HASH = "QmfGEcjpNkDJtqae7JZmXMf4NRu7Uu6GNf1PMVnfqPjsRZ"
PICKLE_IMG_HASH = "QmQWgYQphs8NM1RfWr2UmhEd7f1UjN9RfP46R24g8neSvB"
CSV_FILE_HASH = "Qmb6WHfMmp3E85P26D1qjVeXbNYrTSHyjGW1jAqkhNuV2c"

def plot_time_elapsed_serialize_text(t_t_pickle, t_t_csv, file_type):
    x = [i for i in range(len(t_t_pickle))]

    plt.plot(x, t_t_pickle, label="PICKLE {} deserialization".format(file_type))
    plt.plot(x, t_t_csv, label="CSV {} deserialization".format(file_type))

    plt.title("Time elapsed to retrieve and deserialize for {}".format(file_type))
    plt.xlabel("# run")
    plt.ylabel("time")

    plt.legend()
    plt.savefig("deserialization.png")
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
            data = pickle.loads(out_file.read())
            with open(f"{document}", "w") as f:
                f.write(str(data))
        if type == "json":
            data = json.loads(out_file.read())["data"]
            with open(f"{document}", "w") as f:
                f.write(data)
        elif type == "csv":
            data = b''
            for line in out_file.readlines():
                data += line
            with open(f"{document}", "wb") as f:
                f.write(data)

        out_file.close()
        end = time.time()

        t_d.append(end - start2)
        t_t.append(end - start1)
        print("Run {}: deserialize {}, total {}".format(i + 1, round(t_d[i], 8), round(t_t[i], 8)))
    print("Avg: deserialize {}, total {}".format(np.mean(t_d), np.mean(t_t)))
    return t_t


# run_measurement(PICKLE_FILE_HASH, 10, "pickle")
print("---------------")
# run_measurement(PICKLE_FILE_HASH, 10, "json")

tt_csv = run_measurement(CSV_FILE_HASH, 10, "csv")
tt_pickle = run_measurement(PICKLE_FILE_HASH, 10, "pickle")


    # try with random numbers
plot_time_elapsed_serialize_text(tt_pickle, tt_csv, "text")