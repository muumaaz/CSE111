class User:
    activities = ["Post", "Like", "Comment"]
    def __init__(self, name,email):
        self.name = name
        self.email = email
    def UserActivity(self, activityType):
        if activityType in User.activities:
            return True
        else:
            return False
    def userDetail(self):
        return f"User Detail:\nName:{self.name}\nEmail: {self.email}"

class BracbookUser(User):
    def __init__(self, name, email, phone = "Not set"):
        super().__init__(name, email)
        self.phone = phone
        self.activity = []
        self.log = ''

    def UserActivity(self, log):
        if log in User.activities:
            self.activity.append(log)
            print(f"{self.name} has {log}(d/ed) successfully.")
        else:
            print(f"No activities found like {log}")
    
    def userDetail(self):
        if not self.activity:
            self.log = "No recent activity"
        else:
            self.log = ', '.join(self.activity)
        detail = super().userDetail()
        return f"User Details: {detail} \nPhone: {self.phone} \nActivity log: {self.log}"

user1 = BracbookUser("Rakait","xyz@gmail.com")
print("1===========================")
print(user1.userDetail())
print("2===========================")
user2 = BracbookUser("Sazzad","abc@gmail.com","01727xxxxxx")
print("3===========================")
print(user2.userDetail())
print("4===========================")
user1.UserActivity("Like")
print("5===========================")
user1.UserActivity("Comment")
print("6===========================")
print(user1.userDetail())
print("7===========================")
user2.UserActivity("Share")
print("8===========================")
user2.UserActivity("Comment")
print("9===========================")
print(user2.userDetail())
