nums = [5,4,3,2,1]
i = 0
j = i+1
for i in range(len(nums)-1):
    if nums[i]>nums[j]:
        nums[i],nums[j]=nums[j],nums[i]
    j = j+1
    
print(nums)