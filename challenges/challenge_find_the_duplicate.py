def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums:
        return False
    nums = sorted(nums)
    for index, num in enumerate(nums):
        if index == len(nums) - 1 or isinstance(num, str) or num < 0:
            return False
        if num == nums[index + 1]:
            return num
