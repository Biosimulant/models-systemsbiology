# Leloup2003 Circclock Ld Rev Erbalpha

This Biosimulant lab wraps `Leloup2003 Circclock Ld Rev Erbalpha` as a runnable systems biology model with a companion visualization module.
This is model is according to the paper Toward a detailed computational model for the mammalian circadian clock In this model interlocked negative and positive regulation of Per,Cry,Bmal,REV-ERBalpha. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Leloup2003_CircClock_LD_REV-ERBalpha. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Rn, Rc, Pcp, Pc, PCnp, and PCn, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Pc** moved from 0 to 2.16e-05 across 1.0 simulation windows.


### Output Visualizations

![Leloup2003 Circclock Ld Rev Erbalpha - run interpretation](assets/01-leloup2003-circclock-ld-rev-erbalpha-lab-run-interpretation.png)

*Summary table for Leloup2003 Circclock Ld Rev Erbalpha, reporting the scientific question, observed answer, dominant module, and caveat.*

![Leloup2003 Circclock Ld Rev Erbalpha - timeseries visualization](assets/02-leloup2003-circclock-ld-rev-erbalpha-physiology-and-tissue-state.png)

*Trajectories of Pc, Rc, Pcp, Rn, PCn, and PCnp across the 1.0 simulation. In this run **Pc** climbed from 0 to 2.16e-05 — the largest movements among the focused observables.*

![Leloup2003 Circclock Ld Rev Erbalpha - excursions bar](assets/03-leloup2003-circclock-ld-rev-erbalpha-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Pc** = 2.16e-05, **Rc** = 1.34e-05, **Pcp** = 8.61e-06, with 3 more observables below.*

![Leloup2003 Circclock Ld Rev Erbalpha - endpoint snapshot bar](assets/04-leloup2003-circclock-ld-rev-erbalpha-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Pc** = 2.16e-05, **Rc** = 1.34e-05, **Pcp** = 8.61e-06, with 3 more observables below.*

![Leloup2003 Circclock Ld Rev Erbalpha - visualization](assets/05-leloup2003-circclock-ld-rev-erbalpha-activity-phase-portrait.png)

*Visualization card from the Leloup2003 Circclock Ld Rev Erbalpha dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000083`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Rn | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_model_state_rn` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rn`. |
| Initial Model State Rc | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_model_state_rc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rc`. |
| Initial Model State Pcp | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_model_state_pcp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pcp`. |
| Initial Model State Pc | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_model_state_pc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pc`. |
| Initial P Cnp | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_p_cnp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCnp`. |
| Initial P Cn | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.initial_p_cn` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCn`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_rn` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.model_state_rn` | Available to the visualization model and downstream workflows. |
| `model_state_rc` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.model_state_rc` | Available to the visualization model and downstream workflows. |
| `pcp` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.pcp` | Available to the visualization model and downstream workflows. |
| `model_state_pc` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.model_state_pc` | Available to the visualization model and downstream workflows. |
| `p_cnp` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.p_cnp` | Available to the visualization model and downstream workflows. |
| `p_cn` | `systemsbiology_sbml_leloup2003_circclock_ld_rev_erbalpha_biomd0000000083_model.p_cn` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
