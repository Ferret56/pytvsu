def solution(pwd):
    numbers=['1','2','3','4','5','6','7','8', '9', '0']
    letters_small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    N = False
    l = False
    L = False
    for i in range(len(pwd)):
        if pwd[i] in numbers :
            N = True
        if pwd[i] in letters_small:
            l=True;
        if pwd[i] in letters_big:
            L = True
    if len(pwd) > 9 and N and  l and L: 
        return True
    else:
        return False

