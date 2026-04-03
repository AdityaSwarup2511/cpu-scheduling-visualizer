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
    print("4. Compare All Algorithms")
    print("5. Exit")


def draw_gantt_chart(order, algorithm_name=""):
    print(f"\nGANTT CHART ({algorithm_name}):")
    print("------------------------------")

    for p in order:
        print(f"| {p} ", end="")
    print("|")

    print("------------------------------")

    # timeline
    for i in range(len(order) + 1):
        print(f"{i}\t", end="")
    print("\n")


def compare_all_algorithms(processes):
    """
    Run all three algorithms and compare their performance
    """
    print("\n" + "="*60)
    print("COMPARING ALL SCHEDULING ALGORITHMS")
    print("="*60)

    # Store results for each algorithm
    algorithm_results = {}

    # ===== FCFS =====
    print("\n" + "-"*60)
    print("1. FIRST COME FIRST SERVED (FCFS)")
    print("-"*60)
    order_fcfs, ct_fcfs = fcfs(processes)
    results_fcfs, avg_wt_fcfs, avg_tat_fcfs = calculate_times(processes, ct_fcfs)
    draw_gantt_chart(order_fcfs, "FCFS")
    display_table(results_fcfs, avg_wt_fcfs, avg_tat_fcfs)
    
    algorithm_results['FCFS'] = {
        'avg_wt': avg_wt_fcfs,
        'avg_tat': avg_tat_fcfs,
        'order': order_fcfs,
        'completion_time': ct_fcfs
    }

    # ===== SJF =====
    print("\n" + "-"*60)
    print("2. SHORTEST JOB FIRST (SJF)")
    print("-"*60)
    order_sjf, ct_sjf = sjf(processes)
    results_sjf, avg_wt_sjf, avg_tat_sjf = calculate_times(processes, ct_sjf)
    draw_gantt_chart(order_sjf, "SJF")
    display_table(results_sjf, avg_wt_sjf, avg_tat_sjf)
    
    algorithm_results['SJF'] = {
        'avg_wt': avg_wt_sjf,
        'avg_tat': avg_tat_sjf,
        'order': order_sjf,
        'completion_time': ct_sjf
    }

    # ===== ROUND ROBIN =====
    print("\n" + "-"*60)
    print("3. ROUND ROBIN (RR)")
    print("-"*60)
    tq = int(input("Enter Time Quantum for Round Robin: "))
    order_rr, ct_rr = round_robin(processes, tq)
    results_rr, avg_wt_rr, avg_tat_rr = calculate_times(processes, ct_rr)
    draw_gantt_chart(order_rr, f"ROUND ROBIN (TQ={tq})")
    display_table(results_rr, avg_wt_rr, avg_tat_rr)
    
    algorithm_results['ROUND ROBIN'] = {
        'avg_wt': avg_wt_rr,
        'avg_tat': avg_tat_rr,
        'order': order_rr,
        'completion_time': ct_rr
    }

    # ===== COMPARISON =====
    print("\n" + "="*60)
    print("ALGORITHM COMPARISON SUMMARY")
    print("="*60)
    print("\n{:<20} {:<20} {:<20}".format("Algorithm", "Avg Waiting Time", "Avg Turnaround Time"))
    print("-"*60)
    
    for algo, results in algorithm_results.items():
        print("{:<20} {:<20.2f} {:<20.2f}".format(
            algo,
            results['avg_wt'],
            results['avg_tat']
        ))

    # Find best algorithm based on minimum average waiting time
    best_algo = min(algorithm_results.items(), key=lambda x: x[1]['avg_wt'])
    
    print("\n" + "="*60)
    print("🏆 BEST ALGORITHM: {} 🏆".format(best_algo[0]))
    print("="*60)
    print(f"Average Waiting Time: {best_algo[1]['avg_wt']:.2f}")
    print(f"Average Turnaround Time: {best_algo[1]['avg_tat']:.2f}")
    print("="*60)


def main():
    processes = take_input()

    if not processes:
        return

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n" + "-"*60)
            print("FIRST COME FIRST SERVED (FCFS)")
            print("-"*60)
            order, ct = fcfs(processes)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(order, "FCFS")
            display_table(results, avg_wt, avg_tat)

        elif choice == 2:
            print("\n" + "-"*60)
            print("SHORTEST JOB FIRST (SJF)")
            print("-"*60)
            order, ct = sjf(processes)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(order, "SJF")
            display_table(results, avg_wt, avg_tat)

        elif choice == 3:
            print("\n" + "-"*60)
            print("ROUND ROBIN (RR)")
            print("-"*60)
            tq = int(input("Enter Time Quantum: "))
            order, ct = round_robin(processes, tq)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(order, f"ROUND ROBIN (TQ={tq})")
            display_table(results, avg_wt, avg_tat)

        elif choice == 4:
            compare_all_algorithms(processes)

        elif choice == 5:
            print("\nExiting program...")
            break

        else:
            print("Invalid choice")
            continue


if __name__ == "__main__":
    main()
