from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key='secret'
def activitylog(location,gold,time, earn):
    if location != 'casino':
        message="<p class='activitylist'>you found "+str(gold)+" gold at the "+str(location)+" at: "+str(time)+'</p>'
        session['activity'] += message
    else:
        if earn==True:
            message="<p class='activitylist greentext'>You Won "+str(gold)+" at the casino. the time was: "+str(time)+'</p>'
            session['activity'] += message
        else:
            message="<p class='activitylist redtext'>You Lost "+str(gold)+" at the casino. the time was: "+str(time)+'</p>'
            session['activity'] += message
@app.route('/')
def ninjagoldsplash():
    
    if 'total' not in session:
        session['total'] = 0
        total = session['total']
    if 'activity' not in session:
        session['activity'] = str('welcome to ninja gold!')
    print(session['activity'],session['total'],'hello world')
    return render_template('index.html', activity=session['activity'], total=session['total'])

@app.route('/process_money', methods=['GET','POST'])
def processmoney():
    hiddenName=request.form['hidden']
    print(hiddenName)
    time = datetime.datetime.now()
    if hiddenName == 'farm':
        gold=random.randrange(10,20)
        print('hello')
        session['total']= session['total']+gold
        activitylog(hiddenName,gold,time,earn=True)
    elif hiddenName =='cave':
        gold=random.randrange(5,10)
        print('hello')
        session['total']= session['total']+gold
        activitylog(hiddenName,gold,time,earn=True)
    elif hiddenName =='house':
        gold=random.randrange(2,5)
        print('hello')
        session['total']= session['total']+gold
        activitylog(hiddenName,gold,time, earn=True)
    elif hiddenName =='casino':
        gold=random.randrange(0,50)
        print('hello')
        chance=random.randrange(0,2)
        if chance == 0:
            session['total']= session['total']+gold
            activitylog(hiddenName,gold,time, earn=True)
        elif chance==1:
            session['total']= session['total']-gold
            activitylog(hiddenName,gold,time, earn=False)            
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)