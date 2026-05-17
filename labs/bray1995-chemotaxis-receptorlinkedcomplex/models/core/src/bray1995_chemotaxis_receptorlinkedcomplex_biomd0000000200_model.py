# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bray1995_chemotaxis_receptorlinkedcomplex."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bray1995ChemotaxisReceptorlinkedcomplexBiomd0000000200Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bray1995_chemotaxis_receptorlinkedcomplex."""

    _SBML_ID = 'BIOMD0000000200'
    _TITLE = 'Bray1995_chemotaxis_receptorlinkedcomplex'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AA', 'AAp', 'W', 'WAA', 'WAAp', 'WWAA', 'WWAAp', 'TT', 'TTW', 'TTWW', 'TTWAA', 'TTWAAp', 'TTAA', 'TTAAp', 'TTWWAA', 'TTWWAAp', 'Y', 'Yp', 'Z', 'B', 'Bp', 'SetYp']
    _SPECIES_LABELS = {'AA': 'AA', 'AAp': 'AAp', 'W': 'W', 'WAA': 'WAA', 'WAAp': 'WAAp', 'WWAA': 'WWAA', 'WWAAp': 'WWAAp', 'TT': 'TT', 'TTW': 'TTW', 'TTWW': 'TTWW', 'TTWAA': 'TTWAA', 'TTWAAp': 'TTWAAp', 'TTAA': 'TTAA', 'TTAAp': 'TTAAp', 'TTWWAA': 'TTWWAA', 'TTWWAAp': 'TTWWAAp', 'Y': 'Y', 'Yp': 'Yp', 'Z': 'Z', 'B': 'B', 'Bp': 'Bp', 'SetYp': 'setYp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_set_yp': ('SetYp', 1.63e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `SetYp`.'), 'initial_model_state_tt': ('TT', 2.5e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TT`.'), 'initial_model_state_aa': ('AA', 2.5e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AA`.'), 'initial_model_state_yp': ('Yp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Yp`.'), 'initial_wwa_ap': ('WWAAp', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `WWAAp`.'), 'initial_wwaa': ('WWAA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `WWAA`.')}
    _HEADLINE_OUTPUTS = {'set_yp': ('SetYp', 'native SBML value', 'setYp. Maps to SBML symbol `SetYp`.'), 'model_state_tt': ('TT', 'native SBML value', 'TT. Maps to SBML symbol `TT`.'), 'model_state_aa': ('AA', 'native SBML value', 'AA. Maps to SBML symbol `AA`.'), 'model_state_yp': ('Yp', 'native SBML value', 'Yp. Maps to SBML symbol `Yp`.'), 'wwa_ap': ('WWAAp', 'native SBML value', 'WWAAp. Maps to SBML symbol `WWAAp`.'), 'wwaa': ('WWAA', 'native SBML value', 'WWAA. Maps to SBML symbol `WWAA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000200.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
