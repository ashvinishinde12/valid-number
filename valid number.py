import re
def isvalid(s):
    Pattern=re.compile(r"\+?\b[\d]{3}-[\d]{3}-[\d]{4}\b" )
 
    return Pattern.match(s)
s="+212-456-7890"
if(isvalid(s)):
    print("valid number")
else: print("invalid")
          
 
