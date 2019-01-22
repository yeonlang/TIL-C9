import os 
import csv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
    
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name}님'
    
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')
    
@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)
    
@app.route('/fruits')
def fruits():
    fruits = ['apple','banana', 'mango', 'melon']
    return render_template('fruits.html', fruits=fruits)

@app.route('/send')
def send():
    return render_template('send.html')
    
@app.route('/receive')
def receive():
    # request.args : {'who': 'daehyeon', 'message': 'hello'}
    who=request.args.get('who')
    message=request.args.get('message')
    
    with open('guestbook.csv','a',encoding='utf8',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['who', 'message'])
        writer.writerow({
            'who' : who ,
            'message': message
        })
    
    return render_template('receive.html', name=who, message=message)
    
@app.route('/guestbook')
def guestbook():
    messages = []
    with open('guestbook.csv','r',encoding='utf8',newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(row)
            
    return render_template('guestbook.html',messages=messages)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)