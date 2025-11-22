class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input=input("""Welcome to chatbook!!
                            1. press 1 to sign up
                            2. press 2 to sign in
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                         """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email=input("enter you email for signup: ")
        pwd=input("set your password: ")
        self.username=email
        self.password=pwd
        print("sign up successful")
        self.menu()
    
    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname=input("enter you email for signup: ")
            pwd=input("set your password: ")
            if self.username==uname and self.password==pwd:
                print("you have loggedIn successfully")
                self.loggedin=True
            else:
                print("input correct credentials")
        self.menu()
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

user=chatbook()