# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Akman2008_Circadian_Clock_Model2."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Akman2008CircadianClockModel2Biomd0000000214Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Akman2008_Circadian_Clock_Model2."""

    _SBML_ID = 'BIOMD0000000214'
    _TITLE = 'Akman2008_Circadian_Clock_Model2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E1F', 'E1Fp', 'E1W', 'E2F', 'E2Fp', 'E2W', 'MF', 'MW', 'PF', 'PFp', 'PW', 'PWL', 'sFrq_tot', 'lFrq_tot', 'Frq_tot', 'WC1_tot']
    _SPECIES_LABELS = {'E1F': 's-Frq_1', 'E1Fp': 'l-Frq_1', 'E1W': 'WC-1_1', 'E2F': 's-Frq_2', 'E2Fp': 'l-Frq_2', 'E2W': 'WC-1_2', 'MF': 'Frq mRNA', 'MW': 'WC-1 mRNA', 'PF': 's-Frq', 'PFp': 'l-Frq', 'PW': 'WC-1', 'PWL': 'WC-1*', 'sFrq_tot': 'tot s-Frq', 'lFrq_tot': 'tot l-Frq', 'Frq_tot': 'tot Frq', 'WC1_tot': 'tot WC-1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_wc_1_mrna': ('MW', 1.2689, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MW`.'), 'initial_frq_mrna': ('MF', 0.6935, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MF`.'), 'initial_wc_1': ('PW', 26.4393, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PW`.'), 'initial_wc_1_1': ('E1W', 5.84748, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E1W`.'), 'initial_wc_1_2': ('E2W', 5.70265, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2W`.'), 'initial_l_frq_1': ('E1Fp', 0.45583, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E1Fp`.')}
    _HEADLINE_OUTPUTS = {'wc_1_mrna': ('MW', 'native SBML value', 'WC-1 mRNA. Maps to SBML symbol `MW`.'), 'frq_mrna': ('MF', 'native SBML value', 'Frq mRNA. Maps to SBML symbol `MF`.'), 'wc_1': ('PW', 'native SBML value', 'WC-1. Maps to SBML symbol `PW`.'), 'wc_1_1': ('E1W', 'native SBML value', 'WC-1_1. Maps to SBML symbol `E1W`.'), 'wc_1_2': ('E2W', 'native SBML value', 'WC-1_2. Maps to SBML symbol `E2W`.'), 'l_frq_1': ('E1Fp', 'native SBML value', 'l-Frq_1. Maps to SBML symbol `E1Fp`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000214.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
