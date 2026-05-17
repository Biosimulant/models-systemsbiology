# Nijhout2004 Folate Cycle

This Biosimulant lab wraps `Nijhout2004 Folate Cycle` as a runnable systems biology model with a companion visualization module.
This is an SBML version of the folate cycle model model from: A mathematical model of the folate cycle: new insights into folate homeostasis. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Nijhout2004_Folate_Cycle. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on NADPH, Gly, HCOOH, Ser, DUMP, and GAR, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **NADPH** moved from 50.000 to 50.000 across 1.0 simulation windows.


### Output Visualizations

![Nijhout2004 Folate Cycle - run interpretation](assets/01-nijhout2004-folate-cycle-lab-run-interpretation.png)

*Summary table for Nijhout2004 Folate Cycle, reporting the scientific question, observed answer, dominant module, and caveat.*

![Nijhout2004 Folate Cycle - timeseries visualization](assets/02-nijhout2004-folate-cycle-metabolic-response.png)

*Trajectories of NADPH, Gly, HCOOH, Ser, DUMP, and GAR across the 1.0 simulation. In this run NADPH, Gly, HCOOH, Ser stayed near their initial values — no observable moved appreciably.*

![Nijhout2004 Folate Cycle - endpoint snapshot bar](assets/03-nijhout2004-folate-cycle-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Gly** = 1850.0, **HCOOH** = 900.0, **Ser** = 468.0, with 3 more observables below.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000213`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Nadph | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_nadph` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`. |
| Initial Model State Gly | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_model_state_gly` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`. |
| Initial Hcooh | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_hcooh` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HCOOH`. |
| Initial Model State Ser | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_model_state_ser` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ser`. |
| Initial Dump | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_dump` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dUMP`. |
| Initial Model State Gar | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.initial_model_state_gar` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GAR`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.species_labels` | Available to the visualization model and downstream workflows. |
| `nadph` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.nadph` | Available to the visualization model and downstream workflows. |
| `gly` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.gly` | Available to the visualization model and downstream workflows. |
| `hcooh` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.hcooh` | Available to the visualization model and downstream workflows. |
| `ser` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.ser` | Available to the visualization model and downstream workflows. |
| `dump` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.dump` | Available to the visualization model and downstream workflows. |
| `gar` | `systemsbiology_sbml_nijhout2004_folate_cycle_biomd0000000213_model.gar` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
