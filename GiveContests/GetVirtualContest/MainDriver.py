from . import try_virtual


def letsGo(user,div):

    ok=try_virtual.TryTheseContests(user,div)

    if(ok[0]): print("Success!!")
    else: print("Error!!!")

    return ok




# CHANGE THIS [user] TO YOUR CODEFORCES HANDLE
# user='deepanshu_pali'


# letsGo(user)