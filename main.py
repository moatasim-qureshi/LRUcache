class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LRUCache:
    num_of_ref = 0
    miss = 0

    def __init__(self, capacity: int ):
        self.capacity = capacity
        self.front = None
        self.rear = None

    def file_write(self):
        with open("cache.txt","w") as file:
                temp = self.front
                while temp is not None:
                    file.write(f"({temp.key},{temp.value})\n")   
                    temp = temp.next  
            
    def put(self, key : int,value :int):
        LRUCache.num_of_ref += 1  
        new = Node( key, value)
        if self.front == None:
            self.front = new
            self.rear = new
            LRUCache.miss += 1
            self.file_write()
            return self
        
        a = self.front
        b = a.next

        if a.key == key:
            self.rear.next = new
            self.rear = new
            self.front = self.front.next
            a.next = None
            self.file_write()            
            return

        while b is not None and b.key != key:
            a = a.next
            b = b.next
       
        if b is None:
            self.rear.next = new
            self.rear = new
            LRUCache.miss += 1
            if self.len_cache() > self.capacity:
                self.front = self.front.next
            self.file_write()  
        
        elif b.next is None:
            a.next = new
            self.rear = new
            self.file_write()   

        elif b.key == key:
            a.next = b.next
            self.rear.next = new
            self.rear = new
            self.file_write()   
                
        return 
    
    def get(self, key):
        LRUCache.num_of_ref += 1
        a = self.front
        b = a.next
        
        if self.front.key == key:
            b = self.front
            self.front = self.front.next
            a.next = None
            self.rear.next = a
            self.rear = a
            self.file_write()   

            return b.value

        while b is not None and b.key != key:
            a = a.next
            b = b.next

        if b is None:
            LRUCache.miss += 1
            return -1
        
        else:
            self.rear.next = b
            self.rear = b
            a.next = b.next
            b.next = None
            self.file_write()
            return b.value
        
    def len_cache(self):
        a = self.front
        count = 0
        while a != None:
            count += 1
            a = a.next
        return count
    
    def print_cache(self):
        a = self.front
        print(f"FRONT --> ",end = "")
        while a.next is not None:
            print(f"({a.key},{a.value}) -- ",end = "")
            a = a.next
        print(f"({a.key},{a.value}) <-- REAR")



cache = LRUCache(50)
# for i in range(50):
#     cache.put(i, i)

# for i in range(1,101,2):
#     cache.get(i)

# for i in range(101):
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#             cache.put(i,i)

# # cache.print_cache()
# print(cache.len_cache())
# miss_rate = (cache.miss/cache.num_of_ref)
# print("Miss Rate: ", miss_rate * 100:.2f, "%")
# print("Hit Rate: ", 100-(miss_rate * 100:.2f), "%")


#-------------------------------------------------------------------------------------------

print("                          WELCOME TO LRU CACHE                 \n\n")
size = int(input("ENTER THE CAPACITY FOR LRUCACHE: "))
cache = LRUCache(size)
print()

while True:
    print("Options:\n")
    print("  1. Put key Value")
    print("  2. Get Value")
    print("  3. Print Cache")
    print("  4. Miss Rate and Hit Rate")
    print("  5. Exit\n")

    choice = input("Enter choice:")
    print()

    if choice == "1":
        key = int(input("  Enter key: "))
        value = int(input("  Enter value: "))
        cache.put(key, value)
        print("\nVALUE ADDED TO THE CACHE.")

    elif choice == "2":
        key = int(input(" Enter key to get value: "))
        value = cache.get(key)
        if value != -1:
            print(f"VALUE: {value}")
        else:
            print("KEY NOT FOUND")

    elif choice == "3":
        cache.print_cache()

    elif choice == "4":
        miss_rate = cache.miss/cache.num_of_ref
        print(f"Miss Rate: {miss_rate * 100:.2f}%")

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please enter a valid option.\n")











        
# print("                          WELCOME TO LRU CACHE                 \n\n")
# size = int(input("ENTER THE CAPACITY FOR LRUCACHE: "))
# cache = LRUCache(size)
# print()
# print("PRESS [0] TO EXIT\n")
# while True:
#     choice = int(input("WHAT DO YOU WANT TO WITH CACHE : \n\n 1) PUT VALUE\n 2) GET VALUE\n 3) HIT RATE AND MISS RATE\n 0) EXIT\n\n ENTER CHOICE:"))
    
#     if choice == 1:
        
