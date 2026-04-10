class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictt = {}
        for i in s1:
            dictt[i] = dictt.get(i, 0) + 1
        winl = 0
        winr= len(s1)
        for _ in range(len(s2) - len(s1) + 1):
            dictt2 = {}
            for i in s2[winl:winr]:
                dictt2[i] = dictt2.get(i,0)+1
            if dictt2 == dictt:
                return True
            else:
                winl+=1
                winr+=1
        return False

