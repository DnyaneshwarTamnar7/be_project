#import pandas library
import pandas as pd

#anxiety prediction algorithm or model
def result_anxiety(lst):

    #reading anxiety dataset using pandas
    df=pd.read_csv("./datasets/anxiety.csv")
    x=df.drop(['Result'],axis=1)
    y=df['Result']

    #importing train_test_split model to split dataset in training and testing part
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=42)

    #importing multiclass classifier Nearest Neighbor
    from sklearn.neighbors import KNeighborsClassifier

    #initializing neighbors class
    knn=KNeighborsClassifier(n_neighbors=11)

    knn.fit(x_train,y_train)
    y_pred=knn.predict([lst])

    return y_pred[0]

#depression prediction algorithm or model
def result_depression(lst):

    #reading depression dataset using pandas
    df=pd.read_csv("./datasets/depression.csv")
    x=df.drop(['Result'],axis=1)
    y=df['Result']

    #importing train_test_split model to split dataset in training and testing part
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=42)

    #importing multiclass classifier Nearest Neighbor
    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier(n_neighbors=11)

    knn.fit(x_train,y_train)
    y_pred=knn.predict([lst])

    return y_pred[0]

#stress prediction algorithm or model
def result_stress(lst):

    #reading stress dataset using pandas
    df=pd.read_csv("./datasets/stress.csv")
    x=df.drop(['Result'],axis=1)
    y=df['Result']

    #importing train_test_split model to split dataset in training and testing part
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=42)

    #importing multiclass classifier Nearest Neighbor
    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier(n_neighbors=11)

    knn.fit(x_train,y_train)
    y_pred=knn.predict([lst])
    
    return y_pred[0]