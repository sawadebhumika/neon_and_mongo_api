from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class students(BaseModel):
    id : int
    name : str
    age : int

# @app.post("/students")
# def create_student(stud:students):
#     return stud

# test by postman  http://localhost:8000/students pass data in body {id:10, name:"bhumik", age:100}
# for swagger ui http://127.0.0.1:8000/docs


# store student data to file

def save_student_to_file(data):
    with open("students.txt", "a") as f:     #append mode
        f.write(f"{data.id} {data.name}, {data.age}\n")


@app.post("/students")
def create_student(stud:students):
    # data = stud.dict()
    save_student_to_file(stud)
    return {"message":"student data saved success"}

