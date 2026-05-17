# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Qiao2007_MAPK_Signaling_Oscillatory."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Qiao2007MapkSignalingOscillatoryModel6185746832Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Qiao2007_MAPK_Signaling_Oscillatory."""

    _SBML_ID = 'MODEL6185746832'
    _TITLE = 'Qiao2007_MAPK_Signaling_Oscillatory'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['KKK', 'E1', 'KKKE1', 'KKKS', 'E2', 'KKKSE2', 'KK', 'KK_KKKS', 'KKP', 'KKPase', 'KKPKKPase', 'KKPKKKS', 'KKPP', 'KKPPKKPase']
    _SPECIES_LABELS = {'KKK': 'KKK', 'E1': 'E1', 'KKKE1': 'KKKE1', 'KKKS': 'KKKS', 'E2': 'E2', 'KKKSE2': 'KKKSE2', 'KK': 'KK', 'KK_KKKS': 'KK KKKS', 'KKP': 'KKP', 'KKPase': 'KKPase', 'KKPKKPase': 'KKPKKPase', 'KKPKKKS': 'KKPKKKS', 'KKPP': 'KKPP', 'KKPPKKPase': 'KKPPKKPase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_kkpp': ('KKPP', 3.74917682536, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKPP`.'), 'initial_kkks': ('KKKS', 0.00743468337, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKKS`.'), 'initial_kk_pase': ('KKPase', 0.00119813544, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKPase`.'), 'initial_model_state_e2': ('E2', 0.00011836217, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2`.'), 'initial_model_state_e1': ('E1', 6.30957e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E1`.'), 'initial_kkppkk_pase': ('KKPPKKPase', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKPPKKPase`.')}
    _HEADLINE_OUTPUTS = {'kkpp': ('KKPP', 'native SBML value', 'KKPP. Maps to SBML symbol `KKPP`.'), 'kkks': ('KKKS', 'native SBML value', 'KKKS. Maps to SBML symbol `KKKS`.'), 'kk_pase': ('KKPase', 'native SBML value', 'KKPase. Maps to SBML symbol `KKPase`.'), 'model_state_e2': ('E2', 'native SBML value', 'E2. Maps to SBML symbol `E2`.'), 'model_state_e1': ('E1', 'native SBML value', 'E1. Maps to SBML symbol `E1`.'), 'kkppkk_pase': ('KKPPKKPase', 'native SBML value', 'KKPPKKPase. Maps to SBML symbol `KKPPKKPase`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6185746832.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
