
num =4000



hexdict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'f'
}

#find length of an int
def fintlen(a):
    temp = 0
    while True:
        if a >= 1:
            a /= 10
            temp += 1
        if a < 1:
            return(temp - 1)
            
#
#round down
def rounddown(a):
    tmp = round(a)
    if a >= tmp:
        return (tmp)
    if a < tmp:
        return (tmp - 1)
#
#decimal to hex using convertion table aka |ect...|16**3|16**2|16**1|16**0|
#                                          |ect...|4096 |256  |16   |1    |
def dectohex(a):
    tmplen = fintlen(a)
    sub = a
    tmp = 0
    tmpar = []
    result = ""
    #decimal to hex in array
    while True:
        
        #puts hex value into an array
        if sub / (16**tmplen) <= 16:
            tmpar.append( rounddown(sub / (16**tmplen)))
            sub -= ( (16**tmplen) * rounddown(sub / (16**tmplen)))
        if tmplen == 0:
            break
        tmplen -= 1
    #
    while True:
        #cleans and turns the array into an string
        for i in range(len(tmpar)):
            if tmpar[i] == 0:
                tmpar.pop(i)
            elif tmpar[i] != 0:
                break
        #
        for i in range(len(tmpar)):
            result += hexdict[tmpar[i]]
        #
        return(result)

def main():
    a = dectohex(num)
    print(a)
#
    
main()