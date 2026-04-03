# ==============================
# VARUN'S FILE: calculations.py
# ==============================

def take_input():
    n = int(input("Enter number of processes: "))

    if n <= 0:
        print("Invalid number of processes")
        return []

    processes = []

    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter arrival time for {pid}: "))
        bt = int(input(f"Enter burst time for {pid}: "))

        processes.append({
            'id': pid,
            'arrival': at,
            'burst': bt
        })

    return processes


def calculate_times(processes, completion_time):
    result = []
    total_wt = 0
    total_tat = 0

    for p in processes:
        pid = p['id']
        at = p['arrival']
        bt = p['burst']
        ct = completion_time[pid]

        tat = ct - at
        wt = tat - bt

        total_wt += wt
        total_tat += tat

        result.append({
            'id': pid,
            'arrival': at,
            'burst': bt,
            'completion': ct,
            'tat': tat,
            'wt': wt
        })

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    return result, avg_wt, avg_tat


def display_table(results, avg_wt, avg_tat):
    print("\n==============================")
    print("PROCESS DETAILS")
    print("==============================")
    print("PID\tAT\tBT\tCT\tWT\tTAT")

    for r in results:
        print(f"{r['id']}\t{r['arrival']}\t{r['burst']}\t{r['completion']}\t{r['wt']}\t{r['tat']}")

    print("\n------------------------------")
    print(f"Average Waiting Time    : {round(avg_wt, 2)}")
    print(f"Average Turnaround Time : {round(avg_tat, 2)}")
    print("==============================")
