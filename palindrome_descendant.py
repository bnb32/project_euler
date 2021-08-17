def is_palindrome_descendant(N):
    if str(N)==str(N)[::-1]: return True
    s=str(N)
    while len(s)>2:    
        s=''.join([str(int(s[i])+int(s[i+1])) for i in range(0,len(s)-1,2)])
        if s==s[::-1]: return True
    
    return False

print(is_palindrome_descendant(123312))    
print(is_palindrome_descendant(11211230))    
print(is_palindrome_descendant(13001120))    
print(is_palindrome_descendant(11))    
