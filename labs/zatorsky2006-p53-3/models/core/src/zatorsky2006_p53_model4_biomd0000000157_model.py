# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Zatorsky2006_p53_Model4."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zatorsky2006P53Model4Biomd0000000157Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Zatorsky2006_p53_Model4."""

    _SBML_ID = 'BIOMD0000000157'
    _TITLE = 'Zatorsky2006_p53_Model4'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'y0']
    _SPECIES_LABELS = {'x': 'p53', 'y': 'Mdm2', 'y0': 'precursor Mdm2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_precursor_mdm2': ('y0', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y0`.'), 'initial_mdm2': ('y', 0.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y`.'), 'initial_model_state_p53': ('x', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `x`.')}
    _HEADLINE_OUTPUTS = {'precursor_mdm2': ('y0', 'native SBML value', 'precursor Mdm2. Maps to SBML symbol `y0`.'), 'mdm2': ('y', 'native SBML value', 'Mdm2. Maps to SBML symbol `y`.'), 'p53': ('x', 'native SBML value', 'p53. Maps to SBML symbol `x`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000157.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
