# Kim2011 Oscillator Extendediii

This Biosimulant lab wraps `Kim2011 Oscillator Extendediii` as a runnable systems biology model with a companion visualization module.
This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Kim2011_Oscillator_ExtendedIII. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on RNAP, RNaseH, RNaseHA3rI3, RNaseHA2rI2, RNaseHA1rI1, and RNAPT31A1sI1, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **RNAP** moved from 8.34e-08 to 6.75e-08 across 1.0 simulation windows.


### Output Visualizations

![Kim2011 Oscillator Extendediii - run interpretation](assets/01-kim2011-oscillator-extendediii-lab-run-interpretation.png)

*Summary table for Kim2011 Oscillator Extendediii, reporting the scientific question, observed answer, dominant module, and caveat.*

![Kim2011 Oscillator Extendediii - timeseries visualization](assets/02-kim2011-oscillator-extendediii-gene-regulation.png)

*Trajectories of RNAP, RNaseH, RNaseHA2rI2, RNaseHA3rI3, RNaseHA1rI1, and RNAPT31A1sI1 across the 1.0 simulation. In this run **RNaseHA2rI2** climbed from 0 to 4.63e-14 and **RNAP** fell from 8.34e-08 to 6.75e-08 — the largest movements among the focused observables.*

![Kim2011 Oscillator Extendediii - excursions bar](assets/03-kim2011-oscillator-extendediii-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **RNAP** = 1.59e-08, **RNaseH** = 5.89e-14, **RNaseHA2rI2** = 4.63e-14, with 3 more observables below.*

![Kim2011 Oscillator Extendediii - endpoint snapshot bar](assets/04-kim2011-oscillator-extendediii-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **RNAP** = 6.75e-08, **RNaseH** = 1.04e-08, **RNaseHA2rI2** = 4.63e-14, with 3 more observables below.*

![Kim2011 Oscillator Extendediii - visualization](assets/05-kim2011-oscillator-extendediii-activity-phase-portrait.png)

*Visualization card from the Kim2011 Oscillator Extendediii dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1012090006`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Rnap | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_rnap` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`. |
| Initial R Nase H | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_r_nase_h` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`. |
| Initial R Nase Ha3r I3 | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_r_nase_ha3r_i3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_32`. |
| Initial R Nase Ha2r I2 | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_r_nase_ha2r_i2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`. |
| Initial R Nase Ha1r I1 | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_r_nase_ha1r_i1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`. |
| Initial Rnapt31 A1S I1 | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.initial_rnapt31_a1s_i1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_38`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.species_labels` | Available to the visualization model and downstream workflows. |
| `rnap` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.rnap` | Available to the visualization model and downstream workflows. |
| `r_nase_h` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.r_nase_h` | Available to the visualization model and downstream workflows. |
| `r_nase_ha3r_i3` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.r_nase_ha3r_i3` | Available to the visualization model and downstream workflows. |
| `r_nase_ha2r_i2` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.r_nase_ha2r_i2` | Available to the visualization model and downstream workflows. |
| `r_nase_ha1r_i1` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.r_nase_ha1r_i1` | Available to the visualization model and downstream workflows. |
| `rnapt31_a1s_i1` | `systemsbiology_sbml_kim2011_oscillator_extendediii_model1012090006_model.rnapt31_a1s_i1` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
