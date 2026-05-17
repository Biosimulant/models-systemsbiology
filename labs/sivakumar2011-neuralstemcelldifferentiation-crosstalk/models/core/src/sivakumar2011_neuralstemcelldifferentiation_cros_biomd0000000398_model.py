# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sivakumar2011_NeuralStemCellDifferentiation_Crosstalk."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sivakumar2011NeuralstemcelldifferentiationCrosBiomd0000000398Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sivakumar2011_NeuralStemCellDifferentiation_Crosstalk."""

    _SBML_ID = 'BIOMD0000000398'
    _TITLE = 'Sivakumar2011_NeuralStemCellDifferentiation_Crosstalk'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s53', 's57', 's58', 's60', 's61', 's68', 's72', 's73', 's81', 's83', 's85', 's88', 's89', 's96', 's98', 's100', 's101', 's107', 's109', 's111', 's122', 's124', 's135', 's142', 's144', 's146', 's147']
    _SPECIES_LABELS = {'s53': 'NICD', 's57': 'Notch', 's58': 'Notch TM', 's60': 'Gamma secretase', 's61': 'DAPT', 's68': 'RBP-jk', 's72': 'Complex NICD-RBP', 's73': 'Hes-1', 's81': 'Shh', 's83': 'Ptch1', 's85': 'Complex Shh Ptch1', 's88': 'smo', 's89': 'SAG', 's96': 'EGF', 's98': 'EGFR', 's100': 'Complex EGF-EGFR', 's101': 'Erlotinib', 's107': 'Wnt', 's109': 'Frzzl', 's111': 'Complex Wnt-Frzzl', 's122': 'Dishevelled', 's124': 'FRAT-CK2', 's135': 'Complex Dishevelled-FRAT-CK2', 's142': 'GSK3B', 's144': 'Beta-catenin', 's146': 'Complex GSK3B-Bcatenin', 's147': '6 bromoindirubin 3`oxime'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_erlotinib': ('s101', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s101`.'), 'initial_dapt': ('s61', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s61`.'), 'initial_model_state_6_bromoindirubin_3_oxime': ('s147', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s147`.'), 'initial_model_state_smo': ('s88', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s88`.'), 'initial_model_state_wnt': ('s107', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s107`.'), 'initial_model_state_shh': ('s81', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `s81`.')}
    _HEADLINE_OUTPUTS = {'erlotinib': ('s101', 'native SBML value', 'Erlotinib. Maps to SBML symbol `s101`.'), 'dapt': ('s61', 'native SBML value', 'DAPT. Maps to SBML symbol `s61`.'), 'model_state_6_bromoindirubin_3_oxime': ('s147', 'native SBML value', '6 bromoindirubin 3`oxime. Maps to SBML symbol `s147`.'), 'smo': ('s88', 'native SBML value', 'smo. Maps to SBML symbol `s88`.'), 'wnt': ('s107', 'native SBML value', 'Wnt. Maps to SBML symbol `s107`.'), 'shh': ('s81', 'native SBML value', 'Shh. Maps to SBML symbol `s81`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000398.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
