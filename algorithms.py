# ==============================
# ADITYA'S FILE: algorithms.py
# ==============================

def fcfs(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])

    current_time = 0
    completion_time = {}
    execution_order = []
    timeline = []  # ✅ Track actual Gantt timeline

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']

        start = current_time
        current_time += process['burst']

        completion_time[process['id']] = current_time
        execution_order.append(process['id'])
        timeline.append({'pid': process['id'], 'start': start, 'end': current_time, 'duration': process['burst']})

    return execution_order, completion_time, timeline


def sjf(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['burst']))

    current_time = 0
    completion_time = {}
    execution_order = []
    completed = []
    timeline = []  # ✅ Track actual Gantt timeline

    while len(completed) < len(processes):
        available = [
            p for p in processes
            if p['arrival'] <= current_time and p['id'] not in completed
        ]

        if not available:
            current_time += 1
            continue

        shortest = min(available, key=lambda x: x['burst'])

        start = current_time
        current_time += shortest['burst']
        completion_time[shortest['id']] = current_time
        execution_order.append(shortest['id'])
        completed.append(shortest['id'])
        timeline.append({'pid': shortest['id'], 'start': start, 'end': current_time, 'duration': shortest['burst']})

    return execution_order, completion_time, timeline


def round_robin(processes, tq):
    queue = []
    current_time = 0
    completion_time = {}
    execution_order = []
    timeline = []  # ✅ Track actual Gantt timeline (per quantum slot)

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
        start = current_time           # ✅ Capture start before advancing time
        current_time += run_time
        remaining[process['id']] -= run_time

        timeline.append({'pid': process['id'], 'start': start, 'end': current_time, 'duration': run_time})

        for p in processes:
            if p['arrival'] <= current_time and p['id'] not in arrived:
                queue.append(p)
                arrived.append(p['id'])

        if remaining[process['id']] > 0:
            queue.append(process)
        else:
            completion_time[process['id']] = current_time

    return execution_order, completion_time, timeline


def priority_np(processes):
    """
    Non-Preemptive Priority Scheduling.
    Lower priority number = Higher priority (e.g., priority 1 runs before priority 3).
    """
    processes_copy = sorted(processes, key=lambda x: x['arrival'])

    current_time = 0
    completion_time = {}
    execution_order = []
    completed = []
    timeline = []

    while len(completed) < len(processes_copy):
        available = [
            p for p in processes_copy
            if p['arrival'] <= current_time and p['id'] not in completed
        ]

        if not available:
            current_time += 1
            continue

        # ✅ Pick process with highest priority (lowest number), tie-break by arrival
        highest = min(available, key=lambda x: (x['priority'], x['arrival']))

        start = current_time
        current_time += highest['burst']
        completion_time[highest['id']] = current_time
        execution_order.append(highest['id'])
        completed.append(highest['id'])
        timeline.append({'pid': highest['id'], 'start': start, 'end': current_time, 'duration': highest['burst']})

    return execution_order, completion_time, timeline


if __name__ == "__main__":
    processes = [
        {'id': 'P1', 'arrival': 0, 'burst': 5, 'priority': 2},
        {'id': 'P2', 'arrival': 1, 'burst': 3, 'priority': 1},
        {'id': 'P3', 'arrival': 2, 'burst': 8, 'priority': 3}
    ]

    print("=== Round Robin ===")
    order, ct, tl = round_robin(processes, 2)
    print("Order:", order)
    print("Completion:", ct)
    print("Timeline:", tl)

    print("\n=== Priority (Non-Preemptive) ===")
    order, ct, tl = priority_np(processes)
    print("Order:", order)
    print("Completion:", ct)
    print("Timeline:", tl)
