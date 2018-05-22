import re

def str_xmid(dss,ks1,ks9):
    #s="abcd232" ;x=str_xmid(s,'b','2');print(x)
    mx=''.join(['(',ks1,')(.*?)(',ks9,')']);
    r = re.search( mx,dss)
    dat=''
    if r:dat=r.groups()[1]
    return dat