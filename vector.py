"""
- HELP

# Start osint for nickname
$ python vector.py nickname

# Start vector web [nickname,email,phone]

"""

import typer

import vapi

def is_ip(ip):
    if(ip.count(".")==3):
        return True
    else:
        return False

def main(vinp: str):
    
    email = False
    em = ["@outlook", "@gmail", "@hotmail", "@yahoo"]
    bnck = ""
    for i in em:
        if(i in vinp):
            tnick = vinp
            email = True
            bnck = tnick.split(i)[0]

    if(vinp == "v" or vinp == "V" or vinp == "help" or ("help" in vinp)):       vapi.help()
    elif("thesaderror" in vinp.lower()):                                        vapi.T()
    elif(vinp=="web"):                                                          vapi.web()
    elif(email==True):                                                          vapi.email(vinp,bnck)
    elif(is_ip(vinp)):                                                          vapi.geos(vinp)
    else:                                                                       vapi.cli(vinp)


if __name__ == "__main__":
    vapi.clear()
    typer.run(main)