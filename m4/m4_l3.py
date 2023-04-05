graph  = {'1': set(['2', '5']),
          '2': set(['1', '3', '4']),
          '3': set(['2']),
          '4': set(['2']),
          '5': set(['1', '6', '7']),
          '6': set(['5']),
          '7': set(['5', '8', '9']),
          '8': set(['7']),
          '9': set(['7'])}

def bfs(graph, start, visited = [], queue = []):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            queue.append(v)
    while queue:
    	bfs(graph, queue.pop(0), visited, queue)
    return visited

print(bfs(graph, '1'))          




