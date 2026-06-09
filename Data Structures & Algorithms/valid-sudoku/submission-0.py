class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print("checking rows")
        for row in board:
            dcount = 0
            rowset = set()
            for element in row:
                rowset.add(element)
                if element == ".": dcount += 1
            print(rowset)
            if dcount > 0:
                if (9 - len(rowset) - dcount + 1) > 0:
                    return False 
        
        print("checking cols")
        for c in range(len(board[0])):
            colset = set()
            dcount = 0
            for r in range(len(board)):
                colval = board[r][c]
                colset.add(colval)
                if colval == ".": dcount += 1
            if dcount > 0:
                if (9 - len(colset) - dcount + 1) > 0:
                    return False 

        print("checking squares")
        rows = len(board)
        cols = len(board[0])
        hashmap = {}
        for r in range(rows):
            for c in range(cols):
                element = board[r][c]
                boxId = (r // 3) * 3 + (c // 3)
                if boxId not in hashmap:
                    hashmap[boxId] = []
                hashmap[boxId].append(element)

        for key,value in hashmap.items():
            dotcount = value.count(".")
            if dotcount > 0:
                if 9 - dotcount - len(set(value)) + 1 > 0:
                    return False
        return True





