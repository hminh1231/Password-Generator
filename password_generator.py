import random
import string

class Password:
    def menu(self):
        '''This function will print out the main menu of the application'''
        print('Welcome to your password generation application.')
        print('Please choose one of the options below here:')
        print('1. Generate passwords')
        print('2. Exit')
        
    def strength(self):
        '''This function will ask user how strong of the password that they want and return their choice'''
        print('So how strong of password that you want?')
        print('1. Low (just numbers only)')
        print('2. Normal (letters only)')
        print('3. Strong (letters and numbers combine)')
        print('4. Very strong (letters + numbers + symbols)')
        while 1:
            try:
                pass_strength = int(input('Now tell me your choice: '))
                if pass_strength not in range(1,5):
                    print('You need to choose from the range of the option only.')
                else:
                    break
            except ValueError:
                print('Try not to make mistake again, your input must be a number only')
        return pass_strength
        
    def passgenerate(self):
        while 1:
            try:
                length = int(input('Please enter the length of the password that you want to generate: '))
                if length not in range(12):
                    print('What? You want a password more than 12 letters? Are you trying to protect White House secret files? Come on buddy.')
                else:
                    break
            except ValueError:
                print('Your input must be a number')
        pass_combine = string.ascii_letters + string.digits + string.punctuation #This will generate letters, numbers and symbols character
        pass_strong = string.ascii_letters + string.digits
        pass_normal = string.ascii_letters
        pass_low = string.digits
        pass_option = self.strength()
        if pass_option == 1:
            generate_pass = ''.join(random.choice(pass_low) for _ in range(length))
            print(f'Your password is: {generate_pass}')
        elif pass_option == 2:
            generate_pass = ''.join(random.choice(pass_normal) for _ in range(length))
            print(f'Your password is {generate_pass}')
        elif pass_option == 3:
            generate_pass = ''.join(random.choice(pass_strong) for _ in range(length))
            print(f'Your password is: {generate_pass}')
        else:
            generate_pass = ''.join(random.choice(pass_combine) for _ in range(length))
            print(f'Your password is: {generate_pass}')
            
    def options(self):
        while 1:
            try:
                option = int(input('So tell me your choice: '))
                if option not in range(1,3):
                    print('You must choose 1 or 2 only')
                else:
                    break
            except ValueError:
                print("Number only please, don't try anything funny else")
        return option
    
    def display(self):
        self.menu()
        user = self.options()
        if user == 1:
            self.passgenerate()
        else:
            print('Thank you for using me')
            
my_password = Password()
my_password.display()
        
        