"""
706. Design HashMap
Easy: Hash Table, Objective oriented design (OOD)

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.entry_size_ = 100
        self.entry_list_ = [[] for _ in range(self.entry_size_)]
        
    def hash_func(self, key: int) -> int:
        return key % self.entry_size_
    
    def get_entry(self, key: int) -> int:
        entry_idx = self.hash_func(key)
        return self.entry_list_[entry_idx]  
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        entry = self.get_entry(key)
        for i in range(len(entry)):
            if entry[i][0] == key:
                entry[i][1] = value
                return
        entry.append([key, value])
                
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        entry = self.get_entry(key)
        for i in range(len(entry)):
            if entry[i][0] == key:
                return entry[i][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        entry = self.get_entry(key)
        position = -1
        for i in range(len(entry)):
            if entry[i][0] == key:
                position = i
                break
        if position != -1:
            return entry.pop(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)