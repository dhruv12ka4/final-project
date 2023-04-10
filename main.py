from foodiez.py import *

class main:
    def execute(self,log_choice):
        if log_choice == 1:
            log.admin_login()

        elif log_choice == 2:
             while true:
                 print('\n+---------------------------------------+\n|enter 1 to register          | \n|enter 2 to login if already register |\n+------------------------------+=)
                 reg_choice = int(input('enter your choice :- '))
                 if reg_choice == 1:
                       log.register()
                 elif reg_choice == 2:
                     log.user__login()
                 else:
                     print('invalid choice')

        else:
            print('see you soon')
            exit()
            
print('                                        welcome to foodiez')
print('+-------------------------+\n|enter 1 to login as admin | \n|enter 2 to login as user  |\n+----------------------+\n')
log_choice = int(input('enter your choice :- '))
main = main()
main.execute(log_choice)
