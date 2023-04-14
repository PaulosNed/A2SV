"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        curr = 0
        all_emps = {}
        
        def traverse(root):
            nonlocal curr
            if not root:
                return
            
            curr += root.importance
            
            for child in root.subordinates:
                traverse(all_emps[child])
        
        for employee in employees:
            all_emps[employee.id] = employee
        
        traverse(all_emps[id])
        return curr
        
    