from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from src.read_config import read_config_file

config_file = "config.yaml"
webapp_dir = "webapp"
static_dir = os.path.join(webapp_dir, "static")
template_dir = os.path.join(webapp_dir, "templates")

app = Flask(
    __name__, 
    static_folder=static_dir, 
    template_folder=template_dir
)

def predict(data):
    config = read_config_file(config_file)
    webapp_model_dir = config["webapp_model_dir"]
    model = joblib.load(webapp_model_dir)
    prediction = model.predict(data)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Someting went wrong"}
        return error

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method =="POST":
        try:
            if request.form:
                data =  dict(request.form).values() # get values from form as dict
                data = [list(map(float, data))] # convert into list and map to float
                response = predict(data) # now make prediction
                return render_template("index.html", response=response) # render index.html again with the prediction
            elif request.json: # if request coming from json, e.g. from postman or as API input
                response = api_response(request)
                return jsonify(response)
        except Exception as e:
            # On exception, render 404.html and print error
            error = {"error": "Someting went wrong"}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)