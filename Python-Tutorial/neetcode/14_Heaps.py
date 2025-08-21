import heapq

# under the hoods are arrays
# by default min heaps
minHeap =[]
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)

print(minHeap[0]) # Min is always at index 0

while len(minHeap):
    print(heapq.heappop(minHeap)) # prints smallest to largest
print()

# does not have defult max heaps
# use min heap and multiply by -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap,-3) # actually inserting 3
heapq.heappush(maxHeap,-2) # actually inserting 2
heapq.heappush(maxHeap,-4) # actually inserting 4

print(-1 * maxHeap[0]) # Max always at index 0

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap)) # prints largest to smallest
print()

# Build heap from initial values
arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))