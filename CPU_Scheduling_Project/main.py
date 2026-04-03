# ==============================
# SHRISTI'S FILE: main.py
# ==============================

from algorithms import fcfs, sjf, round_robin
from calculations import take_input, calculate_times, display_table


def display_menu():
    print("\n==============================")
    print(" CPU SCHEDULING VISUALIZER ")
    print("==============================")
    print("1. FCFS")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Exit")


def draw_gantt_chart(order):
    print("\nGANTT CHART:")
    print("------------------------------")

    for p in order:
        print(f"| {p} ", end="")
    print("|")

    print("------------------------------")

    # simple timeline
    for i in range(len(order) + 1):
        print(f"{i}\t", end="")
    print("\n")


def compare_algorithms(processes):
    print("\n===== ALGORITHM COMPARISON =====")

    # FCFS
    order_fcfs, ct_fcfs = fcfs(processes)
    _, avg_wt_fcfs, _ = calculate_times(processes, ct_fcfs)

    # SJF
    order_sjf, ct_sjf = sjf(processes)
    _, avg_wt_sjf, _ = calculate_times(processes, ct_sjf)

    # Round Robin (fixed TQ = 2)
    order_rr, ct_rr = round_robin(processes, 2)
    _, avg_wt_rr, _ = calculate_times(processes, ct_rr)

    print(f"FCFS Avg WT: {round(avg_wt_fcfs, 2)}")
    print(f"SJF Avg WT: {round(avg_wt_sjf, 2)}")
    print(f"RR Avg WT: {round(avg_wt_rr, 2)}")

    best = min([
        ("FCFS", avg_wt_fcfs),
        ("SJF", avg_wt_sjf),
        ("RR", avg_wt_rr)
    ], key=lambda x: x[1])

    print(f"\nBest Algorithm: {best[0]}")
    print("================================")


def main():
    processes = take_input()

    if not processes:
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            order, ct = fcfs(processes)

        elif choice == '2':
            order, ct = sjf(processes)

        elif choice == '3':
            tq = int(input("Enter Time Quantum: "))
            order, ct = round_robin(processes, tq)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter 1–4.")
            continue

        results, avg_wt, avg_tat = calculate_times(processes, ct)

        draw_gantt_chart(order)
        display_table(results, avg_wt, avg_tat)

        compare_algorithms(processes)


if __name__ == "__main__":
    main()
