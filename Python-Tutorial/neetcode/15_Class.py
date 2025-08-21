class Myclass:
    # constructor
    # self is like this keyword
    def __init__(self,nums): 
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as parameter
    def getLength(self): # method
        return self.size
    
    def getDoubleLength(self): # member func calling another member func
        return 2 * self.getLength()
