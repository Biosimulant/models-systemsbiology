# Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V

This Biosimulant lab wraps `Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V` as a runnable systems biology model with a companion visualization module.
Mathematical model of the blood coagulation cascade with new kinetic rates to simulate acidosis. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Mitrophanov2015 - Simulating extended Hockin Blood Coagulation Model under varied pH. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on mIIa_ATIII, mIIa, Xa_Va_II, Xa_Va, Xa_TFPI, and Xa_ATIII, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Xa_ATIII** moved from 0 to 2.31e-17 across 1.0 simulation windows.


### Output Visualizations

![Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V - run interpretation](assets/01-mitrophanov2015-simulating-extended-hockin-blood-coagulation-model-under-v-lab-r.png)

*Summary table for Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V, reporting the scientific question, observed answer, dominant module, and caveat.*

![Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V - timeseries visualization](assets/02-mitrophanov2015-simulating-extended-hockin-blood-coagulation-model-under-varied-.png)

*Trajectories of Xa_ATIII, Xa_TFPI, mIIa, Xa_Va, Xa_Va_II, and mIIa_ATIII across the 1.0 simulation. In this run **Xa_ATIII** climbed from 0 to 2.31e-17 — the largest movements among the focused observables.*

![Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V - excursions bar](assets/03-mitrophanov2015-simulating-extended-hockin-blood-coagulation-model-under-varied-.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Xa_ATIII** = 2.31e-17, **Xa_TFPI** = 3.63e-18, **mIIa** = 1.14e-24, with 3 more observables below.*

![Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V - endpoint snapshot bar](assets/04-mitrophanov2015-simulating-extended-hockin-blood-coagulation-model-under-varied-.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Xa_ATIII** = 2.31e-17, **Xa_TFPI** = 3.63e-18, **mIIa** = 1.14e-24, with 3 more observables below.*

![Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V - visualization](assets/05-mitrophanov2015-simulating-extended-hockin-blood-coagulation-model-under-varied-.png)

*Visualization card from the Mitrophanov2015 Simulating Extended Hockin Blood Coagulation Model Under V dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000951`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial M I Ia Atiii | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_m_i_ia_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`. |
| Initial M I Ia | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_m_i_ia` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`. |
| Initial Xa Va Ii | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_xa_va_ii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`. |
| Initial Xa Va | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_xa_va` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`. |
| Initial Xa Tfpi | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_xa_tfpi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`. |
| Initial Xa Atiii | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.initial_xa_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.species_labels` | Available to the visualization model and downstream workflows. |
| `m_i_ia_atiii` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.m_i_ia_atiii` | Available to the visualization model and downstream workflows. |
| `m_i_ia` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.m_i_ia` | Available to the visualization model and downstream workflows. |
| `xa_va_ii` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.xa_va_ii` | Available to the visualization model and downstream workflows. |
| `xa_va` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.xa_va` | Available to the visualization model and downstream workflows. |
| `xa_tfpi` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.xa_tfpi` | Available to the visualization model and downstream workflows. |
| `xa_atiii` | `systemsbiology_sbml_mitrophanov2015_simulating_extended_hockin_blood_biomd0000000951_model.xa_atiii` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
