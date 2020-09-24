class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst1 = l1.reverse()
        lst2 = l2.reverse()
        lst3 = []
        for x in range(len(lst1)):
            lst3.append[lst1[x]+lst2[x]]

        for x in lst3:
            num = "".join(x)

l1 = [1,2,3]
l2 = [4,5,6]

add = addTwoNumbers(l1,l2)