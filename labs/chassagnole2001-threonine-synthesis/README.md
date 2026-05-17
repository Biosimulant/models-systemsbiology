# Chassagnole2001 Threonine Synthesis

This Biosimulant lab wraps `Chassagnole2001 Threonine Synthesis` as a runnable systems biology model with a companion visualization module.
. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Chassagnole2001_Threonine Synthesis. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on NADPH, NADP, ATP, ADP, Threonine, and Aspartate, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **ADP** moved from 0 to 0.0339 across 1.0 simulation windows.


### Output Visualizations

![Chassagnole2001 Threonine Synthesis - run interpretation](assets/01-chassagnole2001-threonine-synthesis-lab-run-interpretation.png)

*Summary table for Chassagnole2001 Threonine Synthesis, reporting the scientific question, observed answer, dominant module, and caveat.*

![Chassagnole2001 Threonine Synthesis - timeseries visualization](assets/02-chassagnole2001-threonine-synthesis-metabolic-response.png)

*Trajectories of ADP, ATP, NADPH, NADP, Aspartate, and Threonine across the 1.0 simulation. In this run **ADP** climbed from 0 to 0.0339 and **ATP** fell from 10.000 to 9.966 — the largest movements among the focused observables.*

![Chassagnole2001 Threonine Synthesis - excursions bar](assets/03-chassagnole2001-threonine-synthesis-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **ADP** = 0.0339, **ATP** = 0.0339, **NADPH** = 0.0280, with 3 more observables below.*

![Chassagnole2001 Threonine Synthesis - endpoint snapshot bar](assets/04-chassagnole2001-threonine-synthesis-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **ATP** = 9.966, **Threonine** = 2.000, **Aspartate** = 1.974, with 3 more observables below.*

![Chassagnole2001 Threonine Synthesis - visualization](assets/05-chassagnole2001-threonine-synthesis-activity-phase-portrait.png)

*Visualization card from the Chassagnole2001 Threonine Synthesis dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000066`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Nadph | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_nadph` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nadph`. |
| Initial Nadp | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_nadp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nadp`. |
| Initial Model State ATP | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_model_state_atp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`. |
| Initial Model State ADP | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_model_state_adp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `adp`. |
| Initial Threonine | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_threonine` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `thr`. |
| Initial Aspartate | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.initial_aspartate` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `asp`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.species_labels` | Available to the visualization model and downstream workflows. |
| `nadph` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.nadph` | Available to the visualization model and downstream workflows. |
| `nadp` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.nadp` | Available to the visualization model and downstream workflows. |
| `atp` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.atp` | Available to the visualization model and downstream workflows. |
| `adp` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.adp` | Available to the visualization model and downstream workflows. |
| `threonine` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.threonine` | Available to the visualization model and downstream workflows. |
| `aspartate` | `systemsbiology_sbml_chassagnole2001_threonine_synthesis_biomd0000000066_model.aspartate` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
