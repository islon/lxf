from transwarp import db
db.create_engine(user='root',password='password',database'test',host='127.0.0.1',port=3306)
uses=db.select(select * from user)