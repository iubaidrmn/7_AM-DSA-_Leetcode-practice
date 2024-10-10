class Solution(object):
    def runningSum(self, nums):
        #len(nums) of array tell size of array
        n_array=[]
        c = 0
        for i in range(len(nums)):
            c += nums[i]
            n_array.append(c)
            # n_array = n_arry.append(nums(i) + nums(i+1))
        return n_array
    

       
       
       
       
       
       
        # sum_list = []
        # current_sum = 0
        # for i in range(len(nums)):
        #     current_sum += nums[i]
        #     sum_list.append(current_sum)
        # return sum_list
        