from re import A
from turtle import xcor
import xdrlib
from zipfile import ZIP_BZIP2
import numpy as np
from PIL import Image
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep
import time


#geting the image data
img_data = Image.open('2.png')
CorrectChoice=1
img_arr = np.array(img_data)
TotalSize_arr=(img_arr.size)
new_a = ((np.sum(img_arr, axis=2))/4)/300
new_a=np.concatenate(new_a, axis=0 )
TotalSize_arr=(new_a.size)
#print(img_arr)
#print(new_a)
#print(TotalSize_arr)



newList=[]
def aU(Z):
    for i in range(0, TotalSize_arr):
        print(Z[i])
        if Z[i]>0:
            newList.append(1)
        else:
            newList.append(0)
    return newList

new_a=aU(new_a)
print(new_a)

new_a = np.array(new_a)

def ReLU(Z):
    return np.maximum(Z, 0.0)
    
data_dev = new_a[0:TotalSize_arr].T
Y_dev = data_dev[0]
X_dev = data_dev[0]
X_dev = X_dev / 255.

data_train = new_a[0].T
Y_train = data_train
X_train = data_train
X_train = X_train / 255.

def init_params():
    W1 = np.random.rand(10, TotalSize_arr) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2


def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    #print(Z1)
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def get_predictions(A2):
    return np.argmax(A2, 0)

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def test_prediction(index, W1, b1, W2, b2):
    current_image = (X_train[index])[:, None]
    prediction = make_predictions((X_train[index])[:, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()

def ReLU_deriv(Z):
    return Z > 0

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    #print(one_hot_Y)
    dZ2 = A2 - one_hot_Y[0]
    dW2 = 1 / 1 * dZ2.dot(A1.T)
    db2 = 1 / 1 * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / 1 * dZ1.dot(X.T)
    db1 = 1 / 1 * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    return W1, b1, W2, b2
def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    #print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            print(get_accuracy(predictions, Y))
    return W1, b1, W2, b2

W1, b1, W2, b2 = gradient_descent(X_dev, Y_dev, 0.10, 1000)


def savedata(data,FileName,Type):
    np.save(Type+ "/" + str(FileName)+ ".npy",data)

arr1w=savedata(W1,"Weights1","Weights")
arr2w=savedata(W2,"Weights2","Weights")
arr1b=savedata(b1,"Bias1","Bias")
arr2b=savedata(b2,"Bias2","Bias")







