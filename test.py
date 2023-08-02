import numpy as np
import joblib
#!pip install sklearn==1.1.3
#from sklearn.ensemble import RandomForestClassifier

import numpy as np

#rf = joblib.load("RFor_NoHy_OneHot_Price.joblib")
carat = 0.71
depth = 60.2
table = 56.0
x = 5.86
y = 5.83
z = 3.52
cut = 3
color = 1
clarity = 3

arr1 = [carat,depth,table,x,y,z]
cut_arr = [0.0]*5
color_arr = [0.0]*7
clarity_arr = [0.0]*8

cut_arr[cut-1] = 1.0
color_arr[color-1] = 1.0
clarity_arr[clarity-1] = 1.0

inp = arr1 + cut_arr + color_arr + clarity_arr
print(inp)
ans = 3

class_map = {
        0: (326,2175.7),
        1: (2175.7, 4025.4),
        2: (4025.4, 5875.1),
        3: (5875.1, 7724.8),
        4: (7724.8, 9574.5),
        5: (9574.5, 11424.2),
        6: (11424.2, 13273.9),
        7: (13273.9, 15123.6),
        8: (15123.6, 16973.3),
        9: (16973.3, 18823)
}
# for sellers
max = class_map[ans][1]
min = class_map[ans][0]
print(f"The value of this diamond is in the range of ${min} and ${max}.")

# for buyers
print(f"The maximum price you can buy this diamond is ${max}.")
'''
d = rf.predict(np.array([0.71, 60.2 , 56.  ,  5.86,  5.83,  3.52,  0.  ,  0.  ,  1.  , 0.  ,  0.  ,  1.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,0.  ,  0.  ,  1.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.]).reshape(1,26))
print(d)
[0.71, 60.2, 56.0, 5.86, 5.83, 3.52, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.71, 60.2, 56. , 5.86, 5.83, 3.52, 0. , 0. , 1.0, 0.  ,0.  ,1.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0.  ,0. , 0. , 1. , 0. , 0. , 0. , 0. , 0.]
'''