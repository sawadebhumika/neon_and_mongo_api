# def test():
#     print("my name is bhumika")

# test()    # call the function, pythonic call. purely python dependent 


from fastapi import FastAPI


app = FastAPI()   # objetc of the fastapi

@app.get("/")     #decorated it with the object
def test():
    return {"message":"Hello World!"}

@app.get("/bhumik")
def test1():
    return {"My name  is Bhumika. I am Data Scientist"}


students = {1:"bhumika", 2:"pravs", 3:"Sam"}
@app.get("/students")
def get_students():
    return students


@app.get("/students/{stud_id}")

def student_search(stud_id:int):
    return {"id": stud_id, "name": students[stud_id]}


# to add data in dictionary
@app.get("/add_student")
def add_stud(stud_id:int, name:str):
    students[stud_id] = name
    return students

# http://127.0.0.1:8000/add_student?stud_id=4&name=anshula


@app.post("/add_students_diff")
def add_student_diff():
    students["new_id"] = "new_name"
    return students

# run the above function by post in postman, since its a post well not be ale to call from the browser


from pydantic import BaseModel
class newdata(BaseModel):
    stud_id:int
    name:str

@app.post("/add_student_new_value")
def add_student_new_value(newdata:newdata):
    students[newdata.stud_id] = newdata.name
    return newdata

# in post , inside body {stud_id:10, name:"bhumik"} then run request