import time

start = time.time()  # start time

# Serialization

end_serialization = time.time()
print("Elapsed time to serialize is  {}".formatend_serialization - start))

# Store to IPFS/ central server

end_upload = time.time()
print("Total elapsed time (serialization + storage) is  {}".format(end - start))


