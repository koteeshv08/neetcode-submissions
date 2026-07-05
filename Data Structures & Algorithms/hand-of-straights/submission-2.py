class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        while(len(hand)):
            l=min(hand)
            hand.remove(l)
            temp = [l]
            print(l,temp)
            for i in range(1,groupSize):
                if (l+i) in hand:
                    temp.append(l+i)
                    hand.remove(l+i)
                else:
                    return False
            print(temp)
        return True