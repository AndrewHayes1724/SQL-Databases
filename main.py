import sqlite3
con = sqlite3.connect('test.db')
cur = con.cursor()
con.execute("CREATE TABLE IF NOT EXISTS my_garage (id, make, model, year, color, miles)")

def user_input():
    print("\nCommands - Key")
    print("----------------")
    print("A - View Table")
    print("S - Add row")
    print("W - Modify existing data")
    print("D - Delete Data")
    print("F - Find/Query Data")
    print("1 - Exit")
    print("--------------------")
    tmp_input = 0
    val = input("Type Command \n")
    if val == 1:
        return False

    if val == 'A' or val == 'a':
        view_table()
        return True

    if val == 'S' or val == 's':
        add_row()
        return True

    if val == 'D' or val == 'd':
        delete_data()
        return True

    if val =='W' or val == 'w':
        modify_data()
        return True
    if val == 'F' or val == 'f':
        query_data()
        return True
    

def view_table():
    for row in cur.execute('SELECT * FROM my_garage'):
        print(row)

def add_row():
    total_rows = cur.execute("SELECT * FROM my_garage")
    id = len(total_rows.fetchall())
    id += 1

    make = input("Enter the 'make'\n")
    
    model = input("Enter the 'model'\n")
    
    year = input("Enter the 'year'\n")
    
    color = input("Enter the 'color'\n")
    
    miles = input("Enter the 'mileage'\n")

    con.execute("INSERT INTO my_garage (id,make,model,year,color,miles) VALUES(?,?,?,?,?,?)", (id,make,model,year,color,miles,))

def delete_data():
    print("1 - Delete entire table")
    print("2 - delete just row\n")
    val = str(input())
    if val == '1':
        con.execute("DELETE FROM my_garage")
    else:
        print("Type the 'model' and the year (ie. mustang 1965) of the row you want to delete\n")
        val = str(input())
        val = val.split()
        con.execute("DELETE FROM my_garage WHERE model=? AND year=?", (val[0], val[1],))

def modify_data():
    print("Which row would you like to modify?\n")
    val = input("Type row number\n")
    col = input("Which column would you like to update?\n")
    new_input = str(input("What would you like to change it to?\n"))
    string = "UPDATE my_garage SET " + col + " = " + "'" + new_input + "'" + " WHERE id = " + val
    con.execute(string)
    con.commit()

def query_data():
    num_of_rows = 0
    print("Which makes of cars would you like to find?")
    print("(Format answer ex. ford) \n")
    val = str(input())
    string = "SELECT * FROM my_garage WHERE make=?", (val,)
    for row in cur.execute("SELECT * FROM my_garage WHERE make=?", (val,)):
        num_of_rows += 1
        print(row)
    num_of_rows = str(num_of_rows)
    print("\nTotal number of rows found: " + num_of_rows)

    

status = True
while status == True:
  status = user_input()
con.commit()
con.close()

