#szövegből kiválasztjuk a leghoszabbat

ss = "szépséges leg hosz abb szó"

def keres_elso_leghoszabb_szo(string):
    szavak = string.split()
    return_string = " "
    print(string)
    for substring in szavak:
        if len(substring) > len(return_string):
            return_string = substring
    return return_string


def keres_utolso_leghoszabb_szo(string):
    szavak = string.split()
    return_string = " "
    print(string)
    for substring in szavak:
        if len(substring) >= len(return_string):
            return_string = substring
    return return_string

