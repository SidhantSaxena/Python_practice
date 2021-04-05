class Facebook:
    registered_user=[]

    @staticmethod
    def registration(user_obj):
        for user in Facebook.registered_user:
            if user["user_email"]==user_obj["user_email"]:
                return False
        else:
            Facebook.registered_user.append(user_obj)
            return True

def mutual_friends(user_m1,user_m2):
        mutuals = [i for i in user_m1.friends for j in user_m2.friends if i==j]
        print(f"mutuals:{mutuals}")        
            
def addFriends(user):
        index = int(input("Select"))
        if index != Facebook.registered_user.index(user.__dict__):
            user.friends.append(Facebook.registered_user[index]["user_name"])
            print(user.__dict__)
        else:
            print("Select from the given options")            
            



class Sign_up(Facebook):
    def __init__(self,name,email,pwd,age):
        self.user_name=name
        self.user_email=email
        self.user_pwd=pwd
        self.user_age=age
        self.friends=[]
        status=Sign_up.registration(self.__dict__)
        if status:
            print("Succesfully registered")
        else:
            print("Email Already Exist")    
    def showFacebookuser(self):
        for user in Sign_up.registered_user:
            if self.user_name!=user['user_name']:
                index = Sign_up.registered_user.index(user)
                print(f"{index}---{user['user_name']}")



user1 = Sign_up("Rajiv","rajiv@gmail.com",12345,24)
user2 = Sign_up("ajiv","ajiv@gmail.com",12345,24)
user3 = Sign_up("Ajay","ajay@gmail.com",12345,24)
user4 = Sign_up("sam","sam@gmail.com",12345,24)
user1.showFacebookuser()
addFriends(user1)
addFriends(user1)
addFriends(user2)
addFriends(user2)
mutual_friends(user1,user2)

