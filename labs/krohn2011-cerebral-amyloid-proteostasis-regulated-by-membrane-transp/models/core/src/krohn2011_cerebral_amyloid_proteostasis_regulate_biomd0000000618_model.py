# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Krohn2011 - Cerebral amyloid-β proteostasis regulated by membrane transport protein ABCC1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Krohn2011CerebralAmyloidProteostasisRegulateBiomd0000000618Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Krohn2011 - Cerebral amyloid-β proteostasis regulated by membrane transport protein ABCC1."""

    _SBML_ID = 'BIOMD0000000618'
    _TITLE = 'Krohn2011 - Cerebral amyloid-β proteostasis regulated by membrane transport protein ABCC1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'N', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A50', 'A51', 'A52', 'A53', 'A54', 'soluble_obs', 'insoluble_obs']
    _SPECIES_LABELS = {'M': 'M', 'N': 'N', 'A7': 'A7', 'A8': 'A8', 'A9': 'A9', 'A10': 'A10', 'A11': 'A11', 'A12': 'A12', 'A13': 'A13', 'A14': 'A14', 'A15': 'A15', 'A16': 'A16', 'A17': 'A17', 'A18': 'A18', 'A19': 'A19', 'A20': 'A20', 'A21': 'A21', 'A22': 'A22', 'A23': 'A23', 'A24': 'A24', 'A25': 'A25', 'A26': 'A26', 'A27': 'A27', 'A28': 'A28', 'A29': 'A29', 'A30': 'A30', 'A31': 'A31', 'A32': 'A32', 'A33': 'A33', 'A34': 'A34', 'A35': 'A35', 'A36': 'A36', 'A37': 'A37', 'A38': 'A38', 'A39': 'A39', 'A40': 'A40', 'A41': 'A41', 'A42': 'A42', 'A43': 'A43', 'A44': 'A44', 'A45': 'A45', 'A46': 'A46', 'A47': 'A47', 'A48': 'A48', 'A49': 'A49', 'A50': 'A50', 'A51': 'A51', 'A52': 'A52', 'A53': 'A53', 'A54': 'A54', 'soluble_obs': 'soluble_obs', 'insoluble_obs': 'insoluble_obs'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_soluble_obs': ('soluble_obs', 1.04389999999997, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `soluble_obs`.'), 'initial_insoluble_obs': ('insoluble_obs', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `insoluble_obs`.'), 'initial_model_state_a9': ('A9', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A9`.'), 'initial_model_state_a8': ('A8', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A8`.'), 'initial_model_state_a7': ('A7', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A7`.'), 'initial_model_state_a54': ('A54', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A54`.')}
    _HEADLINE_OUTPUTS = {'soluble_obs': ('soluble_obs', 'native SBML value', 'soluble_obs. Maps to SBML symbol `soluble_obs`.'), 'insoluble_obs': ('insoluble_obs', 'native SBML value', 'insoluble_obs. Maps to SBML symbol `insoluble_obs`.'), 'model_state_a9': ('A9', 'native SBML value', 'A9. Maps to SBML symbol `A9`.'), 'model_state_a8': ('A8', 'native SBML value', 'A8. Maps to SBML symbol `A8`.'), 'model_state_a7': ('A7', 'native SBML value', 'A7. Maps to SBML symbol `A7`.'), 'a54': ('A54', 'native SBML value', 'A54. Maps to SBML symbol `A54`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000618.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
