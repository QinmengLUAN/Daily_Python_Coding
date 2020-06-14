"""
599. Minimum Index Sum of Two Lists
Easy: Hash Table

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lis_counter = Counter(list1 + list2)
        res = {}
        for i in range(len(list1)):
            if lis_counter[list1[i]] == 2:
                res[list1[i]] = i
        
        for j in range(len(list2)):
            if lis_counter[list2[j]] == 2:
                res[list2[j]] += j
        
        res_val = min(res.values())
        res_lis = []
        for item in res:
            if res_val == res[item]:
                res_lis.append(item)
        return res_lis