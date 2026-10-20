# VoltForge — Battery Simulation Workspace

VoltForge is a research-oriented workspace for exploring electrochemical battery models, numerical simulation, and results visualization with [PyBaMM](https://github.com/pybamm-team/PyBaMM).

> **Project note:** VoltForge is a rebranded workspace built around the existing PyBaMM scientific-computing ecosystem. The underlying Python package remains named `pybamm`; this repository does not claim ownership of the upstream project.

## What it offers

- Run battery simulations with PyBaMM's electrochemical models.
- Start with a small lithium-ion Single Particle Model (SPM) quickstart.
- Export voltage data and a visualization for inspection.
- Keep a research-friendly path for extending experiments and comparing results.

## Quick start

Python 3.10+ is recommended. Install the published PyBaMM package and the plotting dependency:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install pybamm matplotlib
```

Once the project files are present, run:

```bash
python voltforge_quickstart.py
```

The quickstart is intended to save simulation outputs locally. Consult the script's help/options and the installed PyBaMM version if your local environment differs.

## Repository status

This repository is being initialized as a separate project. The GitHub repository may initially contain only this README while the complete project ZIP is uploaded locally.

The provided source archive did not include the original Git submodule pins for SUNDIALS and SuiteSparse. Therefore, a full native source build is not claimed to be verified here. Using the published PyBaMM package avoids requiring that native source checkout for the quickstart.

## Scientific and upstream attribution

VoltForge builds on the PyBaMM ecosystem. Please consult the upstream project's license, citation guidance, and documentation before redistributing upstream code or scientific results:

- [PyBaMM source repository](https://github.com/pybamm-team/PyBaMM)
- [PyBaMM documentation](https://docs.pybamm.org/)
- [PyBaMM citation information](https://github.com/pybamm-team/PyBaMM#citing-pybamm)

This project name and presentation do not change the licenses or attribution obligations of any upstream components included with a full source distribution.

## Disclaimer

Simulation results depend on the selected model, parameters, solver, and assumptions. Do not use outputs as a substitute for battery safety validation or qualified engineering review.
