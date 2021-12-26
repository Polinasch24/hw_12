from pprint import pprint
import os
path = os.getcwd()
files = os.listdir(path)

data = {}
for file in files:
    if(file.endswith('.txt')):
        with open( file, encoding= 'utf-8') as f:
            lines = f.read()
            with open(file, encoding='utf-8') as f:
                file1 = f.name
                count = sum(1 for line in f)
            data[file1] = (count,lines)


    sorted_dict = {}
    sorted_keys = sorted(data, key=data.get)
       
    for i in sorted_keys:
             sorted_dict[i] = data[i]

             for j in sorted_dict.items():
               one_f = str(j[0])
               two_f = str(j[1][0])
               three_f = str(j[1][1])

               print(one_f)
               print(two_f)
               print(three_f)


#
