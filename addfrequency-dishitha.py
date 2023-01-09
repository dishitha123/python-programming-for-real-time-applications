def addFrequencyToCharacter(s):
    frequency = [0] * 26
    n = len(s)
    for i in range(n):
        frequency[ord(s[i]) - ord('a')] +=1
    for i in range(n):
        add = frequencyords[i] - ord('a') % 26
        if ord(s[i]) + add <=ord('z'):
            s[i] = chr(ord(s[i]) + add)
        else:
            add = chr(ord('a') + add - 1)
    print("".joinm(s))
if __name__== '__main__':
      str = "ghee"


       addFrequencyTocharacter([i for i in str])
