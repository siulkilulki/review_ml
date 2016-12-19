import os
import shutil
from random import shuffle

if not os.path.exists('training_set'):
    os.mkdir('training_set')
if not os.path.exists('test_set'):
    os.mkdir('test_set')


# def count_dir_files(dir):
#     return len([name for name in os.listdir(dir)])
test_list = [0] * 11
training_list = [0] * 11
test_data_counter = 0
training_data_counter = 0
for foldername in range(1, 11):
    directory = './sorted_data/' + str(foldername)
    list_of_files = os.listdir(directory)
    shuffle(list_of_files)
    nr_of_test_files = len(list_of_files)*0.2
    counter = 0

    for filename in list_of_files:
        counter += 1
        src = directory + '/' + filename
        if counter <= nr_of_test_files:
            test_data_counter += 1
            test_list[foldername] += 1
            shutil.copyfile(src, './test_set/' + str(test_data_counter))
        else:
            training_data_counter += 1
            training_list[foldername] += 1
            shutil.copyfile(src, './training_set/' + str(training_data_counter))


print(training_list)
print(test_list)

#[136, 200, 408, 517, 821, 1285, 1690, 1643, 1032, 804]
#[34, 49, 102, 129, 205, 321, 422, 410, 258, 201]
