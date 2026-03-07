from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/math",methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        #addition condition
        if (ops=='add'):
            r=num1+num2
            result='The sum of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
      
        #Subtraction condition
        if (ops=='subtract'):
            r=num1-num2
            result='The subtract of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        
        #Multiplication condition
        if (ops=='multiply'):
            r=num1*num2
            result='The multiply of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        
        #division condition
        if (ops=='divide'):
            r=num1/num2
            result='The divide of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        return render_template("results.html",result=result)
        

@app.route("/")
def hello_world():
    return "<h1>Hey suresh</h1>"


@app.route("/postman_data",methods=['POST'])
def math_operation1():
    if (request.method=='POST'):
        ops=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        #addition condition
        if (ops=='add'):
            r=num1+num2
            result='The sum of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
      
        #Subtraction condition
        if (ops=='subtract'):
            r=num1-num2
            result='The subtract of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        
        #Multiplication condition
        if (ops=='multiply'):
            r=num1*num2
            result='The multiply of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        
        #division condition
        if (ops=='divide'):
            r=num1/num2
            result='The divide of       '+str(num1)+'  and  '+str(num2)+"  is  "+str(r)
        return jsonify(result)
        


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)