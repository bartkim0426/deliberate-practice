import heapq
node = 5  # 노드의 개수
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start부터 거리값 저장
    distances[start] = 0   # 출발 값은 0
    queue = []
    # queue에 담기는 순서는 (거리, 노드) 형태
    heapq.heappush(queue, (distances[start], start))  # 시작 노드부터 탐색

    while queue:
        # 탐색할 노드, 거리
        current_distance, current_destination = heapq.heappop(queue)

        # 기존보다 거리가 더 길다면 보지 않음
        if distances[current_destination] < current_distance:
            continue

        # 해당 current_destination부터 갈 수 있는 거리를 모두 계산
        for new_destination, new_distance in graph[current_destination].items():
            # 해당 노드를 거쳐갈때의 거리
            distance = current_distance + new_distance
            if distance < distances[new_destination]:  # 기존의 거리보다 더 크면
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 거리를 계산하기 위해 큐에 삽입

    return distances
