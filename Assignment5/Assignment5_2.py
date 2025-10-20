def ChkVowel(ch):
    Vowel='aeiouAEIOU'
    if ch in Vowel:
        return True
    else:
        return False

def main():
    str=input("Enter a character:")
    result=ChkVowel(str)
    
    if result==True:
        print(f"{str} is a vowel")
    else:
        print(f"{str} is not a vowel")

if __name__=="__main__":
    main()