# Author: Rahul Mehta
# Date: July 31, 2019

#[START IMPORTS]
import csv
#[END IMPORTS]

def array_creator():
    r = csv.reader(open('raceData2.csv'))
    lines = list(r)
    return lines

def convert_native_values(arr):
    x = arr.copy()
    for index in range(len(arr)):
        print (x[index])
        x[index][1] = int(x[index][1])
        x[index][2] = int(x[index][2])
        x[index][3] = float(x[index][3])
        x[index][4] = float(x[index][4])
        x[index][5] = float(x[index][5])
        x[index][6] = int(x[index][6])
        if len(x[index]) == 8:
            x[index][7] = int(x[index][7])
    return x

def dict_creator(array):
    dict_ = {}
    for item in array:
        if item[1] in dict_:
            dict_[item[1]].append(item[5])
        else:
            dict_[item[1]] = [item[5]]
    return dict_

def dict_creator_min(dict_):
    _dict = {}
    for key, value in dict_.items():
        _dict[key] = min(value)
    return _dict

def insert_normalized_times(array, dic):
    final_copy = array.copy()
    for index in range(len(array)):
        min_time = dic[array[index][1]]
        final_copy[index].insert(6, ((array[index][5])/min_time))
    return (final_copy)

def write_to_csv(final):
    with open("normalized_race_data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(final)

race_data = array_creator()
race_data = convert_native_values(race_data)
dict_ = dict_creator(race_data)
min_times = dict_creator_min(dict_)
final_copy = insert_normalized_times(race_data, min_times)
write_to_csv(final_copy)
