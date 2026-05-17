# Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 (BIOMD0000000870)

This Biosimulant lab wraps `BIOMD0000000870 Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2` as a runnable systems biology model with a companion visualization module.
This model represents NIK-dependent p100 processing into p52 and NIK-dependent IkBd degradation with mass action kinetics. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Simon2019 - NIK-dependent p100 processing into p52 and IkBd degradation, mass action, SBML 2v4. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on p100t, p52, p100:NIK, p100, IkBd:NIK, and NIK, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **p100** moved from 0 to 0.4400 across 1.0 simulation windows.


### Output Visualizations

![Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 - run interpretation](assets/01-simon2019-nik-dependent-p100-processing-into-p52-and-ikbd-degradatio-2-lab-run-i.png)

*Summary table for Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 - timeseries visualization](assets/02-simon2019-nik-dependent-p100-processing-into-p52-and-ikbd-degradation-mass-actio.png)

*Trajectories of p100, NIK, p100:NIK, p52, IkBd:NIK, and p100t across the 1.0 simulation. In this run **p100** climbed from 0 to 0.4400 and **NIK** fell from 10.000 to 9.990 — the largest movements among the focused observables.*

![Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 - excursions bar](assets/03-simon2019-nik-dependent-p100-processing-into-p52-and-ikbd-degradation-mass-actio.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **p100** = 0.4400, **NIK** = 0.00982, **p100:NIK** = 0.00982, with 2 more observables below.*

![Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 - endpoint snapshot bar](assets/04-simon2019-nik-dependent-p100-processing-into-p52-and-ikbd-degradation-mass-actio.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **NIK** = 9.990, **p100t** = 2.500, **p100** = 0.4400, with 3 more observables below.*

![Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 - visualization](assets/05-simon2019-nik-dependent-p100-processing-into-p52-and-ikbd-degradation-mass-actio.png)

*Visualization card from the Simon2019 Nik Dependent P100 Processing Into P52 And Ikbd Degradatio 2 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000870`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial P100t | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_p100t` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p100t`. |
| Initial Model State P52 | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_model_state_p52` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p52`. |
| Initial P100 Nik | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_p100_nik` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p100_NIK`. |
| Initial P100 | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_p100` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p100`. |
| Initial Ik Bd Nik | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_ik_bd_nik` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkBd_NIK`. |
| Initial Model State Nik | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.initial_model_state_nik` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NIK`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.species_labels` | Available to the visualization model and downstream workflows. |
| `p100t` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.p100t` | Available to the visualization model and downstream workflows. |
| `p52` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.p52` | Available to the visualization model and downstream workflows. |
| `p100_nik` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.p100_nik` | Available to the visualization model and downstream workflows. |
| `p100` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.p100` | Available to the visualization model and downstream workflows. |
| `ik_bd_nik` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.ik_bd_nik` | Available to the visualization model and downstream workflows. |
| `nik` | `systemsbiology_sbml_simon2019_nik_dependent_p100_processing_into_p52_biomd0000000870_model.nik` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
