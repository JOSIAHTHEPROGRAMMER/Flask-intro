from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
  data = json.load(f)


@app.route('/')
def hello_world():
  return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students')
def get_students():
  return jsonify(data)  # return student data in response


# route variables
@app.route('/students/<id>')
def get_student(id):
  for student in data:
    if student['id'] == id:  # filter out the students without the specified id
      return jsonify(student)
  return 'Student does not exist'

#EXERCISE ONE
@app.route('/students/count')
def countStats():
  counts = {
    'Chicken': 0,
    'Computer Science (Major)': 0,
    'Computer Science (Special)': 0,
    'Fish': 0,
    'Information Technology (Major)': 0,
    'Information Technology (Special)': 0,
    'Vegetable': 0,
  }
    
  for student in data:  
      if student['pref'] in counts:
        counts[student['pref']] +=1
      
      if student['programme'] in counts:
        counts[student['programme']] +=1
  return jsonify(counts)
      
#EXERCISE TWO    
@app.route('/add/<a>/<b>')
def addNumbers(a,b):
  num1 = int(a)
  num2 = int(b)
  ans = num1 + num2

  return 'Answer from adding ' + a + ' and ' + b + ' is ' + str(ans)

@app.route('/subtract/<a>/<b>')
def subtractNumbers(a,b):
  num1 = int(a)
  num2 = int(b)
  ans = num1 - num2

  return 'Answer from subtracting ' + a + ' and ' + b + ' is ' + str(ans)

@app.route('/multiply/<a>/<b>')
def multiplyNumbers(a,b):
  num1 = int(a)
  num2 = int(b)
  ans = num1 * num2
  
  return 'Answer from multiplying ' + a + ' and ' + b + ' is ' + str(ans)

@app.route('/divide/<a>/<b>')
def divideNumbers(a,b):
  num1 = int(a)
  num2 = int(b)
  ans = num1/num2

  if b != 0:
     return 'Answer from  ' + a + ' and ' + b + ' is ' + str(ans)
  else: 
      return 'You cannot divide by 0..use a different number', 404
    
app.run(host='0.0.0.0', port=8080)