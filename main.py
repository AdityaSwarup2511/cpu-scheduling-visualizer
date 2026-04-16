# ==============================
# SHRISTI'S FILE: main.py
# ==============================

from algorithms import fcfs, sjf, round_robin, priority_np
from calculations import take_input, calculate_times, display_table


def display_menu():
    print("\n==============================")
    print("  CPU SCHEDULING VISUALIZER  ")
    print("==============================")
    print("1. FCFS")
    print("2. SJF (Non-Preemptive)")
    print("3. Round Robin")
    print("4. Priority (Non-Preemptive)")
    print("5. Compare All Algorithms")
    print("6. Exit")


def draw_gantt_chart(timeline, algorithm_name=""):
    """
    ✅ FIXED: Uses actual start/end times from timeline, not fake 0,1,2... indices
    """
    print(f"\nGANTT CHART ({algorithm_name}):")
    print("─" * 50)

    # Draw process blocks
    for slot in timeline:
        print(f"| {slot['pid']} ", end="")
    print("|")

    # ✅ Draw real timestamps
    for slot in timeline:
        print(f"{slot['start']:<4}", end="")
    # Print final end time
    if timeline:
        print(f"{timeline[-1]['end']}")
    print("─" * 50)


def compare_all_algorithms(processes):
    print("\n" + "=" * 60)
    print("COMPARING ALL SCHEDULING ALGORITHMS")
    print("=" * 60)

    algorithm_results = {}

    # ─── FCFS ───────────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("1. FIRST COME FIRST SERVED (FCFS)")
    print("-" * 60)
    order_fcfs, ct_fcfs, tl_fcfs = fcfs(processes)
    results_fcfs, avg_wt_fcfs, avg_tat_fcfs = calculate_times(processes, ct_fcfs)
    draw_gantt_chart(tl_fcfs, "FCFS")
    display_table(results_fcfs, avg_wt_fcfs, avg_tat_fcfs)
    algorithm_results['FCFS'] = {'avg_wt': avg_wt_fcfs, 'avg_tat': avg_tat_fcfs}

    # ─── SJF ────────────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("2. SHORTEST JOB FIRST (SJF)")
    print("-" * 60)
    order_sjf, ct_sjf, tl_sjf = sjf(processes)
    results_sjf, avg_wt_sjf, avg_tat_sjf = calculate_times(processes, ct_sjf)
    draw_gantt_chart(tl_sjf, "SJF")
    display_table(results_sjf, avg_wt_sjf, avg_tat_sjf)
    algorithm_results['SJF'] = {'avg_wt': avg_wt_sjf, 'avg_tat': avg_tat_sjf}

    # ─── Round Robin ────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("3. ROUND ROBIN (RR)")
    print("-" * 60)
    tq = int(input("Enter Time Quantum for Round Robin: "))
    order_rr, ct_rr, tl_rr = round_robin(processes, tq)
    results_rr, avg_wt_rr, avg_tat_rr = calculate_times(processes, ct_rr)
    draw_gantt_chart(tl_rr, f"ROUND ROBIN (TQ={tq})")
    display_table(results_rr, avg_wt_rr, avg_tat_rr)
    algorithm_results['ROUND ROBIN'] = {'avg_wt': avg_wt_rr, 'avg_tat': avg_tat_rr}

    # ─── Priority NP ────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("4. PRIORITY (NON-PREEMPTIVE)")
    print("-" * 60)
    order_pnp, ct_pnp, tl_pnp = priority_np(processes)
    results_pnp, avg_wt_pnp, avg_tat_pnp = calculate_times(processes, ct_pnp)
    draw_gantt_chart(tl_pnp, "PRIORITY NP")
    display_table(results_pnp, avg_wt_pnp, avg_tat_pnp)
    algorithm_results['PRIORITY'] = {'avg_wt': avg_wt_pnp, 'avg_tat': avg_tat_pnp}

    # ─── Summary ────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("COMPARISON SUMMARY")
    print("=" * 60)
    print("{:<20} {:<20} {:<20}".format("Algorithm", "Avg Waiting Time", "Avg Turnaround Time"))
    print("-" * 60)

    for algo, res in algorithm_results.items():
        print("{:<20} {:<20.2f} {:<20.2f}".format(algo, res['avg_wt'], res['avg_tat']))

    best_algo = min(algorithm_results.items(), key=lambda x: x[1]['avg_wt'])

    print("\n" + "=" * 60)
    print("🏆 BEST ALGORITHM (lowest Avg WT): {}".format(best_algo[0]))
    print("=" * 60)
    print(f"  Average Waiting Time    : {best_algo[1]['avg_wt']:.2f}")
    print(f"  Average Turnaround Time : {best_algo[1]['avg_tat']:.2f}")
    print("=" * 60)


def main():
    processes = take_input()

    if not processes:
        return

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, enter a number.")
            continue

        if choice == 1:
            print("\n" + "-" * 60)
            print("FIRST COME FIRST SERVED (FCFS)")
            print("-" * 60)
            order, ct, timeline = fcfs(processes)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(timeline, "FCFS")
            display_table(results, avg_wt, avg_tat)

        elif choice == 2:
            print("\n" + "-" * 60)
            print("SHORTEST JOB FIRST (SJF)")
            print("-" * 60)
            order, ct, timeline = sjf(processes)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(timeline, "SJF")
            display_table(results, avg_wt, avg_tat)

        elif choice == 3:
            print("\n" + "-" * 60)
            print("ROUND ROBIN (RR)")
            print("-" * 60)
            tq = int(input("Enter Time Quantum: "))
            order, ct, timeline = round_robin(processes, tq)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(timeline, f"ROUND ROBIN (TQ={tq})")
            display_table(results, avg_wt, avg_tat)

        elif choice == 4:
            print("\n" + "-" * 60)
            print("PRIORITY SCHEDULING (NON-PREEMPTIVE)")
            print("-" * 60)
            order, ct, timeline = priority_np(processes)
            results, avg_wt, avg_tat = calculate_times(processes, ct)
            draw_gantt_chart(timeline, "PRIORITY NP")
            display_table(results, avg_wt, avg_tat)

        elif choice == 5:
            compare_all_algorithms(processes)

        elif choice == 6:
            print("\nExiting program...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
