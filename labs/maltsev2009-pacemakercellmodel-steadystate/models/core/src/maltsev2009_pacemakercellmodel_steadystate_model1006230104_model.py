# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Maltsev2009_PacemakerCellModel_SteadyState."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Maltsev2009PacemakercellmodelSteadystateModel1006230104Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Maltsev2009_PacemakerCellModel_SteadyState."""

    _SBML_ID = 'MODEL1006230104'
    _TITLE = 'Maltsev2009_PacemakerCellModel_SteadyState'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Vm_Vm', 'dL', 'fL', 'fCa', 'dT', 'fT', 'paS', 'paF', 'pi_', 'n', 'q', 'r', 'y', 'qa', 'qi', 'R_j_SRCarel', 'O', 'I', 'RI', 'fTC', 'fTMC', 'fTMM', 'fCMi', 'fCMs', 'fCQ', 'Cai', 'Ca_sub_calcium_dynamics', 'Ca_nsr', 'Ca_jsr']
    _SPECIES_LABELS = {'Vm_Vm': 'Vm Vm', 'dL': 'DL', 'fL': 'FL', 'fCa': 'FCa', 'dT': 'DT', 'fT': 'FT', 'paS': 'PaS', 'paF': 'PaF', 'pi_': 'Pi', 'n': 'N', 'q': 'Q', 'r': 'R', 'y': 'Y', 'qa': 'Qa', 'qi': 'Qi', 'R_j_SRCarel': 'R J SRCarel', 'O': 'O', 'I': 'I', 'RI': 'RI', 'fTC': 'FTC', 'fTMC': 'FTMC', 'fTMM': 'FTMM', 'fCMi': 'FCMi', 'fCMs': 'FCMs', 'fCQ': 'FCQ', 'Cai': 'Cai', 'Ca_sub_calcium_dynamics': 'Ca Sub Calcium Dynamics', 'Ca_nsr': 'Ca Nsr', 'Ca_jsr': 'Ca Jsr'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vm_vm': ('Vm_Vm', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm_Vm`.'), 'initial_model_state_ri': ('RI', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI`.'), 'initial_r_j_sr_carel': ('R_j_SRCarel', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_j_SRCarel`.'), 'initial_model_state_qi': ('qi', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `qi`.'), 'initial_model_state_qa': ('qa', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `qa`.'), 'initial_model_state_pi': ('pi_', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pi_`.')}
    _HEADLINE_OUTPUTS = {'vm_vm': ('Vm_Vm', 'native SBML value', 'Vm Vm. Maps to SBML symbol `Vm_Vm`.'), 'model_state_ri': ('RI', 'native SBML value', 'RI. Maps to SBML symbol `RI`.'), 'r_j_sr_carel': ('R_j_SRCarel', 'native SBML value', 'R J SRCarel. Maps to SBML symbol `R_j_SRCarel`.'), 'model_state_qi': ('qi', 'native SBML value', 'Qi. Maps to SBML symbol `qi`.'), 'model_state_qa': ('qa', 'native SBML value', 'Qa. Maps to SBML symbol `qa`.'), 'model_state_pi': ('pi_', 'native SBML value', 'Pi. Maps to SBML symbol `pi_`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230104.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
