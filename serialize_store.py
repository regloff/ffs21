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

FILE = "testfile.txt"
IMG = "bunny.jpg"

def run_measurement(document, runs, type):

    t_s = []
    t_t = []

    print("Running measurements for {} with {} serialization".format(document, type))
    for i in range(runs):

        start = time.time()

        # serialize
        in_file = open(os.path.join(sys.path[0], document), "rb")
        if type == "json":
            serialized = bytes(json.dumps({"data": str(in_file.read())}), encoding="utf-8")
        if type == "csv":
            serialized = b""
            for line in in_file.readlines():
                serialized += line
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

# run_measurement(FILE, 10, "pickle")
print("---------------")
run_measurement(FILE, 10, "json")