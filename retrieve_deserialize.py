import time
import pickle
import ipfsApi

# >>> api = ipfsApi.Client('127.0.0.1', 5001)

start = time.time()  # start time


# Retrieve the files from IPFS/ central server

end_serialization = time.time()
print("Elapsed time to retrive the file is  {}".formatend_serialization - start))

# Deserialize
# file = IPFS_DOWNLOAD
data = pickle.dumps(file)

end_upload = time.time()
print("Total elapsed time (retrieval + deserialization) is {}".format(end_upload - start))


