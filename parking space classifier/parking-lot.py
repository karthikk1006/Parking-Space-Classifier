import  os
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
#prepare data

input_dir=r"C:\Users\Karthik Krishna\Desktop\ComputerVision\Image classifier\parking space classifier\data\clf-data"
categories=["empty","not_empty"]


data=[]
labels=[]

for category_idx,category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir,category)):
        img_path=os.path.join(input_dir,category,file)
        img=imread(img_path)
        img=resize(img,(15,15))
        data.append(img.flatten())
        labels.append(category_idx)

data=np.asarray(data)
labels=np.asarray(labels)
print("success")


x_train,x_test,y_train,y_test=train_test_split(data,labels,test_size=0.2,shuffle=True,stratify=labels)

#use and train model
classifier=SVC()

parameters=[{'gamma':[0.01,0.001,0.0001],'C':[1,10,100,1000]}]
# for all possibilities of gamma and C that many image classifiers are created and trained and the best is chosen.

grid_search=GridSearchCV(classifier,parameters)

grid_search.fit(x_train,y_train)

#test the model


best_estimator=grid_search.best_estimator_

y_prediction=best_estimator.predict(x_test)

score=accuracy_score(y_test,y_prediction)


print('{} percentage of sample were correctly classified'.format(str(score*100)))

pickle.dump(best_estimator,open('./model.p','wsb'))