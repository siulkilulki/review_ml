import os
import re

test_dir = './test_set'


def calc_mse(value):
    sum = 0
    n = 0
    for file in os.listdir(test_dir):
        with open(test_dir + '/' + file) as review:
            read_text = review.read()
            reviewer_mark = re.search(r'<reviewer_mark>\n(..?)\n', read_text).group(1)
            reviewer_mark = int(reviewer_mark)
            sum += (reviewer_mark - value) ** 2
            n += 1
    mse = sum / n
    print('MSE for constant value ' + str(value) + ' is: ' + str(mse))

for default_value in range(1, 11):
    calc_mse(default_value)

# MSE for constant value 1 is: 38.00938526513374
# MSE for constant value 2 is: 27.427968090098545
# MSE for constant value 3 is: 18.84655091506335
# MSE for constant value 4 is: 12.265133740028157
# MSE for constant value 5 is: 7.683716564992961
# MSE for constant value 6 is: 5.102299389957766
# MSE for constant value 7 is: 4.520882214922572
# MSE for constant value 8 is: 5.939465039887377
# MSE for constant value 9 is: 9.358047864852182
# MSE for constant value 10 is: 14.776630689816987


