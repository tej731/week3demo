from flask import Flask,render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form.get('username')
    rollno=request.form.get('rollno')
    email=request.form.get('email')
    year=request.form.get('year')
    return render_template('result.html',name=username,roll=rollno,mail=email,yr=year)
if __name__ == "__main__":
    app.run(debug=True)