import requests,json,os
def tokenchange():#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    os.system('cls')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    with open('token.json', 'r') as f:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        jdata = json.load(f)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    token = jdata["token"]#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    if token == "":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        hmm = print("[?] Token is not set Do you want to set it? (Y/N) : ")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        if hmm == "Y":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            tokenset(select)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        elif hmm == "N":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            exit()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            os.system('cls')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            print("[!] Invaild select")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            tokenchange()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        hid = int(input("[?] Type the desired house ID : "))#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        if hid == 1:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            r = requests.post("https://discord.com/api/v9/hypesquad/online", json={"house_id": hid}, headers={"Authorization": token})#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            if r.status_code == 204:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Successful changed!")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Failed change! Please check your token.")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        elif hid == 2:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            r = requests.post("https://discord.com/api/v9/hypesquad/online", json={"house_id": hid}, headers={"Authorization": token})#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            if r.status_code == 204:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Successful changed!")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Failed change! Please check your token.")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        elif hid == 3:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            r = requests.post("https://discord.com/api/v9/hypesquad/online", json={"house_id": hid}, headers={"Authorization": token})#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            if r.status_code == 204:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Successful changed!")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                print("[!] Failed change! Please check your token.")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
                os.system('pause')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            os.system('cls')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            print("[!] Invaild select")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
            tokenchange()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
def tokenset(select):#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    os.system('cls')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    with open('token.json', 'r') as f:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        jdata = json.load(f)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    token = input("[?] Type your token : ")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    data = {"token":token}#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    with open('token.json', 'w') as outfile:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        json.dump(data, outfile, indent=4)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    menu()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
def menu():#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    os.system('cls')#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    main="""
        ┌─  Discord hypesquad Changer ────────────────────┐
        │                                                 │
        │  [1] TOKEN SETTING                              │
        │  [2] CHANGER                                    │
        │                                                 │
        └─────────────────────────────────────────────────┘
        Made By 이미지#0001
    """#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    print(main)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    global select#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    select = input("> ")#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    if select == "1":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        tokenset(select)#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    elif select == "2":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        tokenchange()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
    else:#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
        menu()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
if __name__ == "__main__":#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
	menu()#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001#Made By 이미지#0001
