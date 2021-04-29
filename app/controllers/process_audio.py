import pandas as pd 
import numpy as np
import scipy.stats as ss
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def process_data(filename):
    print('read csv')
  
    data = pd.read_csv(filename,sep=';|,')
    data = data.iloc[:,1:]
    feats = []
    count = 1
    for col in data:
        count = count+1
        feats.append(data[col].mean())
    return feats
    
   
def predict(feats):
    # print(data.iloc[:,1:].shape)
    scalar = StandardScaler()
    train = pd.read_csv('app/dataset/train.csv',sep=';|,')
    train_x = train.iloc[:,2:]
    scalar.fit(train_x)
    feats = np.array([feats])
    
    feats = scalar.transform(feats)
    print(feats)
    print(feats.shape)
    # pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score = pickle.load(open("tuple_model.pkl", 'rb'))
    
    model = pickle.load(open('app/svm-ll-withoutstats-all-feats.pkl','rb'))
    print('-------------PIckele train---------')
    print()
    result = model.predict_proba(feats)
    print(result)
    return result


    # print(result)
    # print(feats.shape)