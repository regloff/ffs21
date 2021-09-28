import time
import pickle

start = time.time()  # start time
FILE = "/data/1mb.txt"

# Serialization
data = b""
with open (FILE, "rb") as f:
    data = pickle.loads(f.read())

end_serialization = time.time()
print("Elapsed time to serialize is  {}".formatend_serialization - start))

# Store to IPFS/ central server

end_upload = time.time()
print("Total elapsed time (serialization + storage) is  {}".format(end - start))


