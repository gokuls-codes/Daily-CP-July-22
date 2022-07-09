'''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''

class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        # Code here
        p1 = poly1
        p2 = poly2
        
        ans = node(-1, -1)
        temp = ans
        
        while p1!=None and p2!=None:
            if p1.power == p2.power:
                temp.next = node(p1.coef + p2.coef, p1.power)
                p1 = p1.next
                p2 = p2.next
            elif p1.power > p2.power:
                temp.next = node(p1.coef, p1.power)
                p1 = p1.next
            else:
                temp.next = node(p2.coef, p2.power)
                p2 = p2.next
            temp = temp.next
            
        while p1!=None:
            temp.next = node(p1.coef, p1.power)
            temp = temp.next
            p1 = p1.next
        
        while p2!=None:
            temp.next = node(p2.coef, p2.power)
            temp = temp.next
            p2 = p2.next
            
        return ans.next