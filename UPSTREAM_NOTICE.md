# Upstream attribution and scope

VoltForge is a repository-level rebrand of a source archive of [PyBaMM (Python Battery Mathematical Modelling)](https://github.com/pybamm-team/PyBaMM). The battery models, expression-tree framework, solver bindings, package metadata, test suites, examples, and much of the documentation originate from that project and its contributors.

This rebrand adds or updates the VoltForge repository identity, high-level README and diagrams, a runnable quickstart example, and a lightweight smoke-test workflow. It does **not** claim authorship of the underlying PyBaMM framework, does not rename the importable `pybamm` package, and does not imply affiliation with or endorsement by the PyBaMM team.

## Notices retained

- The root [`LICENSE.txt`](LICENSE.txt) and component-level license files remain in the full source distribution.
- Upstream copyright headers, metadata, and citation files must be retained.
- The original workflow definitions from the complete source bundle are archived under [`.github/upstream-workflows/`](.github/upstream-workflows/) and are not active workflows in this rebranded repository.
- The main scientific citation is Sulzer et al. (2021), DOI: <https://doi.org/10.5334/jors.309>. Additional references may apply depending on the models and parameter sets used.

## Scope of the added example

`examples/scripts/voltforge_quickstart.py` is an onboarding example built on the existing `pybamm` public API. It simulates a lithium-ion Single Particle Model (SPM) with a default parameter set and exports voltage data. It is a demonstration of software usage, not experimental validation, a safety assessment, or a prediction for a specified commercial cell.

Before redistributing or publishing derived work, review the retained licenses, citation requirements, upstream trademarks, and the attribution requirements of all included dependencies.
