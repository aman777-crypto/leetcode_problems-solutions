def rev(s):
        

        left = 0
        right = len(s.split()) - 1

        while left < right :
            s[left],s[right] =s[right] ,s[left]
        return s




n = "aman"
rev = n[::-1]
print(rev)