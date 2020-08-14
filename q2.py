# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import *

class Solution:
    def addTwoNumbers(self, l1, l2):
        inList = True
        i = 1
        currentNode1 = l1
        currentNode2 = l2
        outputDict = {}
        carryOver = False
        carryOverValue = 0
        outputNodeValue = 0
        list1End = False
        list2End = False
        if currentNode1.val == None:
            list1End = True
        if currentNode2.val == None:
            list1End = True

        while inList == True:
            if list1End == False and list2End == False:
                outputNodeValue = (currentNode1.val) + (currentNode2.val)
            elif list1End == True:
                outputNodeValue = currentNode2.val
            elif list2End == True:
                outputNodeValue = currentNode1.val

            if carryOver == True:
                outputNodeValue += carryOverValue
                carryOver = False
            if outputNodeValue > 9:
                carryOver = True
                carryOverValue = 1
                outputNodeValue -= 10

            outputDict.update({('lOn%s' % str(i)) : ListNode(outputNodeValue)})

            if i > 1:
                outputDict['lOn%s' % str(i-1)].next = outputDict[('lOn%s' % str(i))]

            if (currentNode1.next != None) and (currentNode2.next != None):
                currentNode1 = currentNode1.next
                currentNode2 = currentNode2.next
                i += 1
            else:
                if (currentNode1.next == None) and (currentNode2.next == None):
                    if carryOver == True:
                        i += 1
                        outputDict.update({('lOn%s' % str(i)) : ListNode(carryOverValue)})
                        outputDict['lOn%s' % str(i-1)].next = outputDict['lOn%s' % str(i)]
                        inList = False
                    else:
                        inList = False

                elif currentNode1.next == None:
                    list1End = True
                    currentNode2 = currentNode2.next
                    i += 1
                elif currentNode2.next == None:
                    list2End = True
                    currentNode1 = currentNode1.next
                    i += 1

        return outputDict['lOn1']

class ListNode:
     def __init__(self, val, next = None):
         self.val = val
         self.next = next

l1n1 = ListNode(5)
#l1n2 = ListNode(8)
#l1n3 = ListNode(3)
#l1n1.next = l1n2
#l1n2.next = l1n3


l2n1 = ListNode(5)
#l2n2 = ListNode(6)
#l2n3 = ListNode(4)
#l2n1.next = l2n2
#l2n2.next = l2n3

S = Solution()
print(S.addTwoNumbers(l1n1, l2n1))
