import time

start = time.time()  # start time

# Retrieve the files from IPFS/ central server

end_serialization = time.time()
print("Elapsed time to retrive the file is  {}".formatend_serialization - start))

# Deserialize

end_upload = time.time()
print("Total elapsed time (retrieval + deserialization) is {}".format(end - start))


