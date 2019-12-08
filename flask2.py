from flask import Flask,redirect,url_for,request
app=Flask(__name__)
@app.route('/login',methods=['POST','GET'])
def log():
    if request.method=='POST':
        user=request.form['n']
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('n')
        return redirect(url_for('success',name=user))
@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name
    
if __name__=="__main__":
    app.run(debug=True)
