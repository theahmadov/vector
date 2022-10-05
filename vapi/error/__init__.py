from vapi.poor import *

class error_:
    #exp_(err,parm):
    code = {
        "0x1" : "[{}!{}] {}ConnectionError!{} Please try to connect internet.",
        "0x2" : "[{}!{}] An error occured while connecting to {}{}{} website..."
    }


def exp(err,parm,nick):
    if(parm==None):
        return error_.code[f"{err}"].format(color.CRED,color.CWHITE,color.CWHITE2,color.CWHITE)
    else:
        return error_.code[f"{err}"].format(color.CRED,color.CWHITE,color.CWHITE2,parm.format(nick),color.CWHITE)