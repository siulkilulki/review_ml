import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC


def review_to_words(raw_review):
    #to lower-case and list of words
    raw_review = raw_review.replace('"', '')
    words = raw_review.lower().split()
    #remove stopwords
    meaningful_words = words
    #meaningful_words = [w for w in words if not w in stopwords]

    # todo: stemm
    return " ".join(meaningful_words)

with open('stopwords.txt', 'r') as f:
    stopwords = f.read()
    stopwords = set(stopwords.split('\n'))

train = pd.read_csv('training.tsv', header=0, delimiter='\t', quoting=3)

print(train.shape)
clean_train_reviews = []

print('cleaning training reviews...')

for review in train['review']:
    clean_train_reviews.append(review_to_words(review))

vectorizer = CountVectorizer(analyzer='word',
                             tokenizer=None,
                             preprocessor=None,
                             stop_words=None,
                             #ngram_range=(2, 3),
                             max_df=0.8,
                             max_features=5000)

train_data_features_counts = vectorizer.fit_transform(clean_train_reviews)

tf_transformer = TfidfTransformer(use_idf=False)
train_data_features = tf_transformer.fit_transform(train_data_features_counts)
train_data_features = train_data_features.toarray()

print(train_data_features.shape)
# vocab = vectorizer.get_feature_names()
# print(vocab)
# dist = np.sum(train_data_features, axis=0)
# for tag, count in zip(vocab, dist):
#     print(count, tag)

test = pd.read_csv('test.tsv', header=0, delimiter='\t', quoting=3)
test_rating_list = test['rating'].tolist()

print(test.shape)
clean_test_reviews = []

for review in test['review']:
    clean_test_reviews.append(review_to_words(review))


test_data_features_counts = vectorizer.transform(clean_test_reviews)
test_data_features = tf_transformer.transform(test_data_features_counts)
test_data_features = test_data_features.toarray()

C = 1.0
classifiers = {'L1_logistic': LogisticRegression(C=C, penalty='l1'),
               'L2_logistic_(OvR)': LogisticRegression(C=C, penalty='l2'),
                'rbf_SVC': SVC(kernel='rbf', C=C),
               'Linear_SVC': SVC(kernel='linear', C=C),
               'Random_Forest': RandomForestClassifier(n_estimators=100),
                'L2_logistic_(Multinomial)': LogisticRegression(
                C=C, solver='lbfgs', multi_class='multinomial')
               }

n_classifiers = len(classifiers)

for index, (name, classifier) in enumerate(classifiers.items()):
    print('Fitting ' + name + ' ...')
    classifier.fit(train_data_features, train['rating'])

    print('Predicting result...')
    result = classifier.predict(test_data_features)

    print('Saving to file...')
    output = pd.DataFrame(data={'id': test['id'], 'rating': result})
    output_filename = name + '_Result.csv'
    output.to_csv(output_filename, index=False, quoting=3)

    predicted_rating_list = output['rating'].tolist()
    mse = mean_squared_error(test_rating_list, predicted_rating_list)
    print('Mean square error of ' + name + ' is: ' + str(mse) + '\n')
