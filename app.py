from flask import Flask,render_template,redirect,url_for,flash,request
import mysql.connector

app=Flask(__name__)
app.secret_key="Ram@123"

conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ram@1997",
    database="mydb"
)
cursor=conn.cursor()

@app.route('/')
def index():
    sql=("select * from users")
    cursor.execute(sql)
    res=cursor.fetchall()
    
    return render_template('index.html',data=res)

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        flash("Data Inserted Successfully")
        name=request.form['nm']
        number=request.form['number']
        email=request.form['email']
        cursor.execute("Insert into users(NAME,CONTACTNO,Email) values(%s,%s,%s)",(name,number,email))
        conn.commit()
        return redirect(url_for("index"))

@app.route('/update', methods=['POST','GET'])
def update():
    if request.method=='POST':
       
       id_data=request.form['id']
       name=request.form['nm']
       number=request.form['number']
       email=request.form['email']
       cursor.execute("""
               Update users 
               SET NAME=%s,CONTACTNO=%s,Email=%s
               Where ID=%s
                      
               """,(name,number,email,id_data))
       conn.commit()
       flash("Data Updated Successfully")
       return redirect(url_for("index"))
   

    
@app.route('/delete/<string:id_data>',methods=['POST','GET'])
def delete(id_data):
    cursor.execute("Delete from users Where ID=%s",(id_data,))
    flash("Data Deleted Successfully")
    conn.commit()
    return redirect(url_for('index'))


       

if __name__=='__main__':
    app.run(debug=True)