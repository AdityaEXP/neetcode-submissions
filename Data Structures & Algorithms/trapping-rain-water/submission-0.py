class Solution:
    def trap(self, height: List[int]) -> int:

        h = height

        w=0
        L=[0]
        R=[0]
        for i in range(len(h)):
            if h[i]>L[i]:
                L.append(h[i])
            else:
                L.append(L[i])
        for i in range(len(h)):
            if h[len(h)-1-i]>R[i]:
                R.append(h[len(h)-1-i])
            else:
                R.append(R[i])
        for j in range(len(h)):
            w+=min(L[j+1],R[-(j+1)])-h[j]

        

        return w

        
