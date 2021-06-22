import random 
import psycopg2
import datetime
data = {}

#change it by your credantials:
db_connect = psycopg2.connect(database = "practice",host = "127.0.0.1",port = "5432",user= "mrasr",password="admin")
cur = db_connect.cursor()
table = "bank_managment"
#check table exist or not 
try:
    query = f"SELECT 1 FROM {table}"
    cur.execute(query)
    data1 = bool(cur.fetchone())
    data1 = data1
    
    
except psycopg2.errors.UndefinedTable:
    data1 = False
    cur.execute("rollback")    


if data1 == False:
    try: 
        sql = f"CREATE TABLE {table}("
        sql += "bank varchar(255), ifsc varchar(255), account_no BIGINT,name varchar(255), address varchar(255), phone BIGINT, amount INT)"   
        cur.execute(sql)  
    except psycopg2.errors.DuplicateTable:
        print("hew")
        cur.execute("rollback") 


    

class Bank:
    bank_name= "state bank of india"
    def __init__(self):
        self.ifsc= ""
        self.address = ""

    def branch(self):
        self.ifsc = "SBI"+str(random.randint(111111,111113))
        return self.ifsc
        
    
class Function(Bank):

    def add_user(self,name,location,phone,amount):
        super().__init__()
        self.branch()
        self.name = name
        
        self.location = location
        self.phone = phone
        self.account_no = random.randint(666666666666,999999999999)
        self.amount = amount
        insert_query = f"insert into {table} values("
        insert_query += "'"+Bank.bank_name+"', "
        insert_query += "'"+self.branch()+"', "
        insert_query += (str(self.account_no))+", "
        insert_query += "'"+self.name+"', "
        insert_query += "'"+self.location+"', "
        insert_query += (str(self.phone))+", "
        insert_query += (str(self.amount))+") "
        cur.execute(insert_query)
        db_connect.commit()
        
        
    def view(self):
        try:
            confirm = int(input("enter phone: "))

            view_query = f"SELECT * FROM {table} WHERE phone = {confirm}"
            cur.execute(view_query)
            for dt in cur.fetchone():
                print(dt)
        except:
            print("Enter correct phone no!!")
    def deposit(self):
        try:
            confirm = int(input("enter phone: "))
            deposit_amount = int(input("enter deposit amount: "))
            added = f"UPDATE {table} SET amount = amount + {deposit_amount} WHERE phone = {confirm}"
            cur.execute(added)
            db_connect.commit()
            print(f"credit {deposit_amount} in your account")
            run.view()
        except:
            print("Enter correct phone no!!")

    def withdraw(self):
        try:
            confirm = int(input("enter phone: "))
            withdraw_amount = int(input("enter withdraw amount: "))
            dedect = f"UPDATE {table} SET amount = amount - {withdraw_amount} WHERE phone = {confirm}"
            cur.execute(dedect)
            db_connect.commit()
            print(f"debited {withdraw_amount} from your account")
            run.view()
        except:
            print("Enter correct phone no!!")

    def delete(self):
        try:
            confirm = int(input("enter phone: "))
            del_query = f"DELETE FROM {table} WHERE phone = {confirm}"
            cur.execute(del_query)
            db_connect.commit()
            print("your bank account deleted")
        except:
            print("Enter correct phone no!!")
       
run = Function()
print(''' WELCOME TO SBI CLI \n
1. ACCOUNT OPEN \n
2. CHECK ACCOUNT INFORMATION \n
3. DEPOSIT \n
4. WITHDRAW \n
5. CLOSE ACCOUNT
''')
choose_input = int(input("CHOOSE YOUR CHOICE: "))
if choose_input == 1:
    name = input("Enter your name : ")
    location = input("Enter your address; ")
    phone = int(input("enter your phone no "))
    amount = int(input("Enter account opening amount: "))
    run.add_user(name,location,phone,amount)
    
if choose_input ==2:
    run.view()

if choose_input ==3:
    run.deposit()

if choose_input ==4:
    run.withdraw()

if choose_input ==5:
    run.delete()
