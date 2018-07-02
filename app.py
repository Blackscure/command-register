from db import user

class Menu():
    def main_menu(self):
        command = ""
        while command != "q":
            command = input("Enter (r) to register and (l) to login: ")
            print(command)
            if command == "r":
                self.register()
                print("you have regisred! ", user)
            elif command == "l":
                self.login()
                print("you have loged in! ")
            elif command == "q":
                print("quit the program")
                command = "q"
            else:
                print("command unavailable")
                

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        
        new_user = {'name': name, 'password': password}

        new_user[name][password] = name, password

        
        print('new_user')

        
        

        

    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        new_user = {'name': name, 'password': password}
        

        id = len(user) + 1
        

        user[id] = new_user
        

        

        

         
        
      


         
            
            
           
            
             
            
        



     

   
