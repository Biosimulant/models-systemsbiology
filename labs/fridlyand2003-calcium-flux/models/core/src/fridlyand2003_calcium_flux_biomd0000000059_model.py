# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fridlyand2003_Calcium_flux."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fridlyand2003CalciumFluxBiomd0000000059Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fridlyand2003_Calcium_flux."""

    _SBML_ID = 'BIOMD0000000059'
    _TITLE = 'Fridlyand2003_Calcium_flux'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ca_cyt', 'Ca_er', 'IP3_cyt', 'Na_cyt', 'ATP_cyt', 'ADP_cyt']
    _SPECIES_LABELS = {'Ca_cyt': 'Cytosolic Calcium', 'Ca_er': 'ER Calcium', 'IP3_cyt': 'Cytosolic IP3', 'Na_cyt': 'Cytosolic Sodium', 'ATP_cyt': 'Cytosolic ATP', 'ADP_cyt': 'Cytosolic ADP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_adp': ('ADP_cyt', 3067.9, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP_cyt`.'), 'initial_cytosolic_atp': ('ATP_cyt', 932.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP_cyt`.'), 'initial_cytosolic_sodium': ('Na_cyt', 9858.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Na_cyt`.'), 'initial_er_calcium': ('Ca_er', 22.8, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_er`.'), 'initial_cytosolic_ip3': ('IP3_cyt', 0.33, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IP3_cyt`.'), 'initial_cytosolic_calcium': ('Ca_cyt', 0.085, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_cyt`.')}
    _HEADLINE_OUTPUTS = {'cytosolic_adp': ('ADP_cyt', 'native SBML value', 'Cytosolic ADP. Maps to SBML symbol `ADP_cyt`.'), 'cytosolic_atp': ('ATP_cyt', 'native SBML value', 'Cytosolic ATP. Maps to SBML symbol `ATP_cyt`.'), 'cytosolic_sodium': ('Na_cyt', 'native SBML value', 'Cytosolic Sodium. Maps to SBML symbol `Na_cyt`.'), 'er_calcium': ('Ca_er', 'native SBML value', 'ER Calcium. Maps to SBML symbol `Ca_er`.'), 'cytosolic_ip3': ('IP3_cyt', 'native SBML value', 'Cytosolic IP3. Maps to SBML symbol `IP3_cyt`.'), 'cytosolic_calcium': ('Ca_cyt', 'native SBML value', 'Cytosolic Calcium. Maps to SBML symbol `Ca_cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000059.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
