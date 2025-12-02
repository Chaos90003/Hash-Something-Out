#Name: Caden Hanscom
#Date: 12/2/2025
#Description: XOR Hashing

import csv
import time


class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]

#Shifts the ASCII and XOR's into the key
def hashFunction(stringData):
    table_size = 10000
    key = 0

    for i, ch in enumerate(stringData):
        key ^= (ord(ch) << (i % 8))
    
    idx = key % table_size
    return idx

#Hash statistics
def stats(name, table, build_time):
    total_buckets = len(table)
    used_buckets = 0
    wasted_buckets = 0
    total_collisions = 0
     
    for bucket in table:
        if bucket is None:
            wasted_buckets += 1
        else:
            used_buckets += 1
            bucket_size = len(bucket)

            if bucket_size > 1:
                total_collisions += (bucket_size - 1)

    print(f"\nStats for {name}")
    print("Optimization Attempt: XOR Hashing")
    print(f"Used buckets: {used_buckets}")
    print(f"Wasted buckets: {wasted_buckets}")
    print(f"Total Collisions: {total_collisions}")
    print(f"Build time: {build_time:.6f} seconds")


# create empty hash tables
size = 10000 
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0

start = time.time()


#Title Hash Table
with open(file, 'r', newline='',  encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if counter == 0:
                counter += 1
                continue
            title = row[0]
            
            idx = hashFunction(title)

            if hashTitleTable[idx] is None:
                hashTitleTable[idx] = [title]
            else:
                hashTitleTable[idx].append(title)

            counter += 1

end = time.time()
buildTimeTitle = end - start

stats("Title Hash Table", hashTitleTable, buildTimeTitle)


counter = 0

start = time.time()


#Quote Hash Table
with open(file, 'r', newline='',  encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if counter == 0:
                counter += 1
                continue
            quote = row[-1]

            idx = hashFunction(quote)

            if hashQuoteTable[idx] is None:
                hashQuoteTable[idx] = [quote]
            else:
                hashQuoteTable[idx].append(quote)

            counter += 1
        
end = time.time()
buildTimeQuote = end - start

stats("Quote Hash Table", hashQuoteTable, buildTimeQuote)