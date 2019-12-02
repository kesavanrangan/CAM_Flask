from flask import Flask,render_template,request,redirect,url_for
import pyodbc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
         userDetails = request.form
         name = userDetails['name']
         email = userDetails['email']
         conn = pyodbc.connect('DRIVER={SQL Server};SERVER=STPTSQLV04;DATABASE=CamDB_test;UID=techops;PWD=Techops@123;PORT=1433')
         cursor = conn.cursor()
         query = 'INSERT INTO %s (name,email) VALUES (\'%s\',\'%s\')' % ('Users', name, email)
         cursor.execute(query)
         cursor.commit()
         conn.close()
         return redirect(url_for('result_test'))
    return render_template('index_test.html')

@app.route('/result_test', methods=['GET', 'POST'])
def result_test():
    if request.method == 'POST':
        return redirect(url_for('index'))
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=STPTSQLV04;DATABASE=CamDB_test;UID=techops;PWD=Techops@123;PORT=1433')
    cursor = conn.cursor()
    query = 'SELECT * FROM Users'
    cursor.execute(query)
    return render_template('result_test.html',final=cursor.fetchall())
    conn.close()


if __name__=='__main__':
    app.run(host="10.88.1.123",debug=True,port=5000)