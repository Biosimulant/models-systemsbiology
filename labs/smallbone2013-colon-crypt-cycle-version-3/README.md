# Smallbone2013 Colon Crypt Cycle Version 3

This Biosimulant lab wraps `Smallbone2013 Colon Crypt Cycle Version 3` as a runnable systems biology model with a companion visualization module.
Smallbone2013 - Colon Crypt cycle - Version 3 This model is described in the article: A mathematical model of the colon crypt capturing compositional dynamic interactions between cell types Kieran Sma. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Smallbone2013 - Colon Crypt cycle - Version 3. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on N2, N1, N0, and N3, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **N2** moved from 44.617 to 48.587 across 1.0 simulation windows.


### Output Visualizations

![Smallbone2013 Colon Crypt Cycle Version 3 - run interpretation](assets/01-smallbone2013-colon-crypt-cycle-version-3-lab-run-interpretation.png)

*Summary table for Smallbone2013 Colon Crypt Cycle Version 3, reporting the scientific question, observed answer, dominant module, and caveat.*

![Smallbone2013 Colon Crypt Cycle Version 3 - timeseries visualization](assets/02-smallbone2013-colon-crypt-cycle-version-3-physiology-and-tissue-state.png)

*Trajectories of N2, N1, N0, and N3 across the 1.0 simulation. In this run **N2** climbed from 44.617 to 48.587 — the largest movements among the focused observables.*

![Smallbone2013 Colon Crypt Cycle Version 3 - excursions bar](assets/03-smallbone2013-colon-crypt-cycle-version-3-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **N2** = 3.971, **N1** = 1.469, **N0** = 0.0415, with 1 more observable below.*

![Smallbone2013 Colon Crypt Cycle Version 3 - endpoint snapshot bar](assets/04-smallbone2013-colon-crypt-cycle-version-3-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **N2** = 48.587, **N1** = 28.273, **N0** = 1.757, with 1 more observable below.*

![Smallbone2013 Colon Crypt Cycle Version 3 - visualization](assets/05-smallbone2013-colon-crypt-cycle-version-3-activity-phase-portrait.png)

*Visualization card from the Smallbone2013 Colon Crypt Cycle Version 3 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000517`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State N2 | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.initial_model_state_n2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N2`. |
| Initial Model State N1 | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.initial_model_state_n1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N1`. |
| Initial Model State N0 | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.initial_model_state_n0` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N0`. |
| Initial Model State N3 | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.initial_model_state_n3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `N3`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_n2` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.model_state_n2` | Available to the visualization model and downstream workflows. |
| `model_state_n1` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.model_state_n1` | Available to the visualization model and downstream workflows. |
| `model_state_n0` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.model_state_n0` | Available to the visualization model and downstream workflows. |
| `model_state_n3` | `systemsbiology_sbml_smallbone2013_colon_crypt_cycle_version_3_biomd0000000517_model.model_state_n3` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
