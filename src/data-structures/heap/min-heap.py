
class MinHeap: 
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def _get_index_of_children(self, i: int) -> (int):
        return 2 * i + 1, 2 * i + 2

    def _get_index_of_parent(self, i: int) -> int:
        return (i - 1) // 2
        
    def insert(self, val: int) -> bool:
        self.heap_list.append(val)
        self.size += 1

        index_of_new_val = self.size - 1
        
        while index_of_new_val > 0:
            index_of_parent = self._get_index_of_parent(index_of_new_val)
            if self.heap_list[index_of_parent] > self.heap_list[index_of_new_val]:
                self.heap_list[index_of_new_val], self.heap_list[index_of_parent] = \
                    self.heap_list[index_of_parent], self.heap_list[index_of_new_val]
                index_of_new_val = index_of_parent
            else:
                break

        return True
    
    def pop_min(self) -> int | bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.size = 0
            return self.heap_list.pop()

        result = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self.size -= 1
        
        i = 0
        size = self.size
        while True:
            left, right = self._get_index_of_children(i)
            smallest = i
            
            if left < size and self.heap_list[left] < self.heap_list[smallest]:
                smallest = left
                
            if right < size and self.heap_list[right] < self.heap_list[smallest]:
                smallest = right
                
            if smallest != i:
                self.heap_list[i], self.heap_list[smallest] = self.heap_list[smallest], self.heap_list[i]
                i = smallest
            else:
                break

        return result
    
    def peek(self) -> int:
        return self.heap_list[0]
    
    def get_size(self) -> int:
        return self.size
