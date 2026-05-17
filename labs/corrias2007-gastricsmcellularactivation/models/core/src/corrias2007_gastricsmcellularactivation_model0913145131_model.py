# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Corrias2007_GastricSMCellularActivation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Corrias2007GastricsmcellularactivationModel0913145131Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Corrias2007_GastricSMCellularActivation."""

    _SBML_ID = 'MODEL0913145131'
    _TITLE = 'Corrias2007_GastricSMCellularActivation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Vm_SM', 'Ca_i', 'd_Ltype_SM', 'f_Ltype_SM', 'f_ca_Ltype_SM', 'd_LVA_SM', 'f_LVA_SM', 'xr1_SM', 'xr2_SM', 'm_Na_SM', 'h_Na_SM', 'xa1_SM', 'xa2_SM', 'm_NSCC_SM']
    _SPECIES_LABELS = {'Vm_SM': 'Vm SM', 'Ca_i': 'Ca I', 'd_Ltype_SM': 'D Ltype SM', 'f_Ltype_SM': 'F Ltype SM', 'f_ca_Ltype_SM': 'F Ca Ltype SM', 'd_LVA_SM': 'D LVA SM', 'f_LVA_SM': 'F LVA SM', 'xr1_SM': 'XR1 SM', 'xr2_SM': 'XR2 SM', 'm_Na_SM': 'M Na SM', 'h_Na_SM': 'H Na SM', 'xa1_SM': 'XA1 SM', 'xa2_SM': 'XA2 SM', 'm_NSCC_SM': 'M NSCC SM'}
    _PARAMETER_INPUTS = {'t_icc_stimulus': ('t_ICC_stimulus', 10000.0, 'time_units', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `t_ICC_stimulus`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'xr2_sm': ('xr2_SM', 'native SBML value', 'XR2 SM. Maps to SBML symbol `xr2_SM`.'), 'xr1_sm': ('xr1_SM', 'native SBML value', 'XR1 SM. Maps to SBML symbol `xr1_SM`.'), 'xa2_sm': ('xa2_SM', 'native SBML value', 'XA2 SM. Maps to SBML symbol `xa2_SM`.'), 'xa1_sm': ('xa1_SM', 'native SBML value', 'XA1 SM. Maps to SBML symbol `xa1_SM`.'), 'vm_sm': ('Vm_SM', 'native SBML value', 'Vm SM. Maps to SBML symbol `Vm_SM`.'), 'm_na_sm': ('m_Na_SM', 'native SBML value', 'M Na SM. Maps to SBML symbol `m_Na_SM`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0913145131.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
