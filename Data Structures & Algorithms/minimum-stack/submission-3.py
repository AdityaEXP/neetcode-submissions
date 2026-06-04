class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        
        if not self.min_arr or val <= self.min_arr[-1]:
            self.min_arr.append(val)

        print(self.arr)
        print(self.min_arr)
        

    def pop(self) -> None:
        top_element = self.top()
        self.arr.pop()
        if top_element == self.min_arr[-1]:
            self.min_arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
