# Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio

This Biosimulant lab wraps `Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio` as a runnable systems biology model with a companion visualization module.
Palmer2014 - Effect of IL-1β-Blocking therapies in T2DM - Healthy Condition This is the model with healthy state initial conditions. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Palmer2014 - Effect of IL-1β-Blocking therapies in T2DM - Healthy Condition. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Insulin, Proinsulin, Glucose, IL1Ra, Rbc1, and Rbc2, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Proinsulin** moved from 6.500 to 6.554 across 1.0 simulation windows.


### Output Visualizations

![Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio - run interpretation](assets/01-palmer2014-effect-of-il-1-blocking-therapies-in-t2dm-healthy-conditio-lab-run-in.png)

*Summary table for Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio, reporting the scientific question, observed answer, dominant module, and caveat.*

![Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio - timeseries visualization](assets/02-palmer2014-effect-of-il-1-blocking-therapies-in-t2dm-healthy-condition-signallin.png)

*Trajectories of Proinsulin, Insulin, Rbc2, Rbc1, Glucose, and IL1Ra across the 1.0 simulation. In this run **Proinsulin** climbed from 6.500 to 6.554 and **Glucose** fell from 5.000 to 5.000 — the largest movements among the focused observables.*

![Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio - excursions bar](assets/03-palmer2014-effect-of-il-1-blocking-therapies-in-t2dm-healthy-condition-largest-a.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Proinsulin** = 0.0544, **Insulin** = 0.0168, **Rbc2** = 0.0057, with 2 more observables below.*

![Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio - endpoint snapshot bar](assets/04-palmer2014-effect-of-il-1-blocking-therapies-in-t2dm-healthy-condition-final-sta.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Insulin** = 50.017, **IL1Ra** = 25.000, **Rbc1** = 8.632, with 3 more observables below.*

![Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio - visualization](assets/05-palmer2014-effect-of-il-1-blocking-therapies-in-t2dm-healthy-condition-activity-.png)

*Visualization card from the Palmer2014 Effect Of Il 1 Blocking Therapies In T2dm Healthy Conditio dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000621`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Kglucose | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.kglucose` | | Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Kglucose`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.species_labels` | Available to the visualization model and downstream workflows. |
| `insulin` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.insulin` | Available to the visualization model and downstream workflows. |
| `proinsulin` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.proinsulin` | Available to the visualization model and downstream workflows. |
| `glucose` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.glucose` | Available to the visualization model and downstream workflows. |
| `il1_ra` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.il1_ra` | Available to the visualization model and downstream workflows. |
| `rbc1` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.rbc1` | Available to the visualization model and downstream workflows. |
| `rbc2` | `systemsbiology_sbml_palmer2014_effect_of_il_1_blocking_therapies_in_biomd0000000621_model.rbc2` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
