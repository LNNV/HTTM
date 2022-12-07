# Chia tập train/test
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
test_percent = 0.2

text = []
label = []

for line in open('training/news_categories.prep',encoding="utf8"):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# Lưu train/test data
# Giữ nguyên train/test để về sau so sánh các mô hình cho công bằng
with open('training/train.txt', 'w',encoding="utf8") as fp:
    for x, y in zip(X_train, y_train):
        fp.write('{} {}\n'.format(y, x))

with open('training/test.txt', 'w',encoding="utf8") as fp:
    for x, y in zip(X_test, y_test):
        fp.write('{} {}\n'.format(y, x))


# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
import joblib
joblib.dump(label_encoder, 'training/label_encoder.joblib')
# print(list(label_encoder.classes_), '\n')
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

# print(X_train[0], y_train[0], '\n')
# print(X_test[0], y_test[0])

MODEL_PATH = "training/models"

import os
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
import pickle
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

start_time = time.time()
text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                             max_df=0.8,
                                             max_features=None)), 
                     ('tfidf', TfidfTransformer()), 
                     ('clf', MultinomialNB())
                    ])
text_clf = text_clf.fit(X_train, y_train)

train_time = time.time() - start_time
print('Done training Naive Bayes in', train_time, 'seconds.')

# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "naive_bayes.pkl"), 'wb'))
# pickle.dump(label_encoder, open(os.path.join('label_encoder.pkl')), 'wb')
nb_model = pickle.load(open(os.path.join(MODEL_PATH,"naive_bayes.pkl"), 'rb'))


# evaluate
# import numpy as np
# # Naive Bayes
# model = pickle.load(open(os.path.join(MODEL_PATH,"naive_bayes.pkl"), 'rb'))
# y_pred = model.predict(X_test)
# print('Naive Bayes, Accuracy =', np.mean(y_pred == y_test))
# # Xem kết quả trên từng nhãn
# from sklearn.metrics import classification_report


# y_pred = nb_model.predict(X_test)
# print(classification_report(y_test, y_pred, target_names=list(label_encoder.classes_)))
