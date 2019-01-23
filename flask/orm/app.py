from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)

# sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlalchemy 초기화
db = SQLAlchemy(app)

#migrate 초기화
migrate = Migrate(app,db)


#table 생성
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
        
    
# fkask db init
# fkask db migrate
# fkask db upgrade

#정리
# [Create]
# INSERT INTO user (username, email) VALUES('Daehyeon', 'no.water@gmail.com')              
# user = User(username='Daehyeon', email='naspy001@gmail.com') 
# db.session.add(user)
# db.session.commit()

#[Read]
#SELECT * FROM users;
#user=User.query.all()

# SELECT * FROM users WHERE username='nwith';
# users = User.query.filter_by(username='nwith').all()

# SELECT * FROM users WHERE username='nwith' LIMIT 1;
# users = User.query.filter_by(username='nwith').first(u)

# SELECT * FROM users WHERE ud=2 LIMIT 1;
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%water%'; 
# users = User.query.filter(User.email.like("%water%")).all()

#ORDER
#users = User.query.order_by(User.username).all()

#LIMIT
#users = User.query.limit(1).all()

#OFFSET
#users = User.query.offset(2).all()

#ORDER + LIMI + OFFSET
#users = User.query.order_by(User.username).limit(1).offset(2).all()
