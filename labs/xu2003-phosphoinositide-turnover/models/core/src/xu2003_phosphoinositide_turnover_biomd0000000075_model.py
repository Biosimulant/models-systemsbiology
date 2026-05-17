# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Xu2003 - Phosphoinositide turnover."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Xu2003PhosphoinositideTurnoverBiomd0000000075Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Xu2003 - Phosphoinositide turnover."""

    _SBML_ID = 'BIOMD0000000075'
    _TITLE = 'Xu2003 - Phosphoinositide turnover'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PIP2_PHGFP_PM', 'PH_GFP_Cyt', 'PI_PM', 'stim_PM', 'IP3_PHGFP_Cyt', 'PIP2_PM', 'PIP_PM', 'DAG_PM', 'hv_Cytosol', 'IP3X_Cytosol', 'PLC_PM', 'PLC_act_PM', 'IP3_Cyt']
    _SPECIES_LABELS = {'PIP2_PHGFP_PM': 'PIP2_PHGFP_PM', 'PH_GFP_Cyt': 'PH_GFP_Cyt', 'PI_PM': 'PI_PM', 'stim_PM': 'stim_PM', 'IP3_PHGFP_Cyt': 'IP3_PHGFP_Cyt', 'PIP2_PM': 'PIP2_PM', 'PIP_PM': 'PIP_PM', 'DAG_PM': 'DAG_PM', 'hv_Cytosol': 'hv_Cytosol', 'IP3X_Cytosol': 'IP3X_Cytosol', 'PLC_PM': 'PLC_PM', 'PLC_act_PM': 'PLC_act_PM', 'IP3_Cyt': 'IP3_Cyt'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pi_pm': ('PI_PM', 142857.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI_PM`.'), 'initial_pip2_pm': ('PIP2_PM', 4000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP2_PM`.'), 'initial_pip_pm': ('PIP_PM', 2857.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP_PM`.'), 'initial_dag_pm': ('DAG_PM', 2000.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DAG_PM`.'), 'initial_plc_pm': ('PLC_PM', 100.0, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PLC_PM`.'), 'initial_ip3_cyt': ('IP3_Cyt', 96.32, 'substance', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IP3_Cyt`.')}
    _HEADLINE_OUTPUTS = {'pi_pm': ('PI_PM', 'substance', 'PI_PM. Maps to SBML symbol `PI_PM`.'), 'pip2_pm': ('PIP2_PM', 'substance', 'PIP2_PM. Maps to SBML symbol `PIP2_PM`.'), 'pip_pm': ('PIP_PM', 'substance', 'PIP_PM. Maps to SBML symbol `PIP_PM`.'), 'dag_pm': ('DAG_PM', 'substance', 'DAG_PM. Maps to SBML symbol `DAG_PM`.'), 'plc_pm': ('PLC_PM', 'substance', 'PLC_PM. Maps to SBML symbol `PLC_PM`.'), 'ip3_cyt': ('IP3_Cyt', 'substance', 'IP3_Cyt. Maps to SBML symbol `IP3_Cyt`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000075.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
