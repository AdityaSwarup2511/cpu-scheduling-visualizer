# ==============================
# ADITYA'S FILE: algorithms.py
# ==============================

def fcfs(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])

    current_time = 0
    completion_time = {}
    execution_order = []

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']

        current_time += process['burst']

        completion_time[process['id']] = current_time
        execution_order.append(process['id'])

    return execution_order, completion_time


def sjf(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['burst']))

    current_time = 0
    completion_time = {}
    execution_order = []
    completed = []

    while len(completed) < len(processes):
        available = [
            p for p in processes
            if p['arrival'] <= current_time and p['id'] not in completed
        ]

        if not available:
            current_time += 1
            continue

        shortest = min(available, key=lambda x: x['burst'])

        current_time += shortest['burst']
        completion_time[shortest['id']] = current_time
        execution_order.append(shortest['id'])
        completed.append(shortest['id'])

    return execution_order, completion_time


def round_robin(processes, tq):
    queue = []
    current_time = 0
    completion_time = {}
    execution_order = []

    remaining = {p['id']: p['burst'] for p in processes}
    arrived = []

    while len(completion_time) < len(processes):
        for p in processes:
            if p['arrival'] <= current_time and p['id'] not in arrived:
                queue.append(p)
                arrived.append(p['id'])

        if not queue:
            current_time += 1
            continue

        process = queue.pop(0)
        execution_order.append(process['id'])

        run_time = min(tq, remaining[process['id']])
        current_time += run_time
        remaining[process['id']] -= run_time

        for p in processes:
            if p['arrival'] <= current_time and p['id'] not in arrived:
                queue.append(p)
                arrived.append(p['id'])

        if remaining[process['id']] > 0:
            queue.append(process)
        else:
            completion_time[process['id']] = current_time

    return execution_order, completion_time



if __name__ == "__main__":
    processes = [
        {'id': 'P1', 'arrival': 0, 'burst': 5},
        {'id': 'P2', 'arrival': 1, 'burst': 3},
        {'id': 'P3', 'arrival': 2, 'burst': 8}
    ]

    order, ct = round_robin(processes, 2)
    print(order)
    print(ct)
