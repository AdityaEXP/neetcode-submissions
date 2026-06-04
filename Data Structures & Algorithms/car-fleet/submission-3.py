class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # creating hashmap of position -> speed
        hmap = dict()
        n = len(speed)

        for i in range(n):
            hmap[position[i]] = speed[i]
        
        position.sort(reverse=True)
        
        cars = []

        for x in position:
            cars.append((x, hmap[x]))

        # computing time for each car
        time = []

        for car in cars:
            p, s = car
            t = (target - p) / s
            time.append(t)

        # preparing stack
        stack = []

        for i in range(n):
            t = time[i]

            if stack and (stack[-1] >= t):
                continue
            
            stack.append(t)
        
        return len(stack)
        