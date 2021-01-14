import sys
import collections

read = lambda x: list(map(x, sys.stdin.readline().split()))

def main():
    cases = read(int)[0]
    for _ in range(cases):
        n,m = read(int)
        stage_location = {}
        items_count = collections.defaultdict(int)
        for stage, location in enumerate(read(int), start=1):
            stage_location[stage] = location
            items_count[location] += 1
            
        graph = { x:[] for x in range(1,n+1) }
        in_degrees = { x:0 for x in range(1,n+1) }
        for _ in range(m):
            s,d = read(int)
            graph[s].append(d)
            in_degrees[d] += 1

        moves = 0
        one_queue = collections.deque([])
        two_queue = collections.deque([])

        get_queue = lambda x: one_queue if x == 1 else two_queue
        switch_location = lambda x: 2 if x == 1 else 1
        add_to_queue = lambda x: get_queue(stage_location[x]).append(x)

        for s,d in in_degrees.items():
            if d == 0:
                add_to_queue(s)
        current_location = 1
        if two_queue and items_count[2] > items_count[1]:
            current_location = 2

        while one_queue or two_queue:
            queue = get_queue(current_location)
            if not queue:
                current_location = switch_location(current_location)
                queue = get_queue(current_location)
                moves += 1
            
            stage = queue.popleft()
            for nei in graph[stage]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    add_to_queue(nei)
        
        print(moves)

if __name__ == "__main__":
    main()