from .entities.User import User

class userModel():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql=""" SELECT id, username, password FROM users WHERE username='{}' """.format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row['id'], row['username'], User.check_password(row['password'], user.password) )

            else:
                return None
        except Exception as ex:
            print('An exception occurred')
            print(ex)
            
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = """ SELECT id, username FROM users WHERE id='{}' """.format(id)
            cursor.execute(sql)
            row= cursor.fetchone()
            if row != None:
                print(row)
                return User(row['id'], row['username'], None)
            
        except Exception as ex:
            print('An exception occurred')
            print(ex)