import pandas as pd
import subprocess

test = pd.read_csv('test.tsv', header=0, delimiter='\t', quoting=3)
index = 0
for review in test['review']:
    if index % 100 == 0:
        print(index)
    raw_review = review.replace('"', '')
    words = raw_review.lower()
    stemmed_words = []
    cmd = ['java', '-jar', 'stempel-1.0.jar',  words]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = process.communicate()
    out = str(out[0], 'utf-8')
    test.loc[index, 'review'] = '\"' + out + '\"'
    index += 1
output_filename = 'test_stemmed.tsv'
test.to_csv(output_filename, index=False, quoting=3)
print('------------------------------------------')
index = 0
train = pd.read_csv('training.tsv', header=0, delimiter='\t', quoting=3)
for review in train['review']:
    if index % 100 == 0:
        print(index)
    raw_review = review.replace('"', '')
    words = raw_review.lower()
    stemmed_words = []
    cmd = ['java', '-jar', 'stempel-1.0.jar',  words]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = process.communicate()
    out = str(out[0], 'utf-8')
    train.loc[index, 'review'] = '\"' + out + '\"'
    index += 1
output_filename = 'training_stemmed.tsv'
train.to_csv(output_filename, index=False, quoting=3)
