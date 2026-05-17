# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lee2016 - Blood Coagulation Model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2016BloodCoagulationModelModel1806060001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lee2016 - Blood Coagulation Model."""

    _SBML_ID = 'MODEL1806060001'
    _TITLE = 'Lee2016 - Blood Coagulation Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FVII', 'TF', 'TF_FVII', 'FVIIa', 'TF_FVIIa', 'FIX', 'TF_FVIIa_FIX', 'TF_FVIIa_FXa', 'FX', 'TF_FVIIa_FX', 'FVIIa_FX', 'FXa', 'FVIII', 'FXa_FVIII', 'FVIIIa', 'F12', 'FII', 'FIIa', 'FIXa', 'FIXa_FVIIIa', 'FIXa_FVIIIa_FX', 'FVIIIa1_L', 'FVIIIa2', 'FV', 'FVa', 'FXa_FVa', 'FXa_FVa_FII', 'mIIa', 'FXa_FVa_mIIa', 'FXa_TFPI', 'TFPI', 'TF_FVIIa_FXa_TFPI', 'CA', 'FXII', 'FXIIa', 'FXIIa_PK', 'PK', 'K', 'FXII_K', 'FXI', 'FXIIa_FXI', 'FXIa', 'FXIa_FIX', 'FIXa_FX', 'FVIIa_CA', 'ATIII', 'TF_FVIIa_ATIII', 'FVIIa_ATIII', 'FIXa_ATIII', 'FXa_ATIII', 'FIIa_ATIII', 'mIIa_ATIII', 'FXIIa_ATIII', 'FXIa_ATIII', 'FIIa_Tmod', 'Tmod', 'FIIa_Tmod_PC', 'PC', 'APC', 'APC_FVa', 'APC_FVIIIa', 'APC_FIXa_FVIIIa', 'APC_FIXa_FVIIIa_FX', 'FIIa_Fg', 'Fg', 'F', 'FIIa_FXIIIa', 'FXIII', 'FXIIIa', 'FXIIIa_F', 'XF', 'Pg', 't_PA', 't_PA_Pg', 'P', 'P_FXIIIa', 'P_Fg', 'FDP', 'P_F', 'P_XF', 'DP']
    _SPECIES_LABELS = {'FVII': 'FVII', 'TF': 'TF', 'TF_FVII': 'TF-FVII', 'FVIIa': 'FVIIa', 'TF_FVIIa': 'TF-FVIIa', 'FIX': 'FIX', 'TF_FVIIa_FIX': 'TF-FVIIa-FIX', 'TF_FVIIa_FXa': 'TF-FVIIa-FXa', 'FX': 'FX', 'TF_FVIIa_FX': 'TF-FVIIa-FX', 'FVIIa_FX': 'FVIIa-FX', 'FXa': 'FXa', 'FVIII': 'FVIII', 'FXa_FVIII': 'FXa-FVIII', 'FVIIIa': 'FVIIIa', 'F12': 'F12', 'FII': 'FII', 'FIIa': 'FIIa', 'FIXa': 'FIXa', 'FIXa_FVIIIa': 'FIXa-FVIIIa', 'FIXa_FVIIIa_FX': 'FIXa-FVIIIa-FX', 'FVIIIa1_L': 'FVIIIa1*L', 'FVIIIa2': 'FVIIIa2', 'FV': 'FV', 'FVa': 'FVa', 'FXa_FVa': 'FXa-FVa', 'FXa_FVa_FII': 'FXa-FVa-FII', 'mIIa': 'mIIa', 'FXa_FVa_mIIa': 'FXa-FVa-mIIa', 'FXa_TFPI': 'FXa-TFPI', 'TFPI': 'TFPI', 'TF_FVIIa_FXa_TFPI': 'TF-FVIIa-FXa-TFPI', 'CA': 'CA', 'FXII': 'FXII', 'FXIIa': 'FXIIa', 'FXIIa_PK': 'FXIIa-PK', 'PK': 'PK', 'K': 'K', 'FXII_K': 'FXII-K', 'FXI': 'FXI', 'FXIIa_FXI': 'FXIIa-FXI', 'FXIa': 'FXIa', 'FXIa_FIX': 'FXIa-FIX', 'FIXa_FX': 'FIXa-FX', 'FVIIa_CA': 'FVIIa-CA', 'ATIII': 'ATIII', 'TF_FVIIa_ATIII': 'TF-FVIIa-ATIII', 'FVIIa_ATIII': 'FVIIa-ATIII', 'FIXa_ATIII': 'FIXa-ATIII', 'FXa_ATIII': 'FXa-ATIII', 'FIIa_ATIII': 'FIIa-ATIII', 'mIIa_ATIII': 'mIIa-ATIII', 'FXIIa_ATIII': 'FXIIa-ATIII', 'FXIa_ATIII': 'FXIa-ATIII', 'FIIa_Tmod': 'FIIa-Tmod', 'Tmod': 'Tmod', 'FIIa_Tmod_PC': 'FIIa-Tmod-PC', 'PC': 'PC', 'APC': 'APC', 'APC_FVa': 'APC-FVa', 'APC_FVIIIa': 'APC-FVIIIa', 'APC_FIXa_FVIIIa': 'APC-FIXa-FVIIIa', 'APC_FIXa_FVIIIa_FX': 'APC-FIXa-FVIIIa-FX', 'FIIa_Fg': 'FIIa-Fg', 'Fg': 'Fg', 'F': 'F', 'FIIa_FXIIIa': 'FIIa-FXIIIa', 'FXIII': 'FXIII', 'FXIIIa': 'FXIIIa', 'FXIIIa_F': 'FXIIIa-F', 'XF': 'XF', 'Pg': 'Pg', 't_PA': 't-PA', 't_PA_Pg': 't-PA-Pg', 'P': 'P', 'P_FXIIIa': 'P-FXIIIa', 'P_Fg': 'P-Fg', 'FDP': 'FDP', 'P_F': 'P-F', 'P_XF': 'P-XF', 'DP': 'DP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p_fg': ('P_Fg', 75.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_Fg`.'), 'initial_t_pa_pg': ('t_PA_Pg', 4.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `t_PA_Pg`.'), 'initial_t_pa': ('t_PA', 0.1449, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `t_PA`.'), 'initial_model_state_p_f': ('P_F', 0.09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_F`.'), 'initial_p_xf': ('P_XF', 5.48e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P_XF`.'), 'initial_tf_fvii': ('TF_FVII', 8.87e-10, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF_FVII`.')}
    _HEADLINE_OUTPUTS = {'p_fg': ('P_Fg', 'native SBML value', 'P-Fg. Maps to SBML symbol `P_Fg`.'), 't_pa_pg': ('t_PA_Pg', 'native SBML value', 't-PA-Pg. Maps to SBML symbol `t_PA_Pg`.'), 't_pa': ('t_PA', 'native SBML value', 't-PA. Maps to SBML symbol `t_PA`.'), 'p_f': ('P_F', 'native SBML value', 'P-F. Maps to SBML symbol `P_F`.'), 'p_xf': ('P_XF', 'native SBML value', 'P-XF. Maps to SBML symbol `P_XF`.'), 'tf_fvii': ('TF_FVII', 'native SBML value', 'TF-FVII. Maps to SBML symbol `TF_FVII`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1806060001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
