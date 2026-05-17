# Leloup2003 Circclock Ld

This Biosimulant lab wraps `Leloup2003 Circclock Ld` as a runnable systems biology model with a companion visualization module.
This model is described in the paper Toward a detailed computational model for the mammalian circadian clock. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Leloup2003_CircClock_LD. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Mb, Mp, Bc, Bn, Mc, and PCn, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **PCn** moved from 1.000 to 0.2556 across 1.0 simulation windows.


### Output Visualizations

![Leloup2003 Circclock Ld - run interpretation](assets/01-leloup2003-circclock-ld-lab-run-interpretation.png)

*Summary table for Leloup2003 Circclock Ld, reporting the scientific question, observed answer, dominant module, and caveat.*

![Leloup2003 Circclock Ld - timeseries visualization](assets/02-leloup2003-circclock-ld-gene-regulation.png)

*Trajectories of PCn, Mp, Bn, Mc, Mb, and Bc across the 1.0 simulation. In this run **Mp** climbed from 2.500 to 3.154 and **PCn** fell from 1.000 to 0.2556 — the largest movements among the focused observables.*

![Leloup2003 Circclock Ld - excursions bar](assets/03-leloup2003-circclock-ld-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **PCn** = 0.7444, **Mp** = 0.6537, **Bn** = 0.3070, with 3 more observables below.*

![Leloup2003 Circclock Ld - endpoint snapshot bar](assets/04-leloup2003-circclock-ld-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Mb** = 9.295, **Mp** = 3.154, **Bc** = 2.164, with 3 more observables below.*

![Leloup2003 Circclock Ld - visualization](assets/05-leloup2003-circclock-ld-activity-phase-portrait.png)

*Visualization card from the Leloup2003 Circclock Ld dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000078`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Mb | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_model_state_mb` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0`. |
| Initial Model State Mp | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_model_state_mp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_7`. |
| Initial Model State Bc | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_model_state_bc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`. |
| Initial Model State Bn | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_model_state_bn` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`. |
| Initial Model State Mc | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_model_state_mc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_5`. |
| Initial P Cn | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.initial_p_cn` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_mb` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.model_state_mb` | Available to the visualization model and downstream workflows. |
| `model_state_mp` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.model_state_mp` | Available to the visualization model and downstream workflows. |
| `model_state_bc` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.model_state_bc` | Available to the visualization model and downstream workflows. |
| `model_state_bn` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.model_state_bn` | Available to the visualization model and downstream workflows. |
| `model_state_mc` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.model_state_mc` | Available to the visualization model and downstream workflows. |
| `p_cn` | `systemsbiology_sbml_leloup2003_circclock_ld_biomd0000000078_model.p_cn` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
