# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fuss2006_MitoticActivation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fuss2006MitoticactivationBiomd0000000069Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fuss2006_MitoticActivation."""

    _SBML_ID = 'BIOMD0000000069'
    _TITLE = 'Fuss2006_MitoticActivation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['srci', 'srco', 'srca', 'srcc', 'Cbp_P_CSK', 'CSK_cytoplasm', 'PTP', 'PTP_pY789', 'Cbp', 'Cbp_P']
    _SPECIES_LABELS = {'srci': 'Srci', 'srco': 'Srco', 'srca': 'Srca', 'srcc': 'Srcc', 'Cbp_P_CSK': 'Cbp P CSK', 'CSK_cytoplasm': 'CSK Cytoplasm', 'PTP': 'PTP', 'PTP_pY789': 'PTP PY789', 'Cbp': 'Cbp', 'Cbp_P': 'Cbp P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_srci': ('srci', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `srci`.'), 'initial_model_state_ptp': ('PTP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PTP`.'), 'initial_model_state_cbp': ('Cbp', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cbp`.'), 'initial_csk_cytoplasm': ('CSK_cytoplasm', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CSK_cytoplasm`.'), 'initial_srco': ('srco', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `srco`.'), 'initial_srcc': ('srcc', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `srcc`.')}
    _HEADLINE_OUTPUTS = {'srci': ('srci', 'native SBML value', 'Srci. Maps to SBML symbol `srci`.'), 'ptp': ('PTP', 'native SBML value', 'PTP. Maps to SBML symbol `PTP`.'), 'cbp': ('Cbp', 'native SBML value', 'Cbp. Maps to SBML symbol `Cbp`.'), 'csk_cytoplasm': ('CSK_cytoplasm', 'native SBML value', 'CSK Cytoplasm. Maps to SBML symbol `CSK_cytoplasm`.'), 'srco': ('srco', 'native SBML value', 'Srco. Maps to SBML symbol `srco`.'), 'srcc': ('srcc', 'native SBML value', 'Srcc. Maps to SBML symbol `srcc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000069.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
