from fastapi import FastAPI
from pydantic import BaseModel
# pip install psycopg2-binary
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()
db_url = "postgres*****************************************aws.neon.**************************equire"



class students(BaseModel):
    id : int
    name : str
    age : int

def get_connection_url():
    conn = psycopg2.connect(db_url,cursor_factory=RealDictCursor)
    return  conn

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

@app.post("/students/db/insert")
def store_students_in_db(student:students):
    conn = get_connection_url()
    cursor = conn.cursor()    #cursor is kind of  pointer
    insert_query = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(insert_query,(student.id, student.name, student.age))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message":"student data inserted successfully"}