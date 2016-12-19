import os
import re

import sys

test_dir = './test_set/'
training_dir = './training_set/'

test_data_count = 2131
training_data_count = 8536


def clear_review(review_text):
    review_text = re.sub('[^a-zA-ZąĄćĆęĘłŁńŃóÓśŚźŹżŻ]', ' ', review_text)
    review_text.replace('  ', ' ')

    return review_text

test_csv_string = 'id\trating\treview\n'
training_csv_string = 'id\trating\treview\n'

test_word_count = 0
for i in range(1, test_data_count+1):
    with open(test_dir + str(i), 'r') as f:
        if i == 68:
            print("")
        read_text = f.read()
        rating = re.search(r'<reviewer_mark>\n*(..?)\n', read_text).group(1)
        if rating == '':
            sys.exit('no rating')
        review_text = re.search(r'<review>\n*(.*)', read_text).group(1)
        review_text = clear_review(review_text)
        if review_text == '':
            sys.exit('no review text')
        test_word_count += len(review_text.split(' '))
        row = '"' + str(i) + '"\t' + rating + '\t"' + review_text + '"\n'
        test_csv_string += row

print(test_word_count)
training_word_count = 0
for i in range(1, training_data_count+1):
    with open(training_dir + str(i), 'r') as f:
        read_text = f.read()
        rating = re.search(r'<reviewer_mark>\n*(..?)\n', read_text).group(1)
        if rating == '':
            sys.exit('no rating')
        review_text = re.search(r'<review>\n*(.*)', read_text).group(1)
        review_text = clear_review(review_text)
        if review_text == '':
            sys.exit('no review text')
        training_word_count += len(review_text.split(' '))
        row = '"' + str(i) + '"\t' + rating + '\t"' + review_text + '"\n'
        training_csv_string += row

print(training_word_count)

test_csv_path = './test.tsv'
if not os.path.exists(test_csv_path):
    with open(test_csv_path, 'w', encoding='utf8') as outfile:
        outfile.write(test_csv_string)

training_csv_path = './training.tsv'
if not os.path.exists(training_csv_path):
    with open(training_csv_path, 'w', encoding='utf8') as outfile:
        outfile.write(training_csv_string)

# test_word_count = 203966
# training_word_count = 816311
