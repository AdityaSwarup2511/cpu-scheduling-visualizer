
from flask import Flask, render_template, request
from algorithms import fcfs, sjf, round_robin, priority_np
from calculations import calculate_times

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            n = int(request.form.get("n", 0))
            algo = request.form.get("algorithm")

            processes = []

            for i in range(n):
                at = request.form.get(f"at{i}")
                bt = request.form.get(f"bt{i}")
                pr = request.form.get(f"pr{i}", 0)  # ✅ Priority input (default 0)

                if not at or not bt:
                    continue

                processes.append({
                    "id": f"P{i+1}",
                    "arrival": int(at),
                    "burst": int(bt),
                    "priority": int(pr) if pr else 0
                })

            if not processes:
                return render_template("index.html", result=None)

            # ─────────────────────────────────────────
            # 🔥 COMPARE MODE
            # ─────────────────────────────────────────
            if algo == "COMPARE":
                comparison = {}

                # FCFS
                _, ct_fcfs, _ = fcfs(processes)
                _, avg_wt_fcfs, avg_tat_fcfs = calculate_times(processes, ct_fcfs)
                comparison["FCFS"] = {"wt": round(avg_wt_fcfs, 2), "tat": round(avg_tat_fcfs, 2)}

                # SJF
                _, ct_sjf, _ = sjf(processes)
                _, avg_wt_sjf, avg_tat_sjf = calculate_times(processes, ct_sjf)
                comparison["SJF"] = {"wt": round(avg_wt_sjf, 2), "tat": round(avg_tat_sjf, 2)}

                # Round Robin
                tq = int(request.form.get("tq", 1))
                _, ct_rr, _ = round_robin(processes, tq)
                _, avg_wt_rr, avg_tat_rr = calculate_times(processes, ct_rr)
                comparison["RR"] = {"wt": round(avg_wt_rr, 2), "tat": round(avg_tat_rr, 2)}

                # Priority NP
                _, ct_pnp, _ = priority_np(processes)
                _, avg_wt_pnp, avg_tat_pnp = calculate_times(processes, ct_pnp)
                comparison["Priority"] = {"wt": round(avg_wt_pnp, 2), "tat": round(avg_tat_pnp, 2)}

                # ✅ FIX: Calculate best algorithm in Python (not broken Jinja dictsort)
                best_algo = min(comparison, key=lambda k: comparison[k]['wt'])

                result = {"comparison": comparison, "best_algo": best_algo}
                return render_template("index.html", result=result)

            # ─────────────────────────────────────────
            # 🔥 NORMAL MODE
            # ─────────────────────────────────────────
            if algo == "FCFS":
                order, ct, timeline = fcfs(processes)

            elif algo == "SJF":
                order, ct, timeline = sjf(processes)

            elif algo == "RR":
                tq = int(request.form.get("tq", 1))
                order, ct, timeline = round_robin(processes, tq)

            elif algo == "PRIORITY":
                order, ct, timeline = priority_np(processes)

            else:
                order, ct, timeline = [], {}, []

            results, avg_wt, avg_tat = calculate_times(processes, ct)

            result = {
                "order": order,
                "timeline": timeline,   # ✅ Now uses accurate per-slot timeline
                "results": results,
                "avg_wt": round(avg_wt, 2),
                "avg_tat": round(avg_tat, 2)
            }

        except Exception as e:
            print("ERROR:", e)
            import traceback
            traceback.print_exc()

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)