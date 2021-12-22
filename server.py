#Understanding Routing Practice Assignment Flask Fundamentals


from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo(): 
    return "Dojo!"

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi" + name + '!'

@app.route('/repeat/<int:number>/<string:message>')
def repeat(number,message):
    output = ''
    for i in range (0,number):
        output += f"<p> {message}</p>"
    return output












if __name__=="__main__":
    app.run(debug=True)



