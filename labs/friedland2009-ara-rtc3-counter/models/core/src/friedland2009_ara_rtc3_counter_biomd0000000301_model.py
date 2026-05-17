# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Friedland2009_Ara_RTC3_counter."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Friedland2009AraRtc3CounterBiomd0000000301Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Friedland2009_Ara_RTC3_counter."""

    _SBML_ID = 'BIOMD0000000301'
    _TITLE = 'Friedland2009_Ara_RTC3_counter'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['taRNA', 'mT7cr', 'mGFPcr', 'pT7', 'pGFP', 'ara', 'pT3', 'mT3cr']
    _SPECIES_LABELS = {'taRNA': 'TaRNA', 'mT7cr': 'MT7cr', 'mGFPcr': 'MGFPcr', 'pT7': 'PT7', 'pGFP': 'PGFP', 'ara': 'Ara', 'pT3': 'PT3', 'mT3cr': 'MT3cr'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pgfp': ('pGFP', 6.338921181, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pGFP`.'), 'initial_mt7cr': ('mT7cr', 0.3569405099, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mT7cr`.'), 'initial_mgf_pcr': ('mGFPcr', 0.176991329, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mGFPcr`.'), 'initial_model_state_pt7': ('pT7', 0.05230744612, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pT7`.'), 'initial_ta_rna': ('taRNA', 0.006796941377, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `taRNA`.'), 'initial_mt3cr': ('mT3cr', 0.00566438, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mT3cr`.')}
    _HEADLINE_OUTPUTS = {'pgfp': ('pGFP', 'native SBML value', 'PGFP. Maps to SBML symbol `pGFP`.'), 'mt7cr': ('mT7cr', 'native SBML value', 'MT7cr. Maps to SBML symbol `mT7cr`.'), 'mgf_pcr': ('mGFPcr', 'native SBML value', 'MGFPcr. Maps to SBML symbol `mGFPcr`.'), 'pt7': ('pT7', 'native SBML value', 'PT7. Maps to SBML symbol `pT7`.'), 'ta_rna': ('taRNA', 'native SBML value', 'TaRNA. Maps to SBML symbol `taRNA`.'), 'mt3cr': ('mT3cr', 'native SBML value', 'MT3cr. Maps to SBML symbol `mT3cr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000301.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
