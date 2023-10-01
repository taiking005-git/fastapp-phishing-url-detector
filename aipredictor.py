import pickle
import numpy as np
from sklearn.neural_network import MLPClassifier

from featureExtractor import featureExtraction


async def predict_url(url):
    #Load the xgb model
    model = pickle.load(open("XGBoostClassifier.pickle.dat", "rb"))

    feature = featureExtraction(url)
    reshape_feature = feature.reshape(1,16)
    prediction = model.predict(reshape_feature)
    
    if prediction[0] == 1:
        return "phishing"
    else:
        return "legitimate"