class chatbook:

    def __init__(self):
        self.userName = ''
        self.password = ''
        self.isLoggedIn = False
        self.mainMenu()


    def mainMenu(self):
        userInput = input('''Welcome to chatbook how you woud like to proceed
                          press 1 to go signup
                          press 2 to signin
                          press 3 to write a post
                          press 4 to write a message
                          press any other key to exit''')
        
        if userInput == "1":
            self.signup()
        elif userInput == "2":
            self.signin()
        elif userInput == "3":
            self.writeAPost()
        elif userInput == "4":
            self.mainMenu()
        else:
            exit()

    def signup(self):
        self.userName = input("enter you username")
        self.password = input("enter your password")
        print("you have signup successfully !!")
        print("\n")
        self.mainMenu()

    def signin(self):
        if self.userName == '' and self.password == '' :
            print("first go to signup then signin...")
        
        else:
            user = input("enter your username")
            pwd = input("enter you password")
            if user == self.userName and pwd == self.password:
                print("you have signed in successfully")
                self.isLoggedIn=True
            else:
                print("credentials are wrong")
        print("\n")
        self.mainMenu()


    def writeAPost(self):
        if self.isLoggedIn != True:
            print("first signin..")
            
        else:
            post = input("write a post")
            print(f"This is the post you want to signin {post}")

        print("\n")
        self.mainMenu()


    def sendMsg(self):
        if self.isLoggedIn != True:
            print("First go to signin then you would be eligible to post")

        else:
            frnd = input("whom you want to send message")
            msg = input("enter your message here  ")
            print(f"{msg} is the msg you want to send to {frnd} ")
        
        print("\n")
        self.mainMenu()




chat = chatbook()