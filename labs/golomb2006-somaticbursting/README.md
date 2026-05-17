# Golomb2006 Somaticbursting

This Biosimulant lab wraps `Golomb2006 Somaticbursting` as a runnable systems biology model with a companion visualization module.
Model is according to the paper Contribution of Persistent Na+ Current and M-Type K+ Current to Somatic Bursting in CA1 Pyramidal Cell: Combined Experimental. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Golomb2006_SomaticBursting. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Zzs, Nns, Hhs, Bbs, and V, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **V** moved from -71.813 to -71.233 across 1.0 simulation windows.


### Output Visualizations

![Golomb2006 Somaticbursting - run interpretation](assets/01-golomb2006-somaticbursting-lab-run-interpretation.png)

*Summary table for Golomb2006 Somaticbursting, reporting the scientific question, observed answer, dominant module, and caveat.*

![Golomb2006 Somaticbursting - timeseries visualization](assets/02-golomb2006-somaticbursting-physiology-and-tissue-state.png)

*Trajectories of V, Hhs, Nns, Bbs, and Zzs across the 1.0 simulation. In this run **V** climbed from -71.813 to -71.233 and **Hhs** fell from 0.9879 to 0.9812 — the largest movements among the focused observables.*

![Golomb2006 Somaticbursting - excursions bar](assets/03-golomb2006-somaticbursting-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **V** = 0.5801, **Hhs** = 0.00665, **Nns** = 0.000707, with 2 more observables below.*

![Golomb2006 Somaticbursting - endpoint snapshot bar](assets/04-golomb2006-somaticbursting-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **V** = 71.233, **Hhs** = 0.9812, **Bbs** = 0.2031, with 2 more observables below.*

![Golomb2006 Somaticbursting - visualization](assets/05-golomb2006-somaticbursting-activity-phase-portrait.png)

*Visualization card from the Golomb2006 Somaticbursting dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000118`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Zzs | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.initial_model_state_zzs` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `zzs`. |
| Initial Model State Nns | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.initial_model_state_nns` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nns`. |
| Initial Model State Hhs | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.initial_model_state_hhs` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `hhs`. |
| Initial Model State Bbs | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.initial_model_state_bbs` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `bbs`. |
| Initial Model State V | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.initial_model_state_v` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `V`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.species_labels` | Available to the visualization model and downstream workflows. |
| `zzs` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.zzs` | Available to the visualization model and downstream workflows. |
| `nns` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.nns` | Available to the visualization model and downstream workflows. |
| `hhs` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.hhs` | Available to the visualization model and downstream workflows. |
| `bbs` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.bbs` | Available to the visualization model and downstream workflows. |
| `model_state_v` | `systemsbiology_sbml_golomb2006_somaticbursting_biomd0000000118_model.model_state_v` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
