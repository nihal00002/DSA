class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_doller = 0
        ten_doller = 0
        for i in bills:
            if i == 5:
                five_doller += 1
            elif i == 10:
                if five_doller >= 1:
                    five_doller -= 1
                    ten_doller += 1
                else:
                    return False
            else:
                if i == 20:
                    if five_doller >= 1 and ten_doller >= 1:
                        five_doller -= 1
                        ten_doller -= 1
                    elif five_doller >= 3:
                        five_doller -= 3
                    else:
                        return False
        return True


            