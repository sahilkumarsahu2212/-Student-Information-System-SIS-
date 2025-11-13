#Student Information System(SIS)
import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox

cn=None
def getconnection():
    global cn
    cn=mysql.connect(database="sis",
                     user="root",
                     password="sahusahil03",
                     host="localhost",
                     port="3306")
def create_student():
    w1=tk.Tk()
    w1.title("Create Student")
    w1.geometry("400x500")
    w1.resizable(False,False)  #Here we can't resize the window
    rno_lbl=tk.Label(w1,text="Roll No",font=("Arial",15))
    name_lbl=tk.Label(w1,text="Name",font=("Arial",15))
    course_lbl=tk.Label(w1,text="Course",font=("Arial",15))
    doj_lbl=tk.Label(w1,text="Date Of Join",font=("Arial",15))
    fee_lbl=tk.Label(w1,text="Fee",font=("Arial",15))

    e1=tk.Entry(w1,width=20,font=("Arial",15),bg="cyan",fg="red")
    e2=tk.Entry(w1,width=20,font=("Arial",15),bg="cyan",fg="red")
    e3=tk.Entry(w1,width=20,font=("Arial",15),bg="cyan",fg="red")
    e4=tk.Entry(w1,width=20,font=("Arial",15),bg="cyan",fg="red")
    e5=tk.Entry(w1,width=20,font=("Arial",15),bg="cyan",fg="red")

    rno_lbl.pack(side="top",fill="both")
    e1.pack(side="top",fill="both")
    name_lbl.pack(side="top",fill="both")
    e2.pack(side="top",fill="both")
    course_lbl.pack(side="top",fill="both")
    e3.pack(side="top",fill="both")
    doj_lbl.pack(side="top",fill="both")
    e4.pack(side="top",fill="both")
    fee_lbl.pack(side="top",fill="both")
    e5.pack(side="top",fill="both")

    def add_student():  #nested function
        rno=e1.get()
        name=e2.get()
        course=e3.get()
        doj=e4.get()
        fee=e5.get()
        cmd="insert into student values(%s,%s,%s,%s,%s)"
        c=cn.cursor()
        try:
            c.execute(cmd,params=(rno,name,course,doj,fee))
            tkinter.messagebox.showinfo("info","Student Created")
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            e3.delete(0,tk.END)
            e4.delete(0,tk.END)
            e5.delete(0,tk.END)
        except:
            tkinter.messagebox.showerror("error","Error Creating Student")
        cn.commit()
    def close_stud_win():
        w1.destroy()
    b1=tk.Button(w1,text="Add",font=("Arial",15),command=add_student)
    b2=tk.Button(w1,text="Close",font=("Arial",15),command=close_stud_win)
    b1.pack(side="top",fill="both")
    b2.pack(side="top",fill="both")
def update_student():
    w=tk.Tk()
    w.geometry("500x400")
    w.title("Update Student")
    rnolbl=tk.Label(w,text="Roll No",font=("Arial",15))
    rno=tk.Entry(w,width=20,font=("Arial",15),bg="cyan",fg="red")
    feelbl=tk.Label(w,text="Fee",font=("Arial",15))
    fee=tk.Entry(w,width=20,font=("Arial",15),bg="cyan",fg="red")
    def update_fun():
        r=rno.get()
        f=fee.get()
        query="update student set fee=%s where rno=%s"
        c=cn.cursor()
        c.execute(query,params=(f,r))
        k=c.rowcount   #We have to count to the row, rowcount is an attribute which is present in cursor object
        if k>0:
            tkinter.messagebox.showinfo("info","Student Updated")
            rno.delete(0,tk.END)
            fee.delete(0,tk.END)
        else:
            tkinter.messagebox.showinfo("info","invalid rollno")      
    def close():
        w.destroy()
    b1=tk.Button(w,text="Update",font=("Arial",15),command=update_fun)
    b2=tk.Button(w,text="Close",font=("Arial",15),command=close)
    rnolbl.pack(side="top",fill="both")
    rno.pack(side="top",fill="both")
    feelbl.pack(side="top",fill="both")
    fee.pack(side="top",fill="both")
    b1.pack(side="top",fill="both")
    b2.pack(side="top",fill="both")
def list_students():
    c=cn.cursor()
    c.execute("select * from student")
    rows=c.fetchall()#type(rows)==>tuple  #It contains all the records
    w=tk.Tk()
    w.geometry("500x400")
    w.title("StudentList")
    w.resizable(False,False )
    r=0
    for t in rows: #read the data from the tuple,so we used for loop
        rno=tk.Label(w,text=t[0],font=("Arial",15))
        name=tk.Label(w,text=t[1],font=("Arial",15))
        course=tk.Label(w,text=t[2],font=("Arial",15))
        doj=tk.Label(w,text=t[3],font=("Arial",15))
        fee=tk.Label(w,text=t[4],font=("Arial",15))
        rno.grid(row=r,column=0)
        name.grid(row=r,column=1)
        course.grid(row=r,column=2)
        doj.grid(row=r,column=3)
        fee.grid(row=r,column=4)
        r=r+1
def search_student():
    w=tk.Tk()
    w.geometry("500x400")
    w.title("Search Student")
    w.resizable(False,False)
    rnolbl=tk.Label(w,text="Roll No",font=("Arial",15))
    rno=tk.Entry(w,width=15,font=("Arial",15),bg="cyan",fg="red")
    rnolbl.pack(side="top",fill="both")
    rno.pack(side="top",fill="both")
    def search():
        c=cn.cursor()
        query="select name,course,doj,fee from student where rno=%s"
        r=rno.get()
        c.execute(query,params=(r,)) 
        row=c.fetchone()  #It returns one record at a time
        if row==None:
            tkinter.messagebox.showinfo("info","Invalid RollNo")
        else:
            s=list(map(str,row))  #str is the function and row is the iterable obj
            output=",".join(s)  #Here we join with comma(,)
            tkinter.messagebox.showinfo("info",output)
            rno.delete(0,tk.END)
    def close():
        w.destroy()
    b1=tk.Button(w,text="Search",font=("Arial",15),command=search)
    b2=tk.Button(w,text="Close",font=("Arial",15),command=close)
    b1.pack(side="top",fill="both")
    b2.pack(side="top",fill="both")
def delete_student():
    w=tk.Tk()
    w.title("Student Delete")
    w.geometry("500x400")
    rnolbl=tk.Label(w,text="Rollno To Delete",font=("Arial",15))
    rno=tk.Entry(w,width=10,font=("Arial",15),bg="cyan",fg="red")
    def delete():
        r=rno.get()
        query="delete from student where rno=%s"
        c=cn.cursor()
        c.execute(query,params=(r,))
        k=c.rowcount #we have to count ,so we used rowcount attribute which is present in cursor obj
        if k>0:
            tkinter.messagebox.showinfo("info","Student Deleted")
            cn.commit() #because it's a DML 
            rno.delete(0,tk.END)
        else:
            tkinter.messagebox.showerror("error","Invalid Rollno")
    def close():
        w.destroy()
    b1=tk.Button(w,text="Delete",font=("Arial",15),command=delete)
    b2=tk.Button(w,text="close",font=("Arial",15),command=close)
    rnolbl.pack(side="top",fill="both")
    rno.pack(side="top",fill="both")
    b1.pack(side="top",fill="both")
    b2.pack(side="top",fill="both")
def main():
    mw=tk.Tk()
    mw.title("Student Information System")
    mw.geometry("600x500+400+400")
    b1=tk.Button(mw,text="Create Student",font=("Arial",15),command=create_student)
    b2=tk.Button(mw,text="Update Student",font=("Arial",15),command=update_student)
    b3=tk.Button(mw,text="List Students",font=("Arial",15),command=list_students)
    b4=tk.Button(mw,text="Search Student",font=("Arial",15),command=search_student)
    b5=tk.Button(mw,text="Delete Student",font=("Arial",15),command=delete_student)

    b1.pack(side="top",fill="both")  #fill="none" ==>It obtains the width of the text
    b2.pack(side="top",fill="both")
    b3.pack(side="top",fill="both")
    b4.pack(side="top",fill="both")
    b5.pack(side="top",fill="both")
    mw.mainloop()

#Here we have to create signin and signup button, after signin we can access, otherwise no
def main_window():
    getconnection()  #Here one function call another function

    w=tk.Tk()
    w.title("Student Info System")
    w.geometry("400x400")
    def signin():
        sw=tk.Tk()  #sw means signinwindow
        userlbl=tk.Label(sw,text="UserName",font=("Arial",15),fg="blue")
        user=tk.Entry(sw,width=20,font=("Arial",15),bg="pink",fg="red")
        pwdlbl=tk.Label(sw,text="Password",font=("Arial",15),fg="blue")
        pwd=tk.Entry(sw,width=20,font=("Arial",15),show="*",bg="pink",fg="red")
        def signin_fun():
            u=user.get().strip()
            p=pwd.get().strip()
            query="select * from users where user=%s and pwd=%s"
            c=cn.cursor()
            c.execute(query,params=(u,p))
            row=c.fetchone() # fetchone() which is present in cursor object
            if row==None:
                tkinter.messagebox.showinfo("info","Invalid UserName and Password")
            elif u=="" or p=="":  #If one of the condition true,it will give msg
                tkinter.messagebox.showerror("error","Username and Password cannot be empty!!")
                return  #It stops furthur execution
            elif len(p)<4:
                tkinter.messagebox.showerror("error","Password must be at least 4 Character!!")
                return
            else:
                tkinter.messagebox.showinfo("info","Signin Successful")
                sw.destroy() #signin window close
                w.destroy()  #main window also close
                main()  #main function call here
        def close():
            sw.destroy()
        b1=tk.Button(sw,text="SignIn",font=("Arial",15),command=signin_fun)
        b2=tk.Button(sw,text="Close",font=("Arial",15),command=close)
        userlbl.pack(side="top",fill="both")
        user.pack(side="top",fill="both")
        pwdlbl.pack(side="top",fill="both")
        pwd.pack(side="top",fill="both")
        b1.pack(side="top",fill="both")
        b2 .pack(side="top",fill="both")
    def signup():
        sw=tk.Tk()  #sw means signinwindow
        userlbl=tk.Label(sw,text="UserName",font=("Arial",15),fg="blue")
        user=tk.Entry(sw,width=20,font=("Arial",15),bg="pink",fg="red")
        pwdlbl=tk.Label(sw,text="Password",font=("Arial",15),fg="blue")
        pwd=tk.Entry(sw,width=20,font=("Arial",15),show="*",bg="pink",fg="red") 
        def signup_fun():
            u=user.get().strip()   #strip() removes the extra spaces from both side of the username and password
            p=pwd.get().strip()
            
            if u=="" or p=="":  #If one of the condition true,it will give msg
                tkinter.messagebox.showerror("error","Username and Password cannot be empty!!")
                return  #It stops furthur execution
            elif len(p)<4:
                tkinter.messagebox.showerror("error","Password must be at least 4 Character!!")
                return

            query="insert into users values(%s,%s)"
            c=cn.cursor()
            try:
                c.execute(query,params=(u,p))
                cn.commit()
                tkinter.messagebox.showinfo("info","User Registered")
                sw.destroy()
            except:
                tkinter.messagebox.showerror("error","User Exists")
        def close():
            sw.destroy()
        b1=tk.Button(sw,text="SignUp",font=("Arial",15),command=signup_fun)
        b2=tk.Button(sw,text="close",font=("Arial",15),command=close)
        userlbl.pack(side="top",fill="both")
        user.pack(side="top",fill="both")
        pwdlbl.pack(side="top",fill="both")
        pwd.pack(side="top",fill="both")
        b1.pack(side="top",fill="both")
        b2 .pack(side="top",fill="both")


    b1=tk.Button(w,text="SignIn",font=("Arial",15),bg="cyan",command=signin)
    b2=tk.Button(w,text="Signup",font=("Arial",15),bg="cyan",command=signup)
    b1.pack(side="top",fill="both")
    b2.pack(side="top",fill="both")
    w.mainloop()

#Main Program
main_window()  #function call