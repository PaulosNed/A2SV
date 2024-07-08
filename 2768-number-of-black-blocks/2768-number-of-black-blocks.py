from typing import  *
from  collections import *


class Solution:
	def countBlackBlocks(self, n: int, m: int, coordinates: List[List[int]]) -> List[int]:
		st=set([(x,y) for x,y in coordinates])
		tot=(n-1)*(m-1)
		deg=defaultdict(int)
		for x,y in st:
			# deg[(x,y)]+=1
			for dx,dy in [(-1,-1),(1,1),(-1,1),(1,-1)]:
				a,b=x+dx,y+dy
				mp=(abs(a+x)//2,abs(b+y)//2)
				if a>=0 and b>=0 and a<n and b<m:
					deg[mp]+=1
		ans=[0]*5
		# print(deg)
		for i in deg:
			ans[deg[i]]+=1
		ans[0]=tot-sum(ans)
		return ans
