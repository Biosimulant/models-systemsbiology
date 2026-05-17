# Kogan2001 Aptt Coagulation

This Biosimulant lab wraps `Kogan2001 Aptt Coagulation` as a runnable systems biology model with a companion visualization module.
This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Kogan2001_aPTT_coagulation. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on alpha1AT, I, ATIII, alpha2M, II, and C1inh, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **I** moved from 8.300 to 6.219 across 1.0 simulation windows.


### Output Visualizations

![Kogan2001 Aptt Coagulation - run interpretation](assets/01-kogan2001-aptt-coagulation-lab-run-interpretation.png)

*Summary table for Kogan2001 Aptt Coagulation, reporting the scientific question, observed answer, dominant module, and caveat.*

![Kogan2001 Aptt Coagulation - timeseries visualization](assets/02-kogan2001-aptt-coagulation-core-system-states.png)

*Trajectories of I, II, ATIII, alpha1AT, alpha2M, and C1inh across the 1.0 simulation. In this run **I** fell from 8.300 to 6.219 — the largest movements among the focused observables.*

![Kogan2001 Aptt Coagulation - excursions bar](assets/03-kogan2001-aptt-coagulation-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **I** = 2.081, **II** = 0.0097, **ATIII** = 0.00807, with 3 more observables below.*

![Kogan2001 Aptt Coagulation - endpoint snapshot bar](assets/04-kogan2001-aptt-coagulation-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **alpha1AT** = 24.497, **I** = 6.219, **ATIII** = 3.392, with 3 more observables below.*

![Kogan2001 Aptt Coagulation - visualization](assets/05-kogan2001-aptt-coagulation-activity-phase-portrait.png)

*Visualization card from the Kogan2001 Aptt Coagulation dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1109160001`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Alpha1 At | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_alpha1_at` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_12`. |
| Initial Model State I | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_model_state_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_35`. |
| Initial Atiii | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_8`. |
| Initial Alpha2 M | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_alpha2_m` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`. |
| Initial Model State Ii | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_model_state_ii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_32`. |
| Initial C1inh | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.initial_c1inh` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.species_labels` | Available to the visualization model and downstream workflows. |
| `alpha1_at` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.alpha1_at` | Available to the visualization model and downstream workflows. |
| `model_state_i` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.model_state_i` | Available to the visualization model and downstream workflows. |
| `atiii` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.atiii` | Available to the visualization model and downstream workflows. |
| `alpha2_m` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.alpha2_m` | Available to the visualization model and downstream workflows. |
| `model_state_ii` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.model_state_ii` | Available to the visualization model and downstream workflows. |
| `c1inh` | `systemsbiology_sbml_kogan2001_aptt_coagulation_model1109160001_model.c1inh` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
