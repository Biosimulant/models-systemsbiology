# Bertram1995 Pancreaticbetacell Crac

This Biosimulant lab wraps `Bertram1995 Pancreaticbetacell Crac` as a runnable systems biology model with a companion visualization module.
This a model from the article: A role for calcium release-activated current (CRAC) in cholinergic modulation ofelectrical activity in pancreatic beta-cells. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which physiological state variables carry the strongest baseline response? Source model: Bertram1995_PancreaticBetaCell_CRAC. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on V_membrane, ca_er_ca_equations, jm, Ca_i, and n, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **V_membrane** moved from -61.000 to -61.020 across 1.0 simulation windows.


### Output Visualizations

![Bertram1995 Pancreaticbetacell Crac - run interpretation](assets/01-bertram1995-pancreaticbetacell-crac-lab-run-interpretation.png)

*Summary table for Bertram1995 Pancreaticbetacell Crac, reporting the scientific question, observed answer, dominant module, and caveat.*

![Bertram1995 Pancreaticbetacell Crac - timeseries visualization](assets/02-bertram1995-pancreaticbetacell-crac-physiology-and-tissue-state.png)

*Trajectories of V_membrane, Ca_i, ca_er_ca_equations, jm, and n across the 1.0 simulation. In this run **Ca_i** climbed from 0.1100 to 0.1101 and **V_membrane** fell from -61.000 to -61.020 — the largest movements among the focused observables.*

![Bertram1995 Pancreaticbetacell Crac - excursions bar](assets/03-bertram1995-pancreaticbetacell-crac-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **V_membrane** = 0.0196, **Ca_i** = 0.000137, **ca_er_ca_equations** = 3.34e-05, with 2 more observables below.*

![Bertram1995 Pancreaticbetacell Crac - endpoint snapshot bar](assets/04-bertram1995-pancreaticbetacell-crac-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **V_membrane** = 61.020, **ca_er_ca_equations** = 9.000, **jm** = 0.2500, with 2 more observables below.*

![Bertram1995 Pancreaticbetacell Crac - visualization](assets/05-bertram1995-pancreaticbetacell-crac-activity-phase-portrait.png)

*Visualization card from the Bertram1995 Pancreaticbetacell Crac dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000374`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial V Membrane | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.initial_v_membrane` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V_membrane`. |
| Initial Ca Er Ca Equations | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.initial_ca_er_ca_equations` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_er_Ca_equations`. |
| Initial Model State Jm | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.initial_model_state_jm` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `jm`. |
| Initial Ca I | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.initial_ca_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_i`. |
| Initial Model State N | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.initial_model_state_n` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `n`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.species_labels` | Available to the visualization model and downstream workflows. |
| `v_membrane` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.v_membrane` | Available to the visualization model and downstream workflows. |
| `ca_er_ca_equations` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.ca_er_ca_equations` | Available to the visualization model and downstream workflows. |
| `model_state_jm` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.model_state_jm` | Available to the visualization model and downstream workflows. |
| `ca_i` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.ca_i` | Available to the visualization model and downstream workflows. |
| `model_state_n` | `systemsbiology_sbml_bertram1995_pancreaticbetacell_crac_biomd0000000374_model.model_state_n` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
