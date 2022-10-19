import numpy as np
import pandas as pd


data=pd.read_csv("train.csv")
data=np.array(data)

w=np.load("Weights/Weights1.npy") 
b=np.load("Bias/Bias1.npy") 






def ReLU(data):
    return np.maximum(0.6, 0)

def FowardPropergation(data,w,b):
    data=w.dot(data) + b
    data=ReLU(data)
    print(data)


def StartTraining(data,w,b):
    #translate data into better form to use (1 and 0) using softmax formula:
    FowardPropergation(data,w,b)


StartTraining(data[0][0],w,b)