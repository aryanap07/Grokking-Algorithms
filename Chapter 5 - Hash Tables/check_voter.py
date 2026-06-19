voted = {
    "arpan": True
}

def check_voter(name):
    if voted.get(name):
        print("Kick Them Out!")
    else:
        voted[name] = True
        print("Let Them Vote.")

check_voter("appu")
check_voter("arpan")
print(voted)