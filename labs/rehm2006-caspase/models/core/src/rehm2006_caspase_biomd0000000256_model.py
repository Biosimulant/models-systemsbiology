# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rehm2006_Caspase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rehm2006CaspaseBiomd0000000256Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rehm2006_Caspase."""

    _SBML_ID = 'BIOMD0000000256'
    _TITLE = 'Rehm2006_Caspase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PC3', 'XIAP', 'C9', 'PC9', 'C3', 'C9P', 'XIAP_C3', 'XIAP_C9', 'XIAP_C9_C3', 'XIAP_p2frag', 'XIAP_p2frag_C3', 'BIR12', 'BIR12_C3', 'BIR3R', 'BIR3R_C9', 'BIR3R_p2frag', 'XIAP_2SMAC', 'BIR12_SMAC', 'BIR3R_SMAC', 'SMAC', 'APAF1', 'XIAP_p2frag_2SMAC', 'Substrate', 'ClvgPrds', 'SMAC_mito', 'CytC_mit', 'CytC_cell']
    _SPECIES_LABELS = {'PC3': 'ProCasp3', 'XIAP': 'XIAP', 'C9': 'Casp9(p35-p12)', 'PC9': 'ProCasp9', 'C3': 'C3', 'C9P': 'Casp9(p35-p10)', 'XIAP_C3': 'XIAP-Casp3', 'XIAP_C9': 'XIAP-Casp9', 'XIAP_C9_C3': 'XIAP-Casp9-Casp3', 'XIAP_p2frag': 'XIAP-p2 fragment', 'XIAP_p2frag_C3': 'XIAP-p2frag-Casp3', 'BIR12': 'BIR12', 'BIR12_C3': 'BIR12-Casp3', 'BIR3R': 'BIR3R', 'BIR3R_C9': 'BIR3R-Casp9', 'BIR3R_p2frag': 'BIR3R-p2frag', 'XIAP_2SMAC': 'XIAP-2*SMAC', 'BIR12_SMAC': 'BIR12-SMAC', 'BIR3R_SMAC': 'BIR3R-SMAC', 'SMAC': 'SMAC', 'APAF1': 'APAF1', 'XIAP_p2frag_2SMAC': 'XIAP-p2frag-2*SMAC', 'Substrate': 'Casp3 Substrate', 'ClvgPrds': 'Clevage Products', 'SMAC_mito': 'SMAC in mitochondrium', 'CytC_mit': 'Cytochrome C in mitochondrium', 'CytC_cell': 'cytosolic Cytochrome C'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytochrome_c_in_mitochondrium': ('CytC_mit', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CytC_mit`.'), 'initial_smac_in_mitochondrium': ('SMAC_mito', 0.126, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SMAC_mito`.'), 'initial_casp3_substrate': ('Substrate', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Substrate`.'), 'initial_pro_casp3': ('PC3', 0.12, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PC3`.'), 'initial_pro_casp9': ('PC9', 0.03, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PC9`.'), 'initial_cytosolic_cytochrome_c': ('CytC_cell', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CytC_cell`.')}
    _HEADLINE_OUTPUTS = {'cytochrome_c_in_mitochondrium': ('CytC_mit', 'native SBML value', 'Cytochrome C in mitochondrium. Maps to SBML symbol `CytC_mit`.'), 'smac_in_mitochondrium': ('SMAC_mito', 'native SBML value', 'SMAC in mitochondrium. Maps to SBML symbol `SMAC_mito`.'), 'casp3_substrate': ('Substrate', 'native SBML value', 'Casp3 Substrate. Maps to SBML symbol `Substrate`.'), 'pro_casp3': ('PC3', 'native SBML value', 'ProCasp3. Maps to SBML symbol `PC3`.'), 'pro_casp9': ('PC9', 'native SBML value', 'ProCasp9. Maps to SBML symbol `PC9`.'), 'cytosolic_cytochrome_c': ('CytC_cell', 'native SBML value', 'cytosolic Cytochrome C. Maps to SBML symbol `CytC_cell`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000256.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
