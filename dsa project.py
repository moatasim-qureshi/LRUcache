# We are implementing a least recently used cache data structure using hashmaps and doubly linked list data structure.

class Node:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRU_Cache:
    miss=0
    def __init__(self,capacity):
        self.dic = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


    def get(self, key):

        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            LRU_Cache.miss+=1
            return n.value

        return -1

    def set(self, key, value):
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        LRU_Cache.miss+=1
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]


cache = LRU_Cache(2)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
cache.set(4,4)
cache.get(3)
print(cache.put)
# print(cache.get(1))
# print(cache.get(3))
# lrucache= LRU_Cache(50)
# reference_count = 0
# for i in range(50):
#     lrucache.set(i,i)
#     reference_count+=1

# for j in range(1,101,2):
#     print(lrucache.get(j))
#     reference_count+=1
# print("-------------------------------------------------------------------------------------------------------")
# def is_prime(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:

#         return True
#     else:
#         return False

# for k in range(101):
#     if is_prime(k):
#         reference_count+=1
#         lrucache.set(k,k)
# #
# # for l in range(50):
# #     print(lrucache.get(l))

# missrate=(lrucache.miss/reference_count)*100
# print("Miss rate: ",missrate,"%")
# print("Hit Rate: ",100-missrate)

