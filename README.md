# ffs21

## Answers to exercise questions

The csv serialization performed worse than pickle. The input file is unstructured data, therefore we decided to add a comma at the end of each line to get a csv file. To do this, we have to loop over all lines of the input file. We assume that pickle is much more optimized compared to this iterative approach. Therefore, the csv serialization took longer than pickle.

---

Applying pickle serialization and csv serialization increase the file size. In case of pickle more than csv. For larger files, we were only able to serialize the file using pickle, as our csv serialization approach took forever. Therefore, this question remains unanswered.

---

For the 1Mb file, the centralized approach was faster than the decentralized approach due to overhead. To download the 1Gb file in the decentralized approach took forever in our case. But from what we have learned, the larger the file is, the better suited the decentralized approach should be. However, several factors, like the server load could affect the results.

---

Rating: 7/10

The approach is well documented and the installation was easy. However, the used APIs in python were outdated and not so well documented. We had to try out multiple versions until it finally worked. What was further helpful is that even if it is an experimental approach, we were able to find multiple resources discussing it on the internet. However, we perceive IPFS still as kind of a "blackbox". As a user, it is not so clear what happens after adding a file to the network, as this process is not transparent.
