import jason

class file_path:
    food_items = 'C:\Users\LENOVO\AppData\Local\Programs\Python\Python311\sample.txt'
    user_pass = 'C:\Users\LENOVO\AppData\Local\Programs\Python\Python311\user_pass.json'
    order_history = 'C:\Users\LENOVO\AppData\Local\Programs\Python\Python311\order_history.json'

class choice:
    def admin_choice(self,oper_choice):

        if oper_choice == 1:
            foodiez.add_items()
        elif oper_choice == 2:
            foodiez.edit_items()
        elif oper_choice == 3:
            foodiez.view_items()
        elif oper_choice == 4:
            foodiez.remove_items()
        elif oper_choice ==5:
            exit()

    def user_choice(self,oper_choice,name):

        if oper_choice ==1:
            foodiez_user.palce_order(name)
        elif oper_choice == 2:
            foodiez_user.order_history(name)
        elif oper_choice == 3:
            foodiez_user.update_profile(name)
        elif oper_choice == 4:
            exit()

class foodiez_admin_function:
     read_file = open(file_path.food_items,'r+')
     file_data = json.load(read_file)
     def add_items(self):

         if len(self.file_data['menu items']) == 0:
             ID = 1
         else:
             ID = self.file_data['menu items'][-1]['ID'] + 1
         name = input('enter food name :')
         quantity = input('enter food quantity :')
         price = float(input('enter food price :'))
         discount = float(input('enter food discount :'))
         stock = int(input('enter stock :'))
         dict_obj = {
                     'ID':ID,
                     'name':name,
                     'quantity':quantity,
                     'price':price,
                     'discount':discount,
                     'stock':stock
             }
         self.file_data['menu items'].append(dict_obj)
         write_file = open(file_path.food_items,'w')
         json.dump(self.file_data,write_file)
         print('\nfood item successfully added!')

     def edit_items(self):
         for i in self.file_data['menu items']:
             print(i,'\n')

         ID = int(input('\nenter ID of them to edit from above items list : ')
         for i in range(len(self.file_data['menu items'])):
             if ID == self.file_data['menu items'][i]['ID']:
                  print('\n',self.file_data['menu items'][i])
                  print('\n+------------------------------+\n|enter 1 to edit food name  | \n|enter 2 to edit food quantity | \n|enter 3 to edit food price   |\n|enter 4 to edit discount   |\n|enter 5 to edit stock     |\n+------------------------------+\n')
                  edit_choice = int(input('\nenter your choice :'))
                  new_value = input = input('\nenter new value :')
                  if edit_choice == 1:
                      self.file_data['menu items'][i]['name'] = str(new_value)
                      print('\nfood item successfully updated!')
                  elif edit_choice == 2:
                      self.file_data['menu items'][i]['quantity'] = str(new_value)
                      print('\nfood item successfully updated!')
                  elif edit_choice == 3:
                      self.file_data['menu items'][i]['price'] = int(new_value)
                      print('\nfood item successfully updated!')
                  elif edit_choice == 4:
                      self.file_data['menu items'][i]['discount'] = float(new_value)
                      print('\nfood item successfully updated!')
                  elif edit_choice == 5:
                      self.file_data['menu items'][i]['stock'] = int(new_value)
                      print('\nfood item successfully updated!')
                  else:
                      print('invalid choice')
         
         write_file = open(file_path.food_items,'w')
         json.dump(self.file_data,write_file)


       def view_items(self):

           for i in self.file_data['menu items']:
               print(i,'\n')

       def remove_items(self):

           for i in self.file_data['menu items']:
               print(i,'\n')

           ID = int(input('\nenter ID of item to remove from above items list: '))
           for i in range(len(self.file_data['menu items'])):
               if ID == self.file_data['menu items'][i]['ID']:
                   del self.file_data['menu items'][i]
                   print('\nfood item successfully removed')
           write_file = open(file_path.food_items,'w')
           json.dump(self.file_data,write_file)

class Log:

    file = open(file_path.user_pass)
    file_data = json.load(file)
    def admin_login(self):

        user = input('\nadmin enter username : ')
        pwd = input('enter password : ')
        for i in self.file_data['users']:
            if (user_phone == i['full name'] and pwd == i['password']):
                while true:
                    print('\n+-----------------------------------+\n|enter 1 to place new order   |\n|enter 2 to view order history | \n|enter 3 to update profile   |\n|enter 4 to exit          |\n+-----------------------+\n')
                    oper_choice = int(input('enter your choice :- '))
                    choice.user_choice(oper_choice,i['full name'])
            else:
                print('wrong username or password')

class foodiez_user_function():
    read_file = open(file_path.food_items,'r+')
    file_data = json.load(read_file)
    def place_order(self,name='Dhruv jha'):
        print('\nt\tmenu\n')
        for i in self.file_data['menu items']:
            print(f'{i['ID']}  {i['name']}  ({i['quantity']})  INR{i['price']}]\n')
        food_choice = input('enter your choice in [1,2,....] format : ')
        dict_obj = {
                    name:{
                    }
            }
        count=1
        for j in food_choice:
            if j.isdigit():

                dict_obj[name][count] = self.file_data['menu items'][int(j)-1]
                count+=1
        print('\n selected items')
        for i in dict_obj[name]:
            print(f'\n{i}  {dict_obj[name][i]['name']}  ({dict_obj[name][i]['quantity']})  INR[{dict_obj[name][i]['price']}]\n')
        confirm = int(input('enter 1 to place order or 2 to exit : '))
        if confirm == 1:
            print('\norder placed!')
            order_history_file = open(file_path.order_history,'r+')
            new_data = json.load(order_history_file)
            new_data['history'].append(dict_obj)
            write_file = open(file_path.order_history,'w')
            json.dump(new_data,write_file)
        else:
            print('\nsee you soon')
            
    def order_history(self,name):
        file = open(file_path.user_pass)
        read_profile = json.load(file)

        for i in range(len(read_profile['users'])):
            if name == read_profile['users'][i]['full name']:
                print('\n',read_profile['users'][i])
                print('\n+----------------------------+\n|enter 1 to edit full name  |\n|enter 2 to edit phone number | \n|enter 3 to edit email    \n|enter 4 to edit address   |\n|enter 5 to password    |\n+----------------------+\n')
                edit_choice = int(input('\nenter your choice : '))
                new_value = input('\nenter new value : ')
                if edit_choice == 1:
                    read_profile['users'][i]['full name'] = str(new_value)
                    print('\ninfo successfully updated!')
                elif edit_choice == 2:
                    read_profile['users'][i]['phone number'] = int(new_value)
                     print('\ninfo successfully updated!')
                elif edit_choice == 3:
                    read_profile['users'][i]['email'] = str(new_value)
                    print('\ninfo successfully updated!')
                elif edit_choice == 4:
                    read_profile['users'][i]['address'] = str(new_value)
                    print('\ninfo successfully updated!')
                elif edit_choice == 5:
                    read_profile['users'][i]['password'] = str(new_value)
                     print('\ninfo successfully updated!')
                else:
                    print('invalid choice')

         write_file = open(file_path.user_pass,'w')
         json.dump(read_profile,write_file)
         exit()

choice = choice()
foodiez = foodiez_admin()
log = log()
foodiez_user = foodiez_user()
                    
                    
                    
               
