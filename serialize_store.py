import time
import pickle
import ipfsApi

start = time.time()  # start time

FILE = "./data/1mb.txt"
OUT_FILE = "./serialized_text.txt"

api = ipfsApi.Client('127.0.0.1', 5001)
# # Serialization
with open(FILE, "rb") as f:
    file = f.read()
    data = pickle.dumps(file)

end_serialization = time.time()
print("Elapsed time to serialize is  {}".format(end_serialization - start))

with open(OUT_FILE, "wb") as f2:
    f2.write(data)

# Store to IPFS/ central server
file_hash = api.add(OUT_FILE)
print(api)
end_upload = time.time()

print(file_hash)

print("Total elapsed time (serialization + storage) is  {}".format(end_upload - start))


