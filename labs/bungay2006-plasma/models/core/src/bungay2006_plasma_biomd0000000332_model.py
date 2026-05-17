# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Bungay2006_Plasma."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bungay2006PlasmaBiomd0000000332Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Bungay2006_Plasma."""

    _SBML_ID = 'BIOMD0000000332'
    _TITLE = 'Bungay2006_Plasma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['II_f', 'II_l', 'mIIa_f', 'mIIa_l', 'V_f', 'V_l', 'Va_f', 'Va_l', 'VII_f', 'VII_l', 'VIIa_f', 'VIIa_l', 'VIII_f', 'VIII_l', 'VIIIa_f', 'VIIIa_l', 'IX_f', 'IX_l', 'IXa_f', 'IXa_l', 'X_f', 'X_l', 'Xa_f', 'Xa_l', 'APC_f', 'APC_l', 'PS_f', 'PS_l', 'VIIIai_f', 'VIIIai_l', 'Vai_f', 'Vai_l', 'PC_f', 'PC_l', 'TF_l', 'TF_VIIa_l', 'TF_VII_l', 'TF_VIIa_IX_l', 'TF_VIIa_IXa_l', 'TF_VIIa_X_l', 'TF_VIIa_Xa_l', 'TF_VII_Xa_l', 'IXa_VIIIa_l', 'Xa_Va_l', 'IXa_VIIIa_X_l', 'V_Xa_l', 'VIII_Xa_l', 'IIa_f', 'V_IIa_l', 'VIII_IIa_l', 'Xa_Va_II_l', 'Xa_Va_mIIa_l', 'XI_f', 'XI_IIa_l', 'XIa_l', 'APC_PS_l', 'APC_PS_VIIIa_l', 'TFPI_f', 'AT_f', 'IIa_AT_f', 'TFPI_Xa_l', 'TFPI_Xa_TF_VIIa_l', 'APC_PS_Va_l', 'IXa_AT_f', 'Xa_AT_f', 'VII_Xa_l', 'V_mIIa_l', 'VIII_mIIa_l', 'TM_l', 'IIa_TM_l', 'IIa_TM_PC_l', 'mIIa_AT_l', 'XIa_IX_l', 'LIPID', 'alpha2M_l', 'alpha2M_IIa_l', 'alpha2M_Xa_l', 'AT_XIa_l']
    _SPECIES_LABELS = {'II_f': 'II_f', 'II_l': 'II_l', 'mIIa_f': 'mIIa_f', 'mIIa_l': 'mIIa_l', 'V_f': 'V_f', 'V_l': 'V_l', 'Va_f': 'Va_f', 'Va_l': 'Va_l', 'VII_f': 'VII_f', 'VII_l': 'VII_l', 'VIIa_f': 'VIIa_f', 'VIIa_l': 'VIIa_l', 'VIII_f': 'VIII_f', 'VIII_l': 'VIII_l', 'VIIIa_f': 'VIIIa_f', 'VIIIa_l': 'VIIIa_l', 'IX_f': 'IX_f', 'IX_l': 'IX_l', 'IXa_f': 'IXa_f', 'IXa_l': 'IXa_l', 'X_f': 'X_f', 'X_l': 'X_l', 'Xa_f': 'Xa_f', 'Xa_l': 'Xa_l', 'APC_f': 'APC_f', 'APC_l': 'APC_l', 'PS_f': 'PS_f', 'PS_l': 'PS_l', 'VIIIai_f': 'VIIIai_f', 'VIIIai_l': 'VIIIai_l', 'Vai_f': 'Vai_f', 'Vai_l': 'Vai_l', 'PC_f': 'PC_f', 'PC_l': 'PC_l', 'TF_l': 'TF_l', 'TF_VIIa_l': 'TF_VIIa_l', 'TF_VII_l': 'TF_VII_l', 'TF_VIIa_IX_l': 'TF_VIIa_IX_l', 'TF_VIIa_IXa_l': 'TF_VIIa_IXa_l', 'TF_VIIa_X_l': 'TF_VIIa_X_l', 'TF_VIIa_Xa_l': 'TF_VIIa_Xa_l', 'TF_VII_Xa_l': 'TF_VII_Xa_l', 'IXa_VIIIa_l': 'IXa_VIIIa_l', 'Xa_Va_l': 'Xa_Va_l', 'IXa_VIIIa_X_l': 'IXa_VIIIa_X_l', 'V_Xa_l': 'V_Xa_l', 'VIII_Xa_l': 'VIII_Xa_l', 'IIa_f': 'IIa_f', 'V_IIa_l': 'V_IIa_l', 'VIII_IIa_l': 'VIII_IIa_l', 'Xa_Va_II_l': 'Xa_Va_II_l', 'Xa_Va_mIIa_l': 'Xa_Va_mIIa_l', 'XI_f': 'XI_f', 'XI_IIa_l': 'XI_IIa_l', 'XIa_l': 'XIa_l', 'APC_PS_l': 'APC_PS_l', 'APC_PS_VIIIa_l': 'APC_PS_VIIIa_l', 'TFPI_f': 'TFPI_f', 'AT_f': 'AT_f', 'IIa_AT_f': 'IIa_AT_f', 'TFPI_Xa_l': 'TFPI_Xa_l', 'TFPI_Xa_TF_VIIa_l': 'TFPI_Xa_TF_VIIa_l', 'APC_PS_Va_l': 'APC_PS_Va_l', 'IXa_AT_f': 'IXa_AT_f', 'Xa_AT_f': 'Xa_AT_f', 'VII_Xa_l': 'VII_Xa_l', 'V_mIIa_l': 'V_mIIa_l', 'VIII_mIIa_l': 'VIII_mIIa_l', 'TM_l': 'TM_l', 'IIa_TM_l': 'IIa_TM_l', 'IIa_TM_PC_l': 'IIa_TM_PC_l', 'mIIa_AT_l': 'mIIa_AT_l', 'XIa_IX_l': 'XIa_IX_l', 'LIPID': 'LIPID', 'alpha2M_l': 'alpha2M_l', 'alpha2M_IIa_l': 'alpha2M_IIa_l', 'alpha2M_Xa_l': 'alpha2M_Xa_l', 'AT_XIa_l': 'AT_XIa_l'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_at_f': ('AT_f', 3400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `AT_f`.'), 'initial_alpha2_m_l': ('alpha2M_l', 2600.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `alpha2M_l`.'), 'initial_ii_f': ('II_f', 1400.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `II_f`.'), 'initial_ps_f': ('PS_f', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PS_f`.'), 'initial_model_state_x_f': ('X_f', 170.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X_f`.'), 'initial_ix_f': ('IX_f', 90.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IX_f`.')}
    _HEADLINE_OUTPUTS = {'at_f': ('AT_f', 'native SBML value', 'AT_f. Maps to SBML symbol `AT_f`.'), 'alpha2_m_l': ('alpha2M_l', 'native SBML value', 'alpha2M_l. Maps to SBML symbol `alpha2M_l`.'), 'ii_f': ('II_f', 'native SBML value', 'II_f. Maps to SBML symbol `II_f`.'), 'ps_f': ('PS_f', 'native SBML value', 'PS_f. Maps to SBML symbol `PS_f`.'), 'x_f': ('X_f', 'native SBML value', 'X_f. Maps to SBML symbol `X_f`.'), 'ix_f': ('IX_f', 'native SBML value', 'IX_f. Maps to SBML symbol `IX_f`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000332.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
