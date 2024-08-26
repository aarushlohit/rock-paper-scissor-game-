import MySQLdb as m
#package installed
a=None
Nofrows=''
def select():
        global a,Nofrows
        print("1.fetchmany(int)")
        print("2.fetchall()")
        print("3._fetch_row()")
        select = int(input("ENTER YOUR CHOICE:"))

        
       
        con= m.connect(host="localhost",user='hotchocolate',password="1986",database="Testing")
        cur=con.cursor()
        cur.execute("select * from courses;")
        if select == 1:
            Nofrows=int(input("enter no .of rows u want to fetch:"))
            a=cur.fetchmany(Nofrows)
            print(a)
            print("sucess")
            con.close()
        elif select==2:
             con= m.connect(host="localhost",user='hotchocolate',password="1986",database="Testing")
             cur=con.cursor()
             cur.execute("select * from courses;")
             a=cur.fetchall()
             print(a)
             print("sucess")
             con.close()
        elif select==3:
            con= m.connect(host="localhost",user='hotchocolate',password="1986",database="Testing")
            cur=con.cursor()
            cur.execute("select * from courses;")
            a=cur._fetch_row()
            print(a)
            print("sucess")
            con.close()
        elif select==4>4:
            print("oops invalid choice")
            
        
            
            
        
        
def insert():
    con= m.connect(host="localhost",user='hotchocolate',password="1986",database="Testing")
    cur=con.cursor()
    X=int(input("enter your roll number:"))
    Y=input("enter your name")
    Z=int(input("enter your age"))
    z1=input("enter your coursename")
    z2=input("enter your secret code:")
    query = """
        INSERT INTO courses VALUES (%s, %s, %s, %s, %s)"""
    values = (X, Y, Z, z1, z2)
    
    
    cur.execute(query, values)
    con.commit()
    print("Data inserted successfully")
    con.close()
while True:
    print("=========MENU===============")
    print("1.select")
    print("2.insert")
    
    choice=int(input('enter your choice:'))
    
    if choice==1:
        select()
    elif choice==2:
        insert()
    elif choice==3:
        print("project under development wait....for new updates and functions")