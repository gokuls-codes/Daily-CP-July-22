class Solution:
	def FirstNonRepeating(self, A):
		# Code here
        ans = ""
        from collections import defaultdict
        from queue import Queue
        
        counter = defaultdict(int)
        q = Queue()
        for character in A:
            q.put(character)
            counter[character] += 1
            
            while not q.empty():
                if counter[q.queue[0]] > 1:
                    q.get()
                else:
                    ans += q.queue[0]
                    break
                    
            if q.empty():
                ans += "#"
                
        return ans