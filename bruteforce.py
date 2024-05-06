'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        print(f"[+] Password found: {password}")
        return True
    except Exception as e:
        print(f"[-] Incorrect password: {password}")
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            with open('rockyou.txt', 'rb') as f:
                for line in f:
                    password = line.strip().decode()
                    if attempt_extract(zf, password):
                        break

    #print("[+] Password not found in list")

if __name__ == "__main__":
    main()