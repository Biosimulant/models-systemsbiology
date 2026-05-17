# Bungay2006 Plasma

This Biosimulant lab wraps `Bungay2006 Plasma` as a runnable systems biology model with a companion visualization module.
This model is from the article: Modelling thrombin generation in human ovarian follicular fluid Bungay Sharene D., Gentry Patricia A., Gentry Rodney D. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Bungay2006_Plasma. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on AT_f, alpha2M_l, II_f, PS_f, X_f, and IX_f, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **II_f** moved from 1400.0 to 591.9 across 1.0 simulation windows.


### Output Visualizations

![Bungay2006 Plasma - run interpretation](assets/01-bungay2006-plasma-lab-run-interpretation.png)

*Summary table for Bungay2006 Plasma, reporting the scientific question, observed answer, dominant module, and caveat.*

![Bungay2006 Plasma - timeseries visualization](assets/02-bungay2006-plasma-gene-regulation.png)

*Trajectories of II_f, PS_f, X_f, IX_f, AT_f, and alpha2M_l across the 1.0 simulation. In this run **II_f** fell from 1400.0 to 591.9 — the largest movements among the focused observables.*

![Bungay2006 Plasma - excursions bar](assets/03-bungay2006-plasma-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **II_f** = 808.1, **PS_f** = 297.8, **X_f** = 116.7, with 3 more observables below.*

![Bungay2006 Plasma - endpoint snapshot bar](assets/04-bungay2006-plasma-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **AT_f** = 3400.0, **alpha2M_l** = 2600.0, **II_f** = 591.9, with 3 more observables below.*

![Bungay2006 Plasma - visualization](assets/05-bungay2006-plasma-activity-phase-portrait.png)

*Visualization card from the Bungay2006 Plasma dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000332`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial At F | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_at_f` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AT_f`. |
| Initial Alpha2 M L | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_alpha2_m_l` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha2M_l`. |
| Initial Ii F | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_ii_f` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II_f`. |
| Initial Ps F | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_ps_f` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PS_f`. |
| Initial Model State X F | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_model_state_x_f` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_f`. |
| Initial Ix F | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.initial_ix_f` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IX_f`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.species_labels` | Available to the visualization model and downstream workflows. |
| `at_f` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.at_f` | Available to the visualization model and downstream workflows. |
| `alpha2_m_l` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.alpha2_m_l` | Available to the visualization model and downstream workflows. |
| `ii_f` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.ii_f` | Available to the visualization model and downstream workflows. |
| `ps_f` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.ps_f` | Available to the visualization model and downstream workflows. |
| `x_f` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.x_f` | Available to the visualization model and downstream workflows. |
| `ix_f` | `systemsbiology_sbml_bungay2006_plasma_biomd0000000332_model.ix_f` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
