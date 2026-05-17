# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Twycross2010_Auxin_Transport."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Twycross2010AuxinTransportModel1005200000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Twycross2010_Auxin_Transport."""

    _SBML_ID = 'MODEL1005200000'
    _TITLE = 'Twycross2010_Auxin_Transport'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ext', 'S', 'a0', 'c1', 'a1', 'c2', 'a2', 'c3', 'a3', 'c4', 'a4', 'c5', 'a5', 'c6', 'a6', 'c7', 'a7', 'c8', 'a8', 'c9', 'a9', 'c10', 'a10', 'c11', 'a11', 'c12', 'a12', 'c13', 'a13', 'c14', 'a14', 'c15', 'a15', 'c16', 'a16', 'c17', 'a17', 'c18', 'a18', 'c19', 'a19', 'c20', 'a20', 'Fvar', 'Aprotc', 'Aprota', 'Aaniona', 'Aanionc', 'Bc', 'Ba']
    _SPECIES_LABELS = {'ext': 'ext', 'S': 'S', 'a0': 'a0', 'c1': 'c1', 'a1': 'a1', 'c2': 'c2', 'a2': 'a2', 'c3': 'c3', 'a3': 'a3', 'c4': 'c4', 'a4': 'a4', 'c5': 'c5', 'a5': 'a5', 'c6': 'c6', 'a6': 'a6', 'c7': 'c7', 'a7': 'a7', 'c8': 'c8', 'a8': 'a8', 'c9': 'c9', 'a9': 'a9', 'c10': 'c10', 'a10': 'a10', 'c11': 'c11', 'a11': 'a11', 'c12': 'c12', 'a12': 'a12', 'c13': 'c13', 'a13': 'a13', 'c14': 'c14', 'a14': 'a14', 'c15': 'c15', 'a15': 'a15', 'c16': 'c16', 'a16': 'a16', 'c17': 'c17', 'a17': 'a17', 'c18': 'c18', 'a18': 'a18', 'c19': 'c19', 'a19': 'a19', 'c20': 'c20', 'a20': 'a20', 'Fvar': 'Fvar', 'Aprotc': 'Aprotc', 'Aprota': 'Aprota', 'Aaniona': 'Aaniona', 'Aanionc': 'Aanionc', 'Bc': 'Bc', 'Ba': 'Ba'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_ext': ('ext', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ext`.'), 'initial_model_state_c9': ('c9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c9`.'), 'initial_model_state_c8': ('c8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c8`.'), 'initial_model_state_c7': ('c7', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c7`.'), 'initial_model_state_c6': ('c6', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c6`.'), 'initial_model_state_c5': ('c5', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `c5`.')}
    _HEADLINE_OUTPUTS = {'ext': ('ext', 'native SBML value', 'ext. Maps to SBML symbol `ext`.'), 'model_state_c9': ('c9', 'native SBML value', 'c9. Maps to SBML symbol `c9`.'), 'model_state_c8': ('c8', 'native SBML value', 'c8. Maps to SBML symbol `c8`.'), 'model_state_c7': ('c7', 'native SBML value', 'c7. Maps to SBML symbol `c7`.'), 'model_state_c6': ('c6', 'native SBML value', 'c6. Maps to SBML symbol `c6`.'), 'model_state_c5': ('c5', 'native SBML value', 'c5. Maps to SBML symbol `c5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1005200000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
