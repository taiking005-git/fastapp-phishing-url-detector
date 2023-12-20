import pickle

from featureExtractor import featureExtraction, checkIsOnline


async def predict_url(url):
    # Load the xgb model
    model = pickle.load(open("XGBoostClassifier.pickle.dat", "rb"))

    if checkIsOnline():
        feature = featureExtraction(url)
        reshape_feature = feature.reshape(1, 16)
        print(reshape_feature)
        prediction = model.predict(reshape_feature)
        print(prediction)
        if prediction[0] == 1:
            return "phishing"
        else:
            return "legitimate"
    else:
        return "An error occur while connecting to the Internet!"
