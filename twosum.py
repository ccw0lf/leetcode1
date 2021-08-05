class Solution(object):
    def twoSum( nums, target):
        
        start = 0 
        end = len(nums)-1
        
        while start < end:
            result=[]
            
            
            if nums[start] + nums[start+1] ==target:
                
                num1=(nums[start])
                num2= (nums[start+1])

                print(num1,num2)

                result.append (nums.index(num1))
                result.append (nums.index(num2))
                
                print (result)
                
            
                
            start+=1
            
Solution.twoSum(nums=[3,3],target=6)
