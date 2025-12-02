#Name: Caden Hanscom
#Date: 12/2/2025
#Description: Hashing useing mid-squared


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

#converts to ASCII and adds to total key then squares the key, 
#extracts the middle 5 digits then modulos table size for valid index
def hashFunction(stringData):
    key = 0
    for ch in stringData:
        key += ord(ch)

    squared_key = key * key
    squared_str = str(squared_key)

    mid_digits = 5
    if len(squared_str) <= mid_digits:
        mid_num = int(squared_str)
    else:
        mid_start = (len(squared_str) - mid_digits) // 2
        mid_num = int(squared_str[mid_start:mid_start + mid_digits])

    table_size = 10000
    idx = mid_num % table_size
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
    print("Optimization Attempt: Mid-squared hashing")
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