from fastapi import FastAPI

app = FastAPI()

# home route 
@app.get("/")
def get_home():
    return {"message" : "Welcome to home tab"}

# about route
@app.get("/about")
def get_about():
    return {"message" : "This is About section"}

# users route
@app.get("/users")
def get_users():
    return {"Users" : ["Cheeta","Cheeti"]}

