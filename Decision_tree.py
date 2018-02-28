"""This is the decision tree algorithm that classifies whether or not a person is male or female given their age,height,weight, and shoe size"""
from sklearn import tree


#[age,height,weight,shoe size]

x = [19,183,75,46],[21,153,63,37],[32,154,58,39],[20,190,85,47],[34,170,69,40],[23,178,77,43],[30,167,80,37],[23,163,55,41],[31,195,93,48],[29,174,78,42],[25,185,81,45],[28,169,66,39]

#gender: male/female relative to the measurements
y = ['male','female','female','male','male','female','female','male','female','male','male','female']

clf = tree.DecisionTreeClassifier() #the algorithm is stored in the clf variable

clf = clf.fit(x,y) #the model is trained here

prediction = clf.predict([[19,183,61,46]]) 

print (prediction)