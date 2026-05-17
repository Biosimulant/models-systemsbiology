# Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf

This Biosimulant lab wraps `Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf` as a runnable systems biology model with a companion visualization module.
Proctor2008 - p53/Mdm2 circuit - p53 stabilisation by p14ARF This model is described in the article: Explaining oscillations and variability in the p53-Mdm2 system. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Proctor2008 - p53/Mdm2 circuit - p53 stablisation by p14ARF. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Mdm2mRNAdeg, Mdm2mRNAsyn, Mdm2 MRNA, Mdm2 P53, P53, and Mdm2, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Mdm2 P53** moved from 95.000 to 94.955 across 1.0 simulation windows.


### Output Visualizations

![Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf - run interpretation](assets/01-proctor2008-p53-mdm2-circuit-p53-stablisation-by-p14arf-lab-run-interpretation.png)

*Summary table for Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf - timeseries visualization](assets/02-proctor2008-p53-mdm2-circuit-p53-stablisation-by-p14arf-physiology-and-tissue-st.png)

*Trajectories of Mdm2 P53, P53, Mdm2, Mdm2mRNAsyn, Mdm2 MRNA, and Mdm2mRNAdeg across the 1.0 simulation. In this run **P53** climbed from 5.000 to 5.045 and **Mdm2 P53** fell from 95.000 to 94.955 — the largest movements among the focused observables.*

![Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf - excursions bar](assets/03-proctor2008-p53-mdm2-circuit-p53-stablisation-by-p14arf-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Mdm2 P53** = 0.0453, **P53** = 0.0450, **Mdm2** = 0.0433, with 3 more observables below.*

![Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf - endpoint snapshot bar](assets/04-proctor2008-p53-mdm2-circuit-p53-stablisation-by-p14arf-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Mdm2 P53** = 94.955, **P53** = 5.045, **Mdm2** = 5.043, with 3 more observables below.*

![Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf - visualization](assets/05-proctor2008-p53-mdm2-circuit-p53-stablisation-by-p14arf-activity-phase-portrait.png)

*Visualization card from the Proctor2008 P53 Mdm2 Circuit P53 Stablisation By P14arf dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000189`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Mdm2m Rn Adeg | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_mdm2m_rn_adeg` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2mRNAdeg`. |
| Initial Mdm2m Rn Asyn | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_mdm2m_rn_asyn` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2mRNAsyn`. |
| Initial Mdm2 MRNA | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_mdm2_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_mRNA`. |
| Initial Mdm2 P53 | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_mdm2_p53` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2_p53`. |
| Initial Model State P53 | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_model_state_p53` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `p53`. |
| Initial Mdm2 | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.initial_mdm2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mdm2`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.species_labels` | Available to the visualization model and downstream workflows. |
| `mdm2m_rn_adeg` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.mdm2m_rn_adeg` | Available to the visualization model and downstream workflows. |
| `mdm2m_rn_asyn` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.mdm2m_rn_asyn` | Available to the visualization model and downstream workflows. |
| `mdm2_mrna` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.mdm2_mrna` | Available to the visualization model and downstream workflows. |
| `mdm2_p53` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.mdm2_p53` | Available to the visualization model and downstream workflows. |
| `p53` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.p53` | Available to the visualization model and downstream workflows. |
| `mdm2` | `systemsbiology_sbml_proctor2008_p53_mdm2_circuit_p53_stablisation_by_biomd0000000189_model.mdm2` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
