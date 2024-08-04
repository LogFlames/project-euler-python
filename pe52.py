x = 0

def testFun(x, k):
    nums = list(str(x))
    nums2 = list(str(k * x))
    for n in range(len(nums2)-1, -1, -1):
        if nums2[n] not in nums:
            return False
        else:
            for a in range(len(nums)-1, -1, -1):
                if nums2[n] == nums[a]:
                    del nums[a]
    return True

while True:
    x += 1
    indicator = True
    for k in range(2, 7):
        if not testFun(x, k):
            indicator = False
            break
    if indicator:
        break

print x
