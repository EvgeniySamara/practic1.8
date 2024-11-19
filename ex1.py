from flask import Flask
from random import choice
from datetime import *

app = Flask(__name__)

carslist =['Chevrolet', 'Renault', 'Ford', 'Lada']
txt = 'корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин'
cats = txt.split(',')
carslist.append('Ford')
time = datetime.now()
time_plus_1 = time + timedelta(hours=1)

# print("Current Time:", current_time.strftime('%H:%M:%S'))
# print("Time Plus One Hour:", time_plus_1.strftime('%H:%M:%S'))



@app.route('/')
def func1():
    return "hello world"


@app.route('/cars')
def func2():
    return ', '.join(carslist)

@app.route('/cats')
def func3():
    return choice(cats)

@app.route('/get_time/now')
def func4():
    return time.strftime('%H:%M:%S')

@app.route('/get_time/future')
def func5():
    return time_plus_1.strftime('%H:%M:%S')




if __name__ == '__main__':
    app.run(port=8080)


