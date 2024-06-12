#Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring  without repeating characters.
#s = "pwwkew"    Output: 3    Explanation: The answer is "wke"


def substrfinder(inp):
    temp=''
    substr=''
    
    for i in inp:
        if i in temp:
            if len(temp)>len(substr):
                substr=substr+temp
                temp=''
        else:
            temp=temp+i
    return substr


inpstr=input("Enter the string to check: ")
print(substrfinder(inpstr))
