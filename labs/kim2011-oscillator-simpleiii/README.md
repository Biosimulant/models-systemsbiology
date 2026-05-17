# Kim2011 Oscillator Simpleiii

This Biosimulant lab wraps `Kim2011 Oscillator Simpleiii` as a runnable systems biology model with a companion visualization module.
This a model from the article: Synthetic in vitro transcriptional oscillators. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Kim2011_Oscillator_SimpleIII. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on x3, x2, and x1, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **x1** moved from 0 to 0.4896 across 1.0 simulation windows.


### Output Visualizations

![Kim2011 Oscillator Simpleiii - run interpretation](assets/01-kim2011-oscillator-simpleiii-lab-run-interpretation.png)

*Summary table for Kim2011 Oscillator Simpleiii, reporting the scientific question, observed answer, dominant module, and caveat.*

![Kim2011 Oscillator Simpleiii - timeseries visualization](assets/02-kim2011-oscillator-simpleiii-gene-regulation.png)

*Trajectories of x1, x2, and x3 across the 1.0 simulation. In this run **x1** climbed from 0 to 0.4896 — the largest movements among the focused observables.*

![Kim2011 Oscillator Simpleiii - excursions bar](assets/03-kim2011-oscillator-simpleiii-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **x1** = 0.4896, **x2** = 0.4603, **x3** = 0.3326.*

![Kim2011 Oscillator Simpleiii - endpoint snapshot bar](assets/04-kim2011-oscillator-simpleiii-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **x3** = 0.6626, **x1** = 0.4896, **x2** = 0.4603.*

![Kim2011 Oscillator Simpleiii - visualization](assets/05-kim2011-oscillator-simpleiii-activity-phase-portrait.png)

*Visualization card from the Kim2011 Oscillator Simpleiii dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000323`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State X3 | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.initial_model_state_x3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_3`. |
| Initial Model State X2 | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.initial_model_state_x2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_2`. |
| Initial Model State X1 | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.initial_model_state_x1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_1`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_x3` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.model_state_x3` | Available to the visualization model and downstream workflows. |
| `model_state_x2` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.model_state_x2` | Available to the visualization model and downstream workflows. |
| `model_state_x1` | `systemsbiology_sbml_kim2011_oscillator_simpleiii_biomd0000000323_model.model_state_x1` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
