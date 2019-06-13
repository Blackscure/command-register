from db import users

class Menu():
    def main_menu(self):
        command = ""
        while command != "q":
            command = input("Enter (r) to register and (l) to login: ")
            if command == "r":
                self.register()
            elif command == "l":  
                self.login()

               
                
            elif command == "q":
                print("quit the program")
                command = "q"
            else:
                print("command unavailable")

     
    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        new_user = {'name': name, 'password': password}
        

        id = len(users) + 1
        

        users[id] = new_user

        

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        self.validation(name, password)

        print(users)
        for user in users:
            if name == users[user]['name'] and password == users[user]['password']:
                print("you are clear to login.")
                return

        print('You have not registered or your password does not match')
        return

    def validation(self, name, password):
        self.name = name
        self.password = password
        if name == name:
            print("checked")
        if password == password:
            print("password checked!")



        
             
         

        
    
        

        

        

         
        
      


         
            
            
           
            
             
            
        



     

   
