def solution(text, ending):
    t = text
    e = ending

    if len(e) > len(t):
        print ("NAO deu bom :(")
        return False
    elif len(e) == len(t):
        if e == t:
            print ("deu bom")
            return True
        else:
            print ("NAO deu bom :(")
            return False
    else:
        reference = (len(t) + 1) - (len(e) + 1)
        for i in range(reference):
            if t[reference:] == e:
                print ("deu bom")
                return True
            else:
                print("NAO deu bom :(")
                return False

solution("aaaa", "bbbb")

