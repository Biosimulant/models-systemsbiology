# Orfao2008 Thrombingeneration Amidolyticactivity

This Biosimulant lab wraps `Orfao2008 Thrombingeneration Amidolyticactivity` as a runnable systems biology model with a companion visualization module.
S. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Orfao2008_ThrombinGeneration_AmidolyticActivity. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Xa_ATIII, IIa_alpha2M, IIa_ATIII, II, PL, and RVV, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **II** moved from 1.400 to 1.304 across 1.0 simulation windows.


### Output Visualizations

![Orfao2008 Thrombingeneration Amidolyticactivity - run interpretation](assets/01-orfao2008-thrombingeneration-amidolyticactivity-lab-run-interpretation.png)

*Summary table for Orfao2008 Thrombingeneration Amidolyticactivity, reporting the scientific question, observed answer, dominant module, and caveat.*

![Orfao2008 Thrombingeneration Amidolyticactivity - timeseries visualization](assets/02-orfao2008-thrombingeneration-amidolyticactivity-gene-regulation.png)

*Trajectories of II, Xa_ATIII, IIa_ATIII, IIa_alpha2M, PL, and RVV across the 1.0 simulation. In this run **Xa_ATIII** climbed from 0 to 0.0368 and **II** fell from 1.400 to 1.304 — the largest movements among the focused observables.*

![Orfao2008 Thrombingeneration Amidolyticactivity - excursions bar](assets/03-orfao2008-thrombingeneration-amidolyticactivity-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **II** = 0.0965, **Xa_ATIII** = 0.0368, **IIa_ATIII** = 0.0231, with 2 more observables below.*

![Orfao2008 Thrombingeneration Amidolyticactivity - endpoint snapshot bar](assets/04-orfao2008-thrombingeneration-amidolyticactivity-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **II** = 1.304, **PL** = 0.0500, **Xa_ATIII** = 0.0368, with 3 more observables below.*

![Orfao2008 Thrombingeneration Amidolyticactivity - visualization](assets/05-orfao2008-thrombingeneration-amidolyticactivity-activity-phase-portrait.png)

*Visualization card from the Orfao2008 Thrombingeneration Amidolyticactivity dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000366`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Xa Atiii | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_xa_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`. |
| Initial I Ia Alpha2 M | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_i_ia_alpha2_m` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_alpha2M`. |
| Initial I Ia Atiii | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_i_ia_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IIa_ATIII`. |
| Initial Model State Ii | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_model_state_ii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II`. |
| Initial Model State Pl | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_model_state_pl` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PL`. |
| Initial Model State Rvv | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.initial_model_state_rvv` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RVV`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.species_labels` | Available to the visualization model and downstream workflows. |
| `xa_atiii` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.xa_atiii` | Available to the visualization model and downstream workflows. |
| `i_ia_alpha2_m` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.i_ia_alpha2_m` | Available to the visualization model and downstream workflows. |
| `i_ia_atiii` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.i_ia_atiii` | Available to the visualization model and downstream workflows. |
| `model_state_ii` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.model_state_ii` | Available to the visualization model and downstream workflows. |
| `model_state_pl` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.model_state_pl` | Available to the visualization model and downstream workflows. |
| `rvv` | `systemsbiology_sbml_orfao2008_thrombingeneration_amidolyticactivity_biomd0000000366_model.rvv` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
