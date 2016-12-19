import os
import re
import sys

if not os.path.exists('sorted_data'):
    os.mkdir('sorted_data')
if not os.path.exists('./sorted_data/1'):
    os.mkdir('./sorted_data/1')
if not os.path.exists('./sorted_data/2'):
    os.mkdir('./sorted_data/2')
if not os.path.exists('./sorted_data/3'):
    os.mkdir('./sorted_data/3')
if not os.path.exists('./sorted_data/4'):
    os.mkdir('./sorted_data/4')
if not os.path.exists('./sorted_data/5'):
    os.mkdir('./sorted_data/5')
if not os.path.exists('./sorted_data/6'):
    os.mkdir('./sorted_data/6')
if not os.path.exists('./sorted_data/7'):
    os.mkdir('./sorted_data/7')
if not os.path.exists('./sorted_data/8'):
    os.mkdir('./sorted_data/8')
if not os.path.exists('./sorted_data/9'):
    os.mkdir('./sorted_data/9')
if not os.path.exists('./sorted_data/10'):
    os.mkdir('./sorted_data/10')

directories_count = [0] * 11
for i in range(1, 10668):
    with open('./data/' + str(i), 'r') as f:
        read_text = f.read()
        rating = re.search(r'<reviewer_mark>\n(..?)\n', read_text)
        if not rating:
            print(str(i))
            sys.exit('exit')
        rating = rating.group(1)
        directories_count[int(rating)] += 1

        if rating == '1':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '2':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '3':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '4':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '5':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '6':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '7':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '8':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '9':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
        elif rating == '10':
            with open('./sorted_data/' + rating + '/' + str(directories_count[int(rating)]), 'w',
                      encoding='utf8') as outfile:
                outfile.write(read_text)
print(directories_count)
# directories_count = [170, 249, 510, 646, 1026, 1606, 2112, 2053, 1290, 1005]