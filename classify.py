from sklearn import tree

#[height, weight, shoe_size]
x=[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],[190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

y=['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']

#varible to store desicion tree modle
clf=tree.DecisionTreeClassifier()
#train the model, takes two arguments, x and y,
clf=clf.fit(x,y)
prediction=clf.predict([[190, 70, 43]])
print(prediction)
#output ['male']
#compared it to chat gpt said male too
