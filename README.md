# models-systemsbiology

Curated systems-biology model labs for Biosimulant.

This repository contains 574 kept systems-biology labs using the standard Biosimulant layout:

```text
labs/<author><year>-<short-scientific-topic>/
  lab.yaml
  models/core/
  models/visualisation/
```

Source model files remain the scientific source of truth. SBML-backed kept labs run through `biosim.contrib.sbml.TelluriumSBMLBioModule`; source-data cases that could not be parsed or validated as SBML were moved to `/Volumes/dem-ssd/imp/projects/Nitoons/Biosimulant/models/orphan` with README evidence and recommended next action.

Cleanup summary:
- Kept labs: 574
- Orphaned systems-biology source-data/runtime cases: 203
- Audit report: `SYSTEMSBIOLOGY_CLEANUP_AUDIT.md`
- Temporary mapping used for migration: `.cleanup_tmp/systemsbiology_lab_mapping.tsv`
