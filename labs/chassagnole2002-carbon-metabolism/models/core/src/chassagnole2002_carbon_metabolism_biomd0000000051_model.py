# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Chassagnole2002_Carbon_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chassagnole2002CarbonMetabolismBiomd0000000051Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Chassagnole2002_Carbon_Metabolism."""

    _SBML_ID = 'BIOMD0000000051'
    _TITLE = 'Chassagnole2002_Carbon_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cpep', 'cglcex', 'cg6p', 'cpyr', 'cf6p', 'cg1p', 'cpg', 'cfdp', 'csed7p', 'cgap', 'ce4p', 'cxyl5p', 'crib5p', 'cdhap', 'cpgp', 'cpg3', 'cpg2', 'cribu5p']
    _SPECIES_LABELS = {'cpep': 'Phosphoenol pyruvate', 'cglcex': 'Extracellular Glucose', 'cg6p': 'Glucose-6-Phosphate', 'cpyr': 'Pyruvate', 'cf6p': 'Fructose-6-Phosphate', 'cg1p': 'Glucose-1-Phosphate', 'cpg': '6-Phosphogluconate', 'cfdp': 'Fructose-1,6-bisphosphate', 'csed7p': 'sedoheptulose-7-phosphate', 'cgap': 'Glyceraldehyde-3-Phosphate', 'ce4p': 'Erythrose-4-phosphate', 'cxyl5p': 'Xylulose-5-phosphate', 'crib5p': 'Ribose-5-phosphate', 'cdhap': 'Dihydroxyacetonephosphate', 'cpgp': '1,3-diphosphosphoglycerate', 'cpg3': '3-Phosphoglycerate', 'cpg2': '2-Phosphoglycerate', 'cribu5p': 'Ribulose-5-phosphate'}
    _PARAMETER_INPUTS = {'cfeed': ('cfeed', 110.96, 'mM', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `cfeed`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'glucose_6_phosphate': ('cg6p', 'native SBML value', 'Glucose-6-Phosphate. Maps to SBML symbol `cg6p`.'), 'pyruvate': ('cpyr', 'native SBML value', 'Pyruvate. Maps to SBML symbol `cpyr`.'), 'phosphoenol_pyruvate': ('cpep', 'native SBML value', 'Phosphoenol pyruvate. Maps to SBML symbol `cpep`.'), 'model_state_3_phosphoglycerate': ('cpg3', 'native SBML value', '3-Phosphoglycerate. Maps to SBML symbol `cpg3`.'), 'extracellular_glucose': ('cglcex', 'native SBML value', 'Extracellular Glucose. Maps to SBML symbol `cglcex`.'), 'model_state_6_phosphogluconate': ('cpg', 'native SBML value', '6-Phosphogluconate. Maps to SBML symbol `cpg`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000051.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
