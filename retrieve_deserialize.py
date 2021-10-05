import time
import pickle
import ipfsApi

api = ipfsApi.Client('127.0.0.1', 5001)

start = time.time()  # start time


# Retrieve the files from IPFS/ central server
file = api.get("QmQz3ivr2YaRDAHwGbw12ULWCXpYgXUf6aVob7NehmKrYG")

end_download = time.time()
print("Elapsed time to retrive the file is  {}".format(end_download - start))

# Deserialize
data = pickle.loads(file)

end_upload = time.time()
print("Total elapsed time (retrieval + deserialization) is {}".format(end_upload - start))

print(data)


