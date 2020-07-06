"""
791. Custom Sort String
Medium: String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
"""
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        chara_order, order_chara = {}, {}
        T_order, not_in = [], []
        for i in range(len(S)):
            chara_order[S[i]] = i
            order_chara[i] = S[i]
        for t in T:
            if t in chara_order:
                T_order.append(chara_order[t])
            else:
                not_in.append(t)
        T_order.sort()
        for j in range(len(T_order)):
            T_order[j] = order_chara[T_order[j]]
        return "".join(T_order + not_in)

    # 1 line solution
    def customSortString2(self, S: str, T: str) -> str:
        return "".join(sorted(T, key = lambda x: S.index(x) if x in S else 0))
