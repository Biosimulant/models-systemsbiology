# Zatorsky2006 P53

This Biosimulant lab wraps `Zatorsky2006 P53` as a runnable systems biology model with a companion visualization module.
The model reproduces the time profile of p53 and Mdm2 as depicted in Fig 6B of the plot for model 1. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Zatorsky2006_p53_Model1. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on precursor Mdm2, p53, and Mdm2, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **p53** moved from 0 to 0.2698 across 1.0 simulation windows.


### Output Visualizations

![Zatorsky2006 P53 - run interpretation](assets/01-zatorsky2006-p53-lab-run-interpretation.png)

*Summary table for Zatorsky2006 P53, reporting the scientific question, observed answer, dominant module, and caveat.*

![Zatorsky2006 P53 - timeseries visualization](assets/02-zatorsky2006-p53-model1-physiology-and-tissue-state.png)

*Trajectories of p53, precursor Mdm2, and Mdm2 across the 1.0 simulation. In this run **p53** climbed from 0 to 0.2698 — the largest movements among the focused observables.*

![Zatorsky2006 P53 - excursions bar](assets/03-zatorsky2006-p53-model1-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **p53** = 0.2698, **precursor Mdm2** = 0.0472, **Mdm2** = 0.00139.*

![Zatorsky2006 P53 - endpoint snapshot bar](assets/04-zatorsky2006-p53-model1-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **p53** = 0.2698, **precursor Mdm2** = 0.0472, **Mdm2** = 0.00139.*

![Zatorsky2006 P53 - visualization](assets/05-zatorsky2006-p53-model1-activity-phase-portrait.png)

*Visualization card from the Zatorsky2006 P53 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000159`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Precursor Mdm2 | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.initial_precursor_mdm2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y0`. |
| Initial Model State P53 | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.initial_model_state_p53` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`. |
| Initial Mdm2 | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.initial_mdm2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.species_labels` | Available to the visualization model and downstream workflows. |
| `precursor_mdm2` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.precursor_mdm2` | Available to the visualization model and downstream workflows. |
| `p53` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.p53` | Available to the visualization model and downstream workflows. |
| `mdm2` | `systemsbiology_sbml_zatorsky2006_p53_model1_biomd0000000159_model.mdm2` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
