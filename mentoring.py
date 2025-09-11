import pymysql


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

def create(name, email):
  cre = """
  INSERT into user (name, email)
  VALUES (%s, %s)
  """

  cursor.execute(cre, (name, email))
  db.commit()

def read(id):
  rea = """
  SELECT name, email
  FROM user
  WHERE id = %s
  """

  cursor.execute(rea, (id))
  row = cursor.fetchone()
  print(row)

def update(name, email, id):
  upd = """
  UPDATE user
  SET name = %s, email = %s
  WHERE id = %s
  """

  cursor.execute(upd, (name, email, id))
  db.commit()

def delete(id):
  dele = """
  DELETE
  FROM user
  WHERE id = %s
  """

  cursor.execute(dele, (id))
  db.commit()

while True:
  print("어떤 것을 하기 원하시나요?\ncreate\nread\nupdate\ndelete\nfinish")
  user_choice = input()
  if user_choice == "create":
    print("name과 email을 공백을 두고 입력해주세요")
    name, email = input().split()
    create(name, email)

  elif user_choice == "read":
    print("id를 입력해주세요")
    id = input()
    read(id)
    
  elif user_choice == "update":
    print("name과 email과 id를 공백을 두고 입력해주세요")
    name, email, id = input().split()
    update(name, email, id)

  elif user_choice == "delete":
    print("id를 입력해주세요")
    id = input()
    delete(id)

  elif user_choice == "finish":
    print("종료합니다")
    break

  else:
    print("다시 입력해주세요")
    

db.close()