# Locke2006 Circclock Ll

This Biosimulant lab wraps `Locke2006 Circclock Ll` as a runnable systems biology model with a companion visualization module.
This a model from the article: Experimental validation of a predicted feedback loop in the multi-oscillator clock of Arabidopsis thaliana. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Locke2006_CircClock_LL. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on PPR7/9 mRNA, PPR7/9 protein in nucleus, PPR7/9 protein in cytoplasm, TOC1 protein in cytoplasm, X protein in cytoplasm, and light sensitive protein P, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **TOC1 protein in cytoplasm** moved from 10.296 to 8.134 across 1.0 simulation windows.


### Output Visualizations

![Locke2006 Circclock Ll - run interpretation](assets/01-locke2006-circclock-ll-lab-run-interpretation.png)

*Summary table for Locke2006 Circclock Ll, reporting the scientific question, observed answer, dominant module, and caveat.*

![Locke2006 Circclock Ll - timeseries visualization](assets/02-locke2006-circclock-ll-gene-regulation.png)

*Trajectories of TOC1 protein in cytoplasm, PPR7/9 mRNA, light sensitive protein P, PPR7/9 protein in cytoplasm, X protein in cytoplasm, and PPR7/9 protein in nucleus across the 1.0 simulation. In this run **PPR7/9 mRNA** climbed from 14.692 to 16.276 and **TOC1 protein in cytoplasm** fell from 10.296 to 8.134 — the largest movements among the focused observables.*

![Locke2006 Circclock Ll - excursions bar](assets/03-locke2006-circclock-ll-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **TOC1 protein in cytoplasm** = 2.163, **PPR7/9 mRNA** = 1.584, **light sensitive protein P** = 0.6710, with 3 more observables below.*

![Locke2006 Circclock Ll - endpoint snapshot bar](assets/04-locke2006-circclock-ll-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **PPR7/9 mRNA** = 16.276, **TOC1 protein in cytoplasm** = 8.134, **X protein in cytoplasm** = 1.500, with 3 more observables below.*

![Locke2006 Circclock Ll - visualization](assets/05-locke2006-circclock-ll-activity-phase-portrait.png)

*Visualization card from the Locke2006 Circclock Ll dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000089`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Light | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.light` | | Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `light`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.species_labels` | Available to the visualization model and downstream workflows. |
| `ppr7_9_mrna` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.ppr7_9_mrna` | Available to the visualization model and downstream workflows. |
| `ppr7_9_protein_in_nucleus` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.ppr7_9_protein_in_nucleus` | Available to the visualization model and downstream workflows. |
| `ppr7_9_protein_in_cytoplasm` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.ppr7_9_protein_in_cytoplasm` | Available to the visualization model and downstream workflows. |
| `toc1_protein_in_cytoplasm` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.toc1_protein_in_cytoplasm` | Available to the visualization model and downstream workflows. |
| `x_protein_in_cytoplasm` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.x_protein_in_cytoplasm` | Available to the visualization model and downstream workflows. |
| `light_sensitive_protein_p` | `systemsbiology_sbml_locke2006_circclock_ll_biomd0000000089_model.light_sensitive_protein_p` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
