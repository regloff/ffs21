# ipfs: 0.8.0
# ipfshttpclient: pip install ipfshttpclient==0.8.0a2
import json

import ipfshttpclient
import sys
import pickle
import time
import os

import numpy as np

client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")

PICKLE_FILE_HASH = "QmPwsb72V1e6sfMFzQRf7Rf538xsy5zymhWqxm6QkUzRwa"
PICKLE_IMG_HASH = "QmQWgYQphs8NM1RfWr2UmhEd7f1UjN9RfP46R24g8neSvB"


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

        if type == "json":
            data = json.loads(out_file.read())["data"]
            with open(f"{document}", "w") as f:
                f.write(data)
        elif type == "csv":
            data = b''
            for line in out_file.readlines():
                data += line
            with open(f"{document}", "w") as f:
                f.write(data)

        out_file.close()
        end = time.time()

        t_d.append(end - start2)
        t_t.append(end - start1)
        print("Run {}: deserialize {}, total {}".format(i + 1, round(t_d[i], 8), round(t_t[i], 8)))
    print("Avg: deserialize {}, total {}".format(np.mean(t_d), np.mean(t_t)))


# run_measurement(PICKLE_FILE_HASH, 10, "pickle")
print("---------------")
run_measurement(PICKLE_FILE_HASH, 10, "json")
