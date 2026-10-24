import requests
usr = input("Enter user name: ")
def find(usr):
    fin = requests.get(f"https://whois.com/whois/{usr}")
    return fin.text

a = find(usr)
print(a)