class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        waitingQueue = deque()
        pq = [(-value,key) for key, value in taskCounter.items()]
        heapq.heapify(pq)
        currentTurn = 0
        while pq or waitingQueue:
            if not pq:
                expectedTurn, count, task = waitingQueue.popleft()
                currentTurn = max(currentTurn + 1, expectedTurn)
            else:
                if waitingQueue:

                    expectedTurn, count, task = waitingQueue[0]
                    if (expectedTurn == (currentTurn + 1)):
                        waitingQueue.popleft()
                        heapq.heappush(pq, (-count, task))
                currentTurn += 1
                count, task = heapq.heappop(pq)
                count = -count

            if count != 1:
                count -= 1
                waitingQueue.append((currentTurn + n + 1, count, task))
        return currentTurn
            





        return 0

        