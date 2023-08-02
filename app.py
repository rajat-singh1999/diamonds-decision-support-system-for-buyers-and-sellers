import re
from flask import Flask, render_template, request, abort
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

def is_numeric(value):
    return re.match(r'^\d+(\.\d+)?$', value)

def doDefault(x,y,z,depth,table):
    if not depth:
        depth = '61.75'
    if not table:
        table = '57.46'
    if not x:
        x = '5.73'
    if not y:
        y = '5.73'
    if not z:
        z = '3.54'
    return x,y,z,depth,table
            

@app.route("/form/<user>", methods=['GET','POST'])
def form(user):
    if user not in ['seller', 'buyer']:
            abort(404)
    else:
        if request.method == 'POST':
            carat = request.form.get('carat')
            depth = request.form.get('depth')
            table = request.form.get('table')
            x = request.form.get('x')
            y = request.form.get('y')
            z = request.form.get('z')
            cut = request.form.get('cut')
            color = request.form.get('color')
            clarity = request.form.get('clarity')
            
            x,y,z,depth,table = doDefault(x,y,z,depth,table)

            if not is_numeric(carat) or not is_numeric(depth) or not is_numeric(table) \
                    or not is_numeric(x) or not is_numeric(y) or not is_numeric(z):
                message = "The values you entered needs to be numeric! Try again."
                category = 'error'
                return render_template("form.html", message=message, category=category, user=user)

            carat = float(carat)
            depth = float(depth)
            table = float(table)
            x = float(x)
            y = float(y)
            z = float(z)

            arr1 = [carat,depth,table,x,y,z]
            cut_arr = [0.0]*5
            color_arr = [0.0]*7
            clarity_arr = [0.0]*8

            cut_arr[cut-1] = 1.0
            color_arr[color-1] = 1.0
            clarity_arr[clarity-1] = 1.0

            inp = arr1 + cut_arr + color_arr + clarity_arr

            rf = joblib.load("RFor_NoHy_OneHot_Price.joblib")
            ans = rf.predict(np.array(inp).reshape(1,26))

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
            max = class_map[ans][1]
            min = class_map[ans][0]
            
            # for sellers
            if user == "seller":
                ans = (f"The value of this diamond is in the range of ${min} and ${max}.")
            else:
                # for buyers
                ans = (f"The maximum price you can buy this diamond is ${max}.")
            
            message = "submitted successfully"
            category = 'success'
            print(carat,cut,color,clarity,depth,table,x,y,z,user)
            return render_template("form.html", vol=ans, message=message, category=category, user=user)

        return render_template("form.html", user=user)
    '''
@app.route("/test")
def test():
    return render_template("test.html")
    '''


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
