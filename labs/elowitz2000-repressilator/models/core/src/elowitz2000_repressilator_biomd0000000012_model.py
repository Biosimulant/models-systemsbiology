# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Elowitz2000 - Repressilator."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Elowitz2000RepressilatorBiomd0000000012Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Elowitz2000 - Repressilator."""

    _SBML_ID = 'BIOMD0000000012'
    _TITLE = 'Elowitz2000 - Repressilator'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PX', 'PY', 'PZ', 'X', 'Y', 'Z']
    _SPECIES_LABELS = {'PX': 'LacI protein', 'PY': 'TetR protein', 'PZ': 'cI protein', 'X': 'LacI mRNA', 'Y': 'TetR mRNA', 'Z': 'cI mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c_i_protein': ('PZ', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PZ`.'), 'initial_tet_r_protein': ('PY', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PY`.'), 'initial_lac_i_protein': ('PX', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PX`.'), 'initial_tet_r_mrna': ('Y', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`.'), 'initial_c_i_mrna': ('Z', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`.'), 'initial_lac_i_mrna': ('X', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`.')}
    _HEADLINE_OUTPUTS = {'c_i_protein': ('PZ', 'native SBML value', 'cI protein. Maps to SBML symbol `PZ`.'), 'tet_r_protein': ('PY', 'native SBML value', 'TetR protein. Maps to SBML symbol `PY`.'), 'lac_i_protein': ('PX', 'native SBML value', 'LacI protein. Maps to SBML symbol `PX`.'), 'tet_r_mrna': ('Y', 'native SBML value', 'TetR mRNA. Maps to SBML symbol `Y`.'), 'c_i_mrna': ('Z', 'native SBML value', 'cI mRNA. Maps to SBML symbol `Z`.'), 'lac_i_mrna': ('X', 'native SBML value', 'LacI mRNA. Maps to SBML symbol `X`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000012.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
