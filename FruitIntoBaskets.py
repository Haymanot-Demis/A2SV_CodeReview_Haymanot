import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxSum = 0
        left = 0
        right = 0
        basket = {}
        length = len(fruits)

        while right < length:
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
            maxSum = max(maxSum, right - left + 1)
            right += 1

        return maxSum
