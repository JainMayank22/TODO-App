# Hierholzer's Algorithm for directed graph
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        from collections import defaultdict
        self.flightmap = defaultdict(list)
        
        for ticket in tickets:
            origin,dest = ticket[0], ticket[1]
            self.flightmap[origin].append(dest)
        for origin,ite in self.flightmap.items():
            ite.sort(reverse = True)
            
        self.result = []
        self.DFS("JFK")
        return self.result[::-1]
        
    def DFS(self,origin):
        destlist = self.flightmap[origin]
        while destlist:
            nextdest = destlist.pop()
            self.DFS(nextdest)
        self.result.append(origin)