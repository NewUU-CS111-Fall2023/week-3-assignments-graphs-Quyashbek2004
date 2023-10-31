import heapq

def dijkstra(adj_list, n):
    distance = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    distance[1] = 0
    pq = [(0, 1)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > distance[node]:
            continue

        for neighbor, road_length in adj_list[node]:
            new_dist = dist + road_length

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return distance, parent

def find_shortest_path(adj_list, forbidden_triplets, n):
    distance, parent = dijkstra(adj_list, n)

    if distance[n] == float('inf'):
        return -1

    path = [n]
    current = n

    while parent[current] != -1:
        path.append(parent[current])
        current = parent[current]

    path.reverse()
    return distance[n], path


n, m, k = map(int, input().split())

adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    xi, yi = map(int, input().split())
    adj_list[xi].append((yi, 1))
    adj_list[yi].append((xi, 1))

forbidden_triplets = []

for _ in range(k):
    ai, bi, ci = map(int, input().split())
    forbidden_triplets.append((ai, bi, ci))


shortest_path = find_shortest_path(adj_list, forbidden_triplets, n)

if shortest_path == -1:
    print(-1)
else:
    d, path = shortest_path
    print(d)
    print(*path)
