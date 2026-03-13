import subprocess

def insecure_function(user_input):
    subprocess.call("echo " + user_input, shell=True)

password = "123456"
print("Hardcoded password:", password)

user = input("Enter command: ")
insecure_function(user)
