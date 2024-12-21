#########
#  DFS
#########

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(r, c, grid, ROWS, COLS):
    grid[r][c] = '#'
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '.':
            dfs(nr, nc, grid, ROWS, COLS)
##### BFS ###

from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(r, c, grid, ROWS, COLS):
    queue = deque([(r, c)])
    grid[r][c] = '#'
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in dir:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '.':
                grid[nr][nc] = '#'
                queue.append((nr, nc))


### roms ###

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs_iterative(r, c):
    stack = [(r, c)]
    while stack:
        cr, cc = stack.pop()
        if grid[cr][cc] == '.':
            grid[cr][cc] = '#'
            for dr, dc in dir:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '.':
                    stack.append((nr, nc))

ROWS, COLS = map(int, input().split())
grid = [list(input()) for _ in range(ROWS)]

rooms = 0

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '.':
            dfs_iterative(r, c)
            rooms += 1

print(rooms)



######area of islands#########

ROWS, COLS = len(grid), len(grid[0])
visit = set()

def dfs(r, c):
    if (r < 0 or r == ROWS or c < 0 or
        c == COLS or grid[r][c] == 0 or
        (r, c) in visit
    ):
        return 0
    visit.add((r, c))
    return (1 + dfs(r + 1, c) + 
                dfs(r - 1, c) + 
                dfs(r, c + 1) + 
                dfs(r, c - 1))

area = 0
for r in range(ROWS):
    for c in range(COLS):
        area = max(area, dfs(r, c))
return area

######island and treasure####

ROWS, COLS = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = 2147483647
visit = [[False for _ in range(COLS)] for _ in range(ROWS)]

def dfs(r, c):
    if (r < 0 or c < 0 or r >= ROWS or
        c >= COLS or grid[r][c] == -1 or
        visit[r][c]):
        return INF
    if grid[r][c] == 0:
        return 0

    visit[r][c] = True
    res = INF
    for dx, dy in directions:
        res = min(res, 1 + dfs(r + dx, c + dy))
    visit[r][c] = False
    return res

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == INF:
            grid[r][c] = dfs(r, c)

#####orangerotting##

q = collections.deque()
fresh = 0
time = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            fresh += 1
        if grid[r][c] == 2:
            q.append((r, c))

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while fresh > 0 and q:
    length = len(q)
    for i in range(length):
        r, c = q.popleft()

        for dr, dc in directions:
            row, col = r + dr, c + dc
            if (row in range(len(grid))
                and col in range(len(grid[0]))
                and grid[row][col] == 1
            ):
                grid[row][col] = 2
                q.append((row, col))
                fresh -= 1
    time += 1
return time if fresh == 0 else -1


###pacific

ROWS, COLS = len(heights), len(heights[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

pacific = atlantic = False

def dfs(r, c, prevVal):
    nonlocal pacific, atlantic
    if r < 0 or c < 0:
        pacific = True
        return
    if r >= ROWS or c >= COLS:
        atlantic = True
        return
    if heights[r][c] > prevVal:
        return

    tmp = heights[r][c]
    heights[r][c] = float('inf')
    for dx, dy in directions:
        dfs(r + dx, c + dy, tmp)
        if pacific and atlantic:
            break
    heights[r][c] = tmp

res = []
for r in range(ROWS):
    for c in range(COLS):
        pacific = False
        atlantic = False
        dfs(r, c, float('inf'))
        if pacific and atlantic:
            res.append([r, c])
return res

##surround

ROWS, COLS = len(board), len(board[0])

def capture(r, c):
    if (r < 0 or c < 0 or r == ROWS or 
        c == COLS or board[r][c] != "O"
    ):
        return
    board[r][c] = "T"
    capture(r + 1, c)
    capture(r - 1, c)
    capture(r, c + 1)
    capture(r, c - 1)

for r in range(ROWS):
    if board[r][0] == "O":
        capture(r, 0)
    if board[r][COLS - 1] == "O":
        capture(r, COLS - 1)

for c in range(COLS):
    if board[0][c] == "O":
        capture(0, c)
    if board[ROWS - 1][c] == "O":
        capture(ROWS - 1, c)

for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "O":
            board[r][c] = "X"
        elif board[r][c] == "T":
            board[r][c] = "O"

###curso

# Map each course to its prerequisites
preMap = {i: [] for i in range(numCourses)}
for crs, pre in prerequisites:
    preMap[crs].append(pre)

# Store all courses along the current DFS path
visiting = set()

def dfs(crs):
    if crs in visiting:
        # Cycle detected
        return False
    if preMap[crs] == []:
        return True

    visiting.add(crs)
    for pre in preMap[crs]:
        if not dfs(pre):
            return False
    visiting.remove(crs)
    preMap[crs] = []
    return True

for c in range(numCourses):
    if not dfs(c):
        return False
return True

###arvore true

if len(edges) > (n - 1):
    return False

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

visit = set()
def dfs(node, par):
    if node in visit:
        return False
    
    visit.add(node)
    for nei in adj[node]:
        if nei == par:
            continue
        if not dfs(nei, node):
            return False
    return True

return dfs(0, -1) and len(visit) == n

