from flask import Flask, render_template, request, jsonify
import os
from prediction_service import prediction

webapp_dir = "webapp"
static_dir = os.path.join(webapp_dir, "static")
template_dir = os.path.join(webapp_dir, "templates")

app = Flask(
    __name__, 
    static_folder=static_dir, 
    template_folder=template_dir
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method =="POST":
        try:
            if request.form:
                data_request =  dict(request.form) # get values from form as dict
                response = prediction.form_response(data_request) # now make prediction
                return render_template("index.html", response=response) # render index.html again with the prediction
            elif request.json: # if request coming from json, e.g. from postman or as API input
                response = prediction.api_response(request.json)
                return jsonify(response)
        except Exception as e:
            # On exception, render 404.html and print error
            #error = {"error": "Someting went wrong"}
            return render_template("404.html", error=e)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)