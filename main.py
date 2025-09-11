from fastapi import FastAPI
import pymysql

app = FastAPI()

db = pymysql.connect(
  host = '127.0.0.1',
  port = 3306,
  user = "root",
  password = "mingun0906!",
  database = "practice",
  charset = "utf8mb4"
)

cursor = db.cursor()

def table():
  sql = """
  CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
  )
  """

  cursor.execute(sql)
  db.commit()

@app.get("/")
def root():
    return {"message": "FastAPI 서버가 정상 실행 중입니다!"}

@app.post("/post")
def create(name, email):
  cre = """
  INSERT into user (name, email)
  VALUES (%s, %s)
  """

  cursor.execute(cre, (name, email))
  db.commit()
  return {"message": "User created", "name": name, "email": email}

@app.get("/get")
def read(id : int):
  rea = """
  SELECT name, email
  FROM user
  WHERE id = %s
  """

  cursor.execute(rea, (id,))
  row = cursor.fetchone()
  if row:
    return {"id": id, "name": row[0], "email": row[1]}
  else:
    return {"error": "User not found"}

@app.put("/update")
def update(name, email, id : int):
  upd = """
  UPDATE user
  SET name = %s, email = %s
  WHERE id = %s
  """

  cursor.execute(upd, (name, email, id))
  db.commit()
  return {"message": "User updated", "id": id, "name": name, "email": email}

@app.delete("/delete")
def delete(id : int):
  dele = """
  DELETE
  FROM user
  WHERE id = %s
  """

  cursor.execute(dele, (id, ))
  db.commit()
  return {"message": f"User {id} deleted"}
