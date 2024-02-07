from bottle import default_app, error, get, static_file, template
import sqlite3 


##############################
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")
 
##############################
@get("/") # 127.0.0.1
def _():
    return template("index.html")
 
##############################
@error(404)
def _(error):
    return "page not found :("
 
##############################
@get("/signup")
def _():
    return template("signup.html")

##############################
@get("/login")
def _():
    return template("login.html")

##############################  
@get("/items")
def _():
    box = [] # list and it is empty
    for i in range(1, 101):
        box.append(i)
    print(box)    
    return template("items", box=box)   

##############################  
@get("/users")
def _():
    db = sqlite3.connect("company.db")
    db.row_factory = dict_factory # JSON objects
    sql = db.execute("SELECT * FROM users")
    users = sql.fetchall()
    return template("users", users=users)   


##############################  
@get("/delete-user")
def _():
    db = sqlite3.connect("company.db")
    db.row_factory = dict_factory # JSON objects
    sql = db.execute("DELETE FROM users WHERE user_pk = '842d9ed8-1e4c-438a-8980-b67f0d5e9994'")
    
    return "user deleted" 


##############################  
@get("/items/<id>")
def _(id):
    title = "Item " + id
    return template("item", 
                    id=id, 
                    title = title)





##############################
app = default_app()
 

