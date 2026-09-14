class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for element in operations:
            if element == 'C':
                record.pop()
            elif element == 'D':
                num = record[-1]
                record.append(num*2)
            elif element == '+':
                addednum = record[-2] + record[-1]
                record.append(addednum)
            else: 
                record.append(int(element))
        
        return sum(record)