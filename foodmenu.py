from pymysql import connect

# ---------- DB CONNECTION ----------
def get_connection():
    return connect(
        host="localhost",
        user="root",
        password="ranham307306",
        database="foodbase"
    )

# ---------- SIGNUP ----------
def signup():
    try:
        user_name = input("Enter user name: ")
        password = input("Enter password: ")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO user(user_name,password) VALUES(%s,%s)",
            (user_name, password)
        )

        conn.commit()
        conn.close()
        print("✅ Signup successful! Please login now.")

    except Exception as e:
        print("❌ Error:", e)

# ---------- LOGIN WITH ERROR TYPE ----------
def login():
    try:
        user_name = input("Enter user name: ")
        password = input("Enter password: ")

        conn = get_connection()
        cur = conn.cursor()

        # Check username exists or not
        cur.execute("SELECT * FROM user WHERE user_name=%s", (user_name,))
        user = cur.fetchone()

        if user is None:
            print("❌ Invalid Username")
            conn.close()
            return False

        # Username exists → check password
        cur.execute(
            "SELECT * FROM user WHERE user_name=%s AND password=%s",
            (user_name, password)
        )
        valid = cur.fetchone()
        conn.close()

        if valid:
            print("✅ Login successful!")
            return True
        else:
            print("❌ Invalid Password")
            return False

    except Exception as e:
        print("❌ Error:", e)
        return False

# ---------- ADD ITEM ----------
def add_item():
    try:
        ID = int(input("Enter item ID: "))
        item_name = input("Enter item name: ")
        item_count = int(input("Enter quantity: "))
        gst = float(input("Enter GST %: "))
        price = float(input("Enter price: "))

        amount = item_count * price
        total = amount + (amount * gst / 100)

        cash = float(input("Enter cash given: "))
        balance = cash - total

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO product VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (ID, item_name, item_count, gst, price, total, cash, balance)
        )

        conn.commit()
        conn.close()
        print("✅ Item added successfully")

    except Exception as e:
        print("❌ Error:", e)

# ---------- UPDATE ----------
def update_menu():
    try:
        ID = int(input("Enter item ID: "))
        item_name = input("Enter item name: ")
        item_count = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE product SET item_name=%s,item_count=%s,price=%s WHERE ID=%s",
            (item_name, item_count, price, ID)
        )

        conn.commit()
        conn.close()

        if cur.rowcount > 0:
            print("✅ Item updated")
        else:
            print("❌ Invalid ID")

    except Exception as e:
        print("❌ Error:", e)

# ---------- DELETE ----------
def delete_menu():
    try:
        ID = int(input("Enter item ID: "))

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM product WHERE ID=%s", (ID,))
        conn.commit()
        conn.close()

        if cur.rowcount > 0:
            print("✅ Item deleted")
        else:
            print("❌ Invalid ID")

    except Exception as e:
        print("❌ Error:", e)
        
def find_item_name():
    try:
        ID = int(input("enter the id no:"))
        
        
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q=f"select * from product where ID={ID}"
        
        cursor = conn.cursor()
        cursor.execute(q)
        res=cursor.fetchall()
        count=0
        print("ID\t\titem_name\titem_count\tgst\t\tprice\t\ttotal\t\tcash_given\tbalance")
        for i in res:
            for j in i:
                print(j,end="\t\t")
                count=1
            print("")
        print("data found.....")
        conn.close
        if(count==0):
            print("data not found....")
        
    except Exception as d:
        print(d)
        
def print_info():
    try:
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        q=f"select * from product"
        
        c = conn.cursor()
        c.execute(q) 
        res=c.fetchall()
        count=0
        print("add_item\tupdate_menu\tdelete_menu\tdata_find")
        for i in res:
            for j in i:
                print(j,end="\t")
                count=1
                print()
                
            if(count==0):
                print("no data found")
                conn.close()
    except Exception as e:
        print(e)
    

# ---------- PRODUCT MENU ----------
def product():
 while(True):
    ch=int(input("1.add_item\n2.update_menu\n3.delete_menu\n4.data_find\n5.print_info\n6.exit\nselect any one choice:"))
    if(ch==1):
        print("\nAdding data processing....\n")
        add_item()
        print("\n")
    elif(ch==2):
        print("\nUpdating data processing....\n")
        update_menu()
        print("\n")
    elif(ch==3):
        print("\nDeleting data processing....\n")
        delete_menu()
        print("\n")
    elif(ch==4):
        print("\nFinding data processing....\n")
        find_item_name()
        print("\n")
    elif(ch==5):
        print("\nprint_info data processing....\n")
        print_info()
        print("\n")
    elif(ch==6):
        print("\nExiting data processing....\n")
        print("thank you...")
        break
    else:
        print("\ninvalid choice...\n")

# ---------- USER MENU ----------
def user_menu():
    while True:
        print("\n1.Signup\n2.Login\n3.Exit")
        ch = int(input("Select: "))

        if ch == 1:
            signup()

        elif ch == 2:
            if login():           # 🔐 LOGIN CHECK
                product()   # Admin menu opens ONLY here

        elif ch == 3:
            print("Thank you!")
            break
        else:
            print("❌ Invalid choice")

# ---------- MAIN ----------
while True:
    print("\n1.Employee\n2.Admin\n3.Exit")
    ch = int(input("Select: "))

    if ch == 1:
        add_item()   # limited access
    elif ch == 2:
        user_menu()
    elif ch == 3:
        print("Thank you!")
        break
    else:
        print("❌ Invalid choice")
