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

    # timeline
    for i in range(len(order) + 1):
        print(f"{i}\t", end="")
    print("\n")


def main():
    processes = take_input()

    if not processes:
        return

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            order, ct = fcfs(processes)

        elif choice == 2:
            order, ct = sjf(processes)

        elif choice == 3:
            tq = int(input("Enter Time Quantum: "))
            order, ct = round_robin(processes, tq)

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")
            continue

        # Calculate results
        results, avg_wt, avg_tat = calculate_times(processes, ct)

        # Display outputs
        draw_gantt_chart(order)
        display_table(results, avg_wt, avg_tat)


if __name__ == "__main__":
    main()