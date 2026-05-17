# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sen2013 - Phospholipid Synthesis in P.knowlesi."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sen2013PhospholipidSynthesisInPKnowlesiBiomd0000000495Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sen2013 - Phospholipid Synthesis in P.knowlesi."""

    _SBML_ID = 'BIOMD0000000495'
    _TITLE = 'Sen2013 - Phospholipid Synthesis in P.knowlesi'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['mw73259e20_240e_4f3a_b2e0_9ca248658898', 'mw15abaa48_d7d0_4845_ae04_c573d289d495', 'mwfcfaf604_14d4_47a6_b021_226d1fb5497c', 'mw8796c919_9251_4970_8f87_0bca9ecfeb5c', 'mw849ed3fd_87d9_44d2_9f3e_4d631b900d41', 'mwcb834e43_dc57_45ae_9452_f4c10955caf1', 'mwf166ad55_4ff0_49fb_95d2_b657ad7653d5', 'mwee54b5b4_b8c0_41df_8dda_5b160c5e10a5', 'mw919f8a86_e702_4b24_9cd7_adad694fcf9b', 'mw812f63db_4cb0_40ad_b92b_9874be969dfe', 'mw08818dfe_fb12_45cc_8c1d_d965f142d0ce']
    _SPECIES_LABELS = {'mw73259e20_240e_4f3a_b2e0_9ca248658898': 'SerE', 'mw15abaa48_d7d0_4845_ae04_c573d289d495': 'Ser', 'mwfcfaf604_14d4_47a6_b021_226d1fb5497c': 'PS', 'mw8796c919_9251_4970_8f87_0bca9ecfeb5c': 'Etn', 'mw849ed3fd_87d9_44d2_9f3e_4d631b900d41': 'PEtn', 'mwcb834e43_dc57_45ae_9452_f4c10955caf1': 'PCho', 'mwf166ad55_4ff0_49fb_95d2_b657ad7653d5': 'PE', 'mwee54b5b4_b8c0_41df_8dda_5b160c5e10a5': 'PC', 'mw919f8a86_e702_4b24_9cd7_adad694fcf9b': 'ChoE', 'mw812f63db_4cb0_40ad_b92b_9874be969dfe': 'Cho', 'mw08818dfe_fb12_45cc_8c1d_d965f142d0ce': 'EtnE'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ser_e': ('mw73259e20_240e_4f3a_b2e0_9ca248658898', 0.0001, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw73259e20_240e_4f3a_b2e0_9ca248658898`.'), 'initial_p_cho': ('mwcb834e43_dc57_45ae_9452_f4c10955caf1', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mwcb834e43_dc57_45ae_9452_f4c10955caf1`.'), 'initial_model_state_etn': ('mw8796c919_9251_4970_8f87_0bca9ecfeb5c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw8796c919_9251_4970_8f87_0bca9ecfeb5c`.'), 'initial_cho_e': ('mw919f8a86_e702_4b24_9cd7_adad694fcf9b', 5e-05, 'mole', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw919f8a86_e702_4b24_9cd7_adad694fcf9b`.'), 'initial_model_state_ser': ('mw15abaa48_d7d0_4845_ae04_c573d289d495', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mw15abaa48_d7d0_4845_ae04_c573d289d495`.'), 'initial_model_state_ps': ('mwfcfaf604_14d4_47a6_b021_226d1fb5497c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mwfcfaf604_14d4_47a6_b021_226d1fb5497c`.')}
    _HEADLINE_OUTPUTS = {'ser_e': ('mw73259e20_240e_4f3a_b2e0_9ca248658898', 'mole', 'SerE. Maps to SBML symbol `mw73259e20_240e_4f3a_b2e0_9ca248658898`.'), 'p_cho': ('mwcb834e43_dc57_45ae_9452_f4c10955caf1', 'native SBML value', 'PCho. Maps to SBML symbol `mwcb834e43_dc57_45ae_9452_f4c10955caf1`.'), 'etn': ('mw8796c919_9251_4970_8f87_0bca9ecfeb5c', 'native SBML value', 'Etn. Maps to SBML symbol `mw8796c919_9251_4970_8f87_0bca9ecfeb5c`.'), 'cho_e': ('mw919f8a86_e702_4b24_9cd7_adad694fcf9b', 'mole', 'ChoE. Maps to SBML symbol `mw919f8a86_e702_4b24_9cd7_adad694fcf9b`.'), 'ser': ('mw15abaa48_d7d0_4845_ae04_c573d289d495', 'native SBML value', 'Ser. Maps to SBML symbol `mw15abaa48_d7d0_4845_ae04_c573d289d495`.'), 'model_state_ps': ('mwfcfaf604_14d4_47a6_b021_226d1fb5497c', 'native SBML value', 'PS. Maps to SBML symbol `mwfcfaf604_14d4_47a6_b021_226d1fb5497c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000495.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
