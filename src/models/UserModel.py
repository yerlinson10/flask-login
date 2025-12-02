from .entities.User import User

class userModel():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql=""" SELECT * FROM users WHERE username='{}' """.format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                print(row)
                print(User.check_password(row['password'], user.password))
                print(row['password'])
                user = User(row['id'], row['username'], User.check_password(row['password'], user.password) )
                return user
            else:
                return None
        except Exception as ex:
            print('An exception occurred')
            print(ex)