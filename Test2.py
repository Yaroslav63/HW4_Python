nums = [1, 5, 2, 3, 4, 6, 1, 7]
def asc_seq(nums):
    seq = [nums[0]]
    for i in nums:
        if i > max(seq):
            seq.append(i)
    return seq
print(asc_seq(nums))