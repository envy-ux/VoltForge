"""Run a small lithium-ion discharge study with the VoltForge workspace.

Uses PyBaMM's built-in Single Particle Model (SPM) and default parameters.
This example is a reproducible software demonstration, not a validated
prediction for a specific commercial cell.

Example:
    python examples/scripts/voltforge_quickstart.py --hours 1 --samples 100
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
import pybamm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simulate lithium-ion cell voltage with a simple SPM model."
    )
    parser.add_argument("--hours", type=float, default=1.0,
                        help="Simulation duration in hours (default: 1.0).")
    parser.add_argument("--samples", type=int, default=100,
                        help="Number of time points (default: 100; minimum: 2).")
    parser.add_argument("--output-dir", type=Path,
                        default=Path("outputs/voltforge_quickstart"),
                        help="Directory for CSV and plot outputs.")
    parser.add_argument("--no-plot", action="store_true",
                        help="Only export CSV; do not require Matplotlib.")
    parser.add_argument("--show", action="store_true",
                        help="Open the plot window after saving the plot.")
    args = parser.parse_args()
    if args.hours <= 0:
        parser.error("--hours must be greater than zero")
    if args.samples < 2:
        parser.error("--samples must be at least 2")
    if args.show and args.no_plot:
        parser.error("--show cannot be used together with --no-plot")
    return args


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    t_eval = np.linspace(0.0, args.hours * 3600.0, args.samples)
    simulation = pybamm.Simulation(pybamm.lithium_ion.SPM())
    solution = simulation.solve(t_eval=t_eval)

    time_s = np.asarray(solution.t, dtype=float).reshape(-1)
    voltage_v = np.asarray(solution["Voltage [V]"].entries, dtype=float).reshape(-1)
    csv_path = args.output_dir / "discharge_voltage.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["time_s", "time_min", "voltage_v"])
        writer.writerows(
            (f"{t:.8g}", f"{t / 60.0:.8g}", f"{v:.8g}")
            for t, v in zip(time_s, voltage_v, strict=True)
        )

    print("VoltForge quickstart completed")
    print("Model: lithium-ion Single Particle Model (SPM)")
    print(f"Simulated duration: {time_s[-1] / 3600.0:.3f} h")
    print(f"Initial voltage: {voltage_v[0]:.3f} V")
    print(f"Final voltage: {voltage_v[-1]:.3f} V")
    print(f"CSV written to: {csv_path.resolve()}")

    if not args.no_plot:
        try:
            import matplotlib
            if not args.show:
                matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise SystemExit(
                "Plotting requires Matplotlib. Install it with "
                "`python -m pip install matplotlib` or rerun with --no-plot."
            ) from exc
        fig, ax = plt.subplots(figsize=(8.5, 4.8), constrained_layout=True)
        ax.plot(time_s / 60.0, voltage_v, linewidth=2.2, color="#087E8B")
        ax.set_title("VoltForge · Simulated discharge voltage")
        ax.set_xlabel("Time (min)")
        ax.set_ylabel("Terminal voltage (V)")
        ax.grid(True, alpha=0.25)
        plot_path = args.output_dir / "discharge_voltage.png"
        fig.savefig(plot_path, dpi=160)
        print(f"Plot written to: {plot_path.resolve()}")
        if args.show:
            plt.show()
        plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
