# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nielsen1998_Glycolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nielsen1998GlycolysisBiomd0000000042Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nielsen1998_Glycolysis."""

    _SBML_ID = 'BIOMD0000000042'
    _TITLE = 'Nielsen1998_Glycolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ATP', 'ADP', 'AMP', 'GLC', 'F6P', 'FBP', 'GAP', 'NAD', 'NADH', 'DPG', 'PEP', 'PYR', 'ACA', 'EtOH', 'P']
    _SPECIES_LABELS = {'ATP': 'ATP', 'ADP': 'ADP', 'AMP': 'AMP', 'GLC': 'GLC', 'F6P': 'F6P', 'FBP': 'FBP', 'GAP': 'GAP', 'NAD': 'NAD', 'NADH': 'NADH', 'DPG': 'DPG', 'PEP': 'PEP', 'PYR': 'PYR', 'ACA': 'ACA', 'EtOH': 'EtOH', 'P': 'P'}
    _PARAMETER_INPUTS = {'flow': ('flow', 0.011, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `flow`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'f6_p': ('F6P', 'native SBML value', 'F6P. Maps to SBML symbol `F6P`.'), 'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'et_oh': ('EtOH', 'native SBML value', 'EtOH. Maps to SBML symbol `EtOH`.'), 'dpg': ('DPG', 'native SBML value', 'DPG. Maps to SBML symbol `DPG`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000042.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
