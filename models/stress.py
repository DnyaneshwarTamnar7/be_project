def result(lst):
    import pandas as pd
    df=pd.read_csv("./datasets/stress.csv")
    x=df.drop(['Score','Result'],axis=1)
    y=df['Result']
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=42)
    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier(n_neighbors=11)
    knn.fit(x_train,y_train)
    y_pred=knn.predict([lst])
    return y_pred[0]
