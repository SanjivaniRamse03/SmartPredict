import numpy as np 
from sklearn.model_selection import train_test_split

class MyReg:

    def __init__(self):
        self.coef = None
        self.intercept = None


    def fit(self,x_train,y_train):
        x_train = np.insert(x_train,0,1,axis = 1)

        coeff = np.linalg.inv(np.dot(x_train.T,x_train)).dot(x_train.T).dot(y_train)
        self.coef = coeff[1:]
        self.intercept = coeff[0]
        
    def predict(self,x_test):
        y_pred = np.dot(x_test,self.coef) + self.intercept
        return y_pred



def prediction_reg(X,y,input_list):
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 2)

    lr = MyReg()
    lr.fit(x_train,y_train)
    y_pred = lr.predict(input_list)
    y_pred = round(y_pred[0])
    return y_pred






