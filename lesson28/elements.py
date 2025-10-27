class pair_element:
    def two_sum(self,nums,target):
        lookup = {}
        for i , num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num] = i
value = int(input("Enter the value:"))
print("index1=%d,index2=%d"% pair_element().two_sum((10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300),value))