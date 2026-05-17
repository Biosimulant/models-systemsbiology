# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mothes2020_NFkB_A20_signaling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mothes2020NfkbA20SignalingModel2307110001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mothes2020_NFkB_A20_signaling."""

    _SBML_ID = 'MODEL2307110001'
    _TITLE = 'Mothes2020_NFkB_A20_signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A20_mRNA', 'NFkB', 'A20', 'IkBa', 'IkBa_mRNA', 'NFkB_IkBa', 'IKK_active']
    _SPECIES_LABELS = {'A20_mRNA': 'A20 MRNA', 'NFkB': 'NFkB', 'A20': 'A20', 'IkBa': 'IkBa', 'IkBa_mRNA': 'IkBa MRNA', 'NFkB_IkBa': 'NFkB IkBa', 'IKK_active': 'IKK Active'}
    _PARAMETER_INPUTS = {'stimulus': ('stimulus', 1.0, 'dimensionless', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `stimulus`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'a20_mrna': ('A20_mRNA', 'native SBML value', 'A20 MRNA. Maps to SBML symbol `A20_mRNA`.'), 'ik_ba_mrna': ('IkBa_mRNA', 'native SBML value', 'IkBa MRNA. Maps to SBML symbol `IkBa_mRNA`.'), 'n_fk_b_ik_ba': ('NFkB_IkBa', 'native SBML value', 'NFkB IkBa. Maps to SBML symbol `NFkB_IkBa`.'), 'ik_ba': ('IkBa', 'native SBML value', 'IkBa. Maps to SBML symbol `IkBa`.'), 'a20': ('A20', 'native SBML value', 'A20. Maps to SBML symbol `A20`.'), 'ikk_active': ('IKK_active', 'native SBML value', 'IKK Active. Maps to SBML symbol `IKK_active`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2307110001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
