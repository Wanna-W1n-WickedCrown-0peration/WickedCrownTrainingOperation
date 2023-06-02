alphabet = "abcdefghijklmnopqrstuvwxyz"
while True:
    key = input("Entering keyword : ").strip()
    what = False
    for i in key:
        if i not in alphabet:
            print("Lmao no. Enter again!!!!")
            what = True
            break 
    if not what:
        break

renewalphabet = ""
for i in key:
    if i in renewalphabet:
        pass 
    else:
        renewalphabet += i

for i in alphabet:
    if i in renewalphabet:
        pass
    else:
        renewalphabet += i

print(f"Old alphahet : {alphabet}")
print(f"New alphabet : {renewalphabet}")

plaintext = input("Enter message - plaintext to encrypt : ")
encrypt = ""
for i in plaintext:
    if i in renewalphabet:
        encrypt += renewalphabet[alphabet.index(i)]
    else:
        encrypt += i
print("Encrypted :", encrypt)