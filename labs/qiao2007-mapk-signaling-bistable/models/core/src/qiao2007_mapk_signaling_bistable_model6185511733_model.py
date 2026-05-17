# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Qiao2007_MAPK_Signaling_Bistable."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Qiao2007MapkSignalingBistableModel6185511733Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Qiao2007_MAPK_Signaling_Bistable."""

    _SBML_ID = 'MODEL6185511733'
    _TITLE = 'Qiao2007_MAPK_Signaling_Bistable'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['K', 'KKPP', 'KKKPP', 'KP', 'KPase', 'KPKPase', 'KPKKPP', 'KPP', 'KPPKPase']
    _SPECIES_LABELS = {'K': 'K', 'KKPP': 'KKPP', 'KKKPP': 'KKKPP', 'KP': 'KP', 'KPase': 'KPase', 'KPKPase': 'KPKPase', 'KPKKPP': 'KPKKPP', 'KPP': 'KPP', 'KPPKPase': 'KPPKPase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_kpp': ('KPP', 0.96691587903, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPP`.'), 'initial_kkpp': ('KKPP', 0.39984600804, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKPP`.'), 'initial_k_pase': ('KPase', 0.2774315895, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPase`.'), 'initial_kppk_pase': ('KPPKPase', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPPKPase`.'), 'initial_kpk_pase': ('KPKPase', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPKPase`.'), 'initial_kpkkpp': ('KPKKPP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPKKPP`.')}
    _HEADLINE_OUTPUTS = {'kpp': ('KPP', 'native SBML value', 'KPP. Maps to SBML symbol `KPP`.'), 'kkpp': ('KKPP', 'native SBML value', 'KKPP. Maps to SBML symbol `KKPP`.'), 'k_pase': ('KPase', 'native SBML value', 'KPase. Maps to SBML symbol `KPase`.'), 'kppk_pase': ('KPPKPase', 'native SBML value', 'KPPKPase. Maps to SBML symbol `KPPKPase`.'), 'kpk_pase': ('KPKPase', 'native SBML value', 'KPKPase. Maps to SBML symbol `KPKPase`.'), 'kpkkpp': ('KPKKPP', 'native SBML value', 'KPKKPP. Maps to SBML symbol `KPKKPP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6185511733.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
