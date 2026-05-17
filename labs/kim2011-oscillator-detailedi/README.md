# Kim2011 Oscillator Detailedi

This Biosimulant lab wraps `Kim2011 Oscillator Detailedi` as a runnable systems biology model with a companion visualization module.
This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Kim2011_Oscillator_DetailedI. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on RNAP, RNaseH, RNaseHrA1dI1, RNaseHA2rI2, RNAPT21A1, and RNAPT21, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **RNAP** moved from 1.25e-07 to 1.09e-07 across 1.0 simulation windows.


### Output Visualizations

![Kim2011 Oscillator Detailedi - run interpretation](assets/01-kim2011-oscillator-detailedi-lab-run-interpretation.png)

*Summary table for Kim2011 Oscillator Detailedi, reporting the scientific question, observed answer, dominant module, and caveat.*

![Kim2011 Oscillator Detailedi - timeseries visualization](assets/02-kim2011-oscillator-detailedi-gene-regulation.png)

*Trajectories of RNAP, RNAPT21, RNAPT21A1, RNaseH, RNaseHA2rI2, and RNaseHrA1dI1 across the 1.0 simulation. In this run **RNAPT21** climbed from 0 to 9.66e-09 and **RNAP** fell from 1.25e-07 to 1.09e-07 — the largest movements among the focused observables.*

![Kim2011 Oscillator Detailedi - excursions bar](assets/03-kim2011-oscillator-detailedi-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **RNAP** = 1.6e-08, **RNAPT21** = 9.89e-09, **RNAPT21A1** = 1.13e-09, with 3 more observables below.*

![Kim2011 Oscillator Detailedi - endpoint snapshot bar](assets/04-kim2011-oscillator-detailedi-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **RNAP** = 1.09e-07, **RNaseH** = 1.5e-08, **RNAPT21** = 9.66e-09, with 3 more observables below.*

![Kim2011 Oscillator Detailedi - visualization](assets/05-kim2011-oscillator-detailedi-activity-phase-portrait.png)

*Visualization card from the Kim2011 Oscillator Detailedi dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1012090002`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Rnap | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_rnap` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_13`. |
| Initial R Nase H | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_r_nase_h` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_14`. |
| Initial R Nase Hr A1D I1 | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_r_nase_hr_a1d_i1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_19`. |
| Initial R Nase Ha2r I2 | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_r_nase_ha2r_i2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_20`. |
| Initial Rnapt21 A1 | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_rnapt21_a1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_17`. |
| Initial Rnapt21 | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.initial_rnapt21` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_18`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.species_labels` | Available to the visualization model and downstream workflows. |
| `rnap` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.rnap` | Available to the visualization model and downstream workflows. |
| `r_nase_h` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.r_nase_h` | Available to the visualization model and downstream workflows. |
| `r_nase_hr_a1d_i1` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.r_nase_hr_a1d_i1` | Available to the visualization model and downstream workflows. |
| `r_nase_ha2r_i2` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.r_nase_ha2r_i2` | Available to the visualization model and downstream workflows. |
| `rnapt21_a1` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.rnapt21_a1` | Available to the visualization model and downstream workflows. |
| `rnapt21` | `systemsbiology_sbml_kim2011_oscillator_detailedi_model1012090002_model.rnapt21` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
