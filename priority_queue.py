import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

pq = PriorityQueue()

pq.push('foo', 1)
pq.push('bar', 1)
pq.push('baz', 2)
pq.push('wibble', 5)
pq.push('wobble', 4)
pq.push('woo', 0)

print pq

print 'pq.pop(): ',pq.pop()
print 'pq.pop(): ',pq.pop()
print 'pq.pop(): ',pq.pop()
print 'pq.pop(): ',pq.pop()
print 'pq.pop(): ',pq.pop()
print 'pq.pop(): ',pq.pop()
#print 'pq.pop(): ',pq.pop() # IndexError: index out of range
