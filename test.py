import numpy as np
import joblib
#!pip install sklearn==1.1.3
from sklearn.ensemble import RandomForestClassifier

import numpy as np

rf = joblib.load("RFor_NoHy_OneHot_Price.joblib")
d = rf.predict(np.array([0.71, 60.2 , 56.  ,  5.86,  5.83,  3.52,  0.  ,  0.  ,  1.  ,
        0.  ,  0.  ,  1.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,
        0.  ,  0.  ,  1.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.]).reshape(1,26))
print(d)