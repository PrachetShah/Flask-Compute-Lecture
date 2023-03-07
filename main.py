from flask import Flask, render_template, url_for, request
from markupsafe import escape
from decision_tree_classification import Decision

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        data = request.form
        print(data)

        # creating input necessary for model
        if data:
            age = data['age']
            salary = data['salary']

            # loading model
            model = Decision()
            result = model.decision(data['age'], data['salary'])
            # print(result[0])
            query = {
                "ans": result[0],
                "age": age,
                "salary": salary,
            }
        return render_template('index.html', var2=query)
    return render_template('index.html')

@app.route('/template/<string:name>')
def temp(name="NULL"):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()