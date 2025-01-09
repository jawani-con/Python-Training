data = data2 = ""

# Reading data from file1
with open('data1.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('data2.txt') as fp:
    data2 = fp.read()

data += "\n"
data += data2

with open ('output_merge.txt', 'w') as fp:
    fp.write(data)
