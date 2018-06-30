class Menu():
    def main_menu(self):
        command = ""
        while command != "q":
            command = input("Enter (r) to register and (l) to login: ")
            print(command)
            if command == "r":
                print("register")
            elif command == "l":
                print("loging")
            elif command == "q":
                print("quit the program")
                command = "q"
            else:
                print("command unavailable")

         
            
            
           
            
             
            
        



     

   
