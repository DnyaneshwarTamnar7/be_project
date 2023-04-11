from flask import * #importing flask
import datetime #datetime module
import bcrypt   #importing hashing algorithm
import mysql.connector  #mysql connector
from fpdf import FPDF


app=Flask(__name__) #initializing flask
pdf=FPDF()
salt=bcrypt.gensalt()   #salt generated for hashing
connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()
app.secret_key="lmk"  #session secret key

# mysql=MySQL(app)

@app.route("/log")  #login route for rendering login page
def log():
    return render_template('login.html')

@app.route("/login",methods=['post']) #login rotue for validating user and their credentials
def login():
    if 'Email' in session:
        session.pop('Email',None)
        flash("Please try to login using valid credentials!")
        return redirect("/log")
    else:
        Email=request.form['email']
        password=request.form['password'].encode('utf-8')
        cursor=connection.cursor(prepared=True)
        cursor.execute("select * from user_view where email=%s",(Email,))
        records=cursor.fetchall()
        if records:
            hash=records[0][1].encode('utf-8')
            result=bcrypt.checkpw(password,hash)
            if result:
                session['Email']=Email
                return render_template('home.html',name=None)
            else:
                flash("Please Enter Correct login Credentials!")
                return render_template('login.html')
        else:
            flash("Please Register as a new user!")
            return redirect("/")    #regiter as new user
        

@app.route("/") #registeration route for rendering registration page
def regist():
    return render_template('register.html')

@app.route("/home") #home route for rendering the home page
def home():
    if 'strs-res' in session:
        stress=session['strs-res']
        return render_template('home.html',stress=stress)
    else:
        return render_template('home.html')

@app.route("/register",methods=['post'])    #registration route for registring the new user 
def register():
    Email=request.form['email']
    cursor=connection.cursor()
    cursor.execute("select * from user where email=%s",(Email,))
    records=cursor.fetchall()
    if records: #already register profile
        flash("You are already registered with us. Please try to login!")
        return redirect('/log')
    else:   #new registeration profile
        Name=request.form['name']
        #date1=request.form['Birth-Date']
        #d=datetime.date(int(date1[2]),int(date1[1]),int(date1[0]))
        #date1=d.strftime("%B %d, %Y")
        Age=request.form['age']
        Email=request.form['email']
        Mobile=int(request.form['mobile'])
        question=request.form['security']
        ans=request.form['sec-ans']
        cursor.execute("insert into user_security(email,question,answer) values(%s,%s,%s)",(Email,question,ans))
        if(len(request.form['mobile'])!=10):
            flash("Please enter valid mobile number!")
            return redirect('/')
        password=request.form['password'].encode('utf-8')
       # if(for i in ['!','@','#','$','%','&','*','^'] if i in password return True):
        Password=bcrypt.hashpw(password,salt)
        cursor.execute("insert into user(name,age,email,mobile,password) values(%s,%s,%s,%s,%s)",(Name,Age,Email,Mobile,Password))
        #cursor.execute("insert into results(email,Stress,Anxiety,Depression) values(%s,%s,%s,%s)",(Email,"","",""))
        connection.commit()
        session['Email']=Email
        return redirect('/home')

@app.route("/forget-password")
def forget_password():
    return render_template("forget-pass.html")


@app.route("/forg-paswd",methods=['post'])
def forg_passwd():
    Email=request.form['email']
    question=request.form['security']
    ans=request.form['sec-ans']
    cursor.execute("select * from user_security where email=%s",(Email,))
    records=cursor.fetchall()
    if records:
        print(records[0][1]," ",records[0][2])
        if records[0][1]==question and records[0][2]==ans:
            password=request.form['password'].encode('utf-8')
            Password=bcrypt.hashpw(password,salt)
            cursor.execute("update user set password=%s where email=%s",(Password,Email))
            flash("You have updated your password successfully")
            connection.commit()
            return redirect('/log')
        else:
            flash("Please enter correct deatails")
            return redirect("/forget-password")



@app.route("/que1") #stress html rotue
def que1():
    return render_template('stress.html')

@app.route("/stress",methods=['post'])  #stress test result sotring and displaying
def stress():
    if 'Email' in session:
        from models.stress import result
        lst=request.form
        lst=list(lst.values())
        res_lst=[]
        for i in lst:
            res_lst.append(int(i))
        res=result(res_lst)
        Email=session['Email']
        date=datetime.datetime.now().date()
        session['strs-res']=res
        cursor.execute("insert into stress(email,date,result) values(%s,%s,%s)",(Email,date,res))
        connection.commit()
        stress_result=session['strs-res']
        return redirect('/que2')
    else:
        flash("Please login into your account")
        return redirect('/log')
    
@app.route("/que2") #anxiety questionnarie route
def que2():
    return render_template('anxiety.html')

@app.route("/anxiety",methods=['post']) #anxiety result route
def anxiety():
    if 'Email' in session:
        from models.anxiety import result
        lst=request.form
        lst=list(lst.values())
        res_lst=[]
        for i in lst:
            res_lst.append(int(i))
        res=result(res_lst)

        Email=session['Email']
        date=datetime.datetime.now().date()
        cursor.execute("insert into anxiety(email,date,result) values(%s,%s,%s)",(Email,date,res))
        connection.commit()
        return redirect('/que3')
    else:
        flash("Please login into your account")
        return redirect('/log')
    
@app.route("/que3") #depression questionnarie route
def que3():
    return render_template('depression.html')

@app.route("/depression",methods=['post'])  #depression result route
def depression():
    if 'Email' in session:
        from models.depression import result
        lst=request.form
        lst=list(lst.values())
        res_lst=[]
        for i in lst:
            res_lst.append(int(i))
        res=result(res_lst)
        Email=session['Email']
        date=datetime.datetime.now().date()
        cursor.execute("insert into depression(email,date,result) values(%s,%s,%s)",(Email,date,res))
        connection.commit()
        return redirect('/home')
    else:
        flash("Please login into your account")
        return redirect('/log')

@app.route("/profile")  #user profile displaying route
def profile():
    if 'Email' in session:
        Email=session['Email']
        cursor.execute("select * from user where email=%s",(Email,))
        records=cursor.fetchall()
        return render_template('profile.html',records=records[0])
    else:
        flash("Please login into your account")
        return redirect('/log')

@app.route("/profile_update", methods=['post']) #profile updating route
def profile_update():
    inpt=request.form
    Email=session['Email']
    cursor.execute("update user set name=%s,age=%s,mobile=%s where email=%s",(inpt['name'],inpt['age'],inpt['mobile'],Email,))
    connection.commit()
    if cursor.rowcount>0:
        flash("Profile updated successfully.")
        return redirect('/profile') 
    else:
        flash("Nothing to update.")
        return redirect('/profile')  

@app.route("/results")
def results():
    Email=session['Email']
    date=datetime.datetime.now().date()
    date="2023-03-10"
    cursor.execute("select * from stress where email=%s",(Email,))
    stress=cursor.fetchall()
    cursor.execute("select * from anxiety where email=%s",(Email,))
    anxiety=cursor.fetchall()
    cursor.execute("select * from depression where email=%s",(Email,))
    depression=cursor.fetchall()
    if stress and depression and anxiety:
        return render_template('results.html',stress=stress,anxiety=anxiety,depression=depression,zip=zip)
    else:
        flash("Please take a test to get result!")
        return render_template('results.html')
@app.route("/logout")   #logout route for getting out of the system
def logout():
    if 'Email' or 'strs-res' in session:
        session.pop('Email',None)
        session.pop('strs-res',None)
        return redirect('/log')

if __name__=="__main__":
    app.run(debug=True)
