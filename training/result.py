from training.setup import text_preprocess , remove_stopwords
import pickle, joblib, os
MODEL_PATH = "training/models"
# from slit import nb_model,label_encoder

# xem kết quả cho 1 văn bản model naive bayes đã load ở trên
# document = "Tui tự hỏi liệu các bạn có ghen khi thấy người yêu mình lo cho người yêu cũ như này không"

def predict(document):
    document = text_preprocess(document)
    document = remove_stopwords(document)

    model = pickle.load(open(os.path.join(MODEL_PATH,"naive_bayes.pkl"), 'rb'))
    label = model.predict([document])

    label_encoder = joblib.load('training/label_encoder.joblib')
    return label_encoder.inverse_transform(label)[0]


# print('Predict label:', predict("Tui tự hỏi liệu các bạn có ghen khi thấy người yêu mình lo cho người yêu cũ như này không"))