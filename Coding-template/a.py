import sys
import os
import ast
from typing import List
from collections import defaultdict, deque
import heapq

def use_files(input_file, output_file):
    if os.path.exists(input_file):
        sys.stdin = open(input_file, 'r')
    if output_file:
        sys.stdout = open(output_file, 'w')

def get_line():
    return sys.stdin.readline().strip()

def get_nested_list():
    return ast.literal_eval(get_line())

def get_int():
    return int(sys.stdin.readline())


def solve(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        def dijkstra(graph, dst, start, k):
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            stopage = {node: 0 for node in graph}

            priority_queue = [(0, start)]  # (distance, node)

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)

                # Skip nodes already processed with a shorter distance
                if current_distance > distances[current_node]:
                    continue

                for neighbor, weight in graph[current_node].items():
                    distance = current_distance + weight
                    stop = stopage[current_node] +1

                    if distance < distances[neighbor] and ((neighbor == dst and stop <= k+1) or (stop<=k)):
                        distances[neighbor] = distance
                        stopage[neighbor] = stop
                        heapq.heappush(priority_queue, (distance, neighbor))

            return distances
        
        graph = {node: {} for node in range(n)}

        for sc, ds, weight in flights:
            if sc not in graph:
                graph[sc] = {}
            graph[sc][ds] = weight

        distance = dijkstra(graph, dst,src, k)
        if distance[dst] == float('inf'):
            return -1
        return distance[dst]


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    use_files(input_file, output_file)
    n = get_int()
    edges = get_nested_list() 
    src = get_int()
    dst = get_int()
    k = get_int()
    result = solve(n,edges, src, dst, k) 

    print(result)
   
