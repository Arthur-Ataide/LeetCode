def adiciona(string, letra, num):
    if num >= 2:
        string += letra + letra
        num -= 2
        return string, num

    string += letra
    num -= 1
    return string, num

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        string = ''
        for i in range(a+b+c):
            if a > b and a > c:
                if string[-2:] != 'aa' and a > 0:
                    string, a = adiciona(string, 'a', a)

            if b > c:
                if string[-2:] != 'bb' and b > 0:
                    string += 'b'
                    b -= 1
                elif a > c and a > 0 and string[-2:] != 'aa':
                    string += 'a'
                    a -= 1
                elif c > 0 and string[-2:] != 'cc':
                    string += 'c'
                    c -= 1             
            else:
                if string[-2:] != 'cc' and c > 0:
                    string += 'c'
                    c -= 1
                elif a > b and a > 0 and string[-2:] != 'aa':
                    string += 'a'
                    a -= 1
                elif b > 0 and string[-2:] != 'bb':
                    string += 'b'
                    b -= 1    
        return string
