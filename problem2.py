#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a,b,c):
    if a > b:
        if a > c:
            hype = a
            A = b
            B = c
        elif c > a:
            hype = c
            A = a
            B = b
    elif a < b:
        if b > c:
            hype = b
            A = a
            B = c
        elif b < c:
            hype = c
            A = a 
            B = b
    elif a == b:
        if c > a:
            hype = c
            A = a 
            B = b
        elif c == a:
            return 1
    st = hype**2
    ts = A**2 + B**2
    K = A + B
    if st == ts:
        return 2
    elif hype > K:
        return 0
    elif st > ts:
        return 3
    elif st < ts:
        return 1

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
