# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mazet2020 - model of the PI cycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mazet2020ModelOfThePiCycleModel2006300001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mazet2020 - model of the PI cycle."""

    _SBML_ID = 'MODEL2006300001'
    _TITLE = 'Mazet2020 - model of the PI cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PI', 'PI4K', 'PIP2', 'OCRL1', 'Ins', 'PLC', 'CDIPT', 'PLCa', 'PI4Ka', 'PIP2_PLB', 'PLB', 'PA', 'AA', 'PLA2', 'PA_PABP', 'PABP', 'smGa', 'smG', 'L_GPCR', 'RGi', 'PLA2a', 'DAG', 'IP3', 'DGK', 'IPx', 'IP3E', 'LPP', 'OCRL1a', 'PI4P', 'SAC1', 'PIP5Ka', 'PIP5K', 'P4BP', 'PI4P_P4BP', 'R', 'Ra', 'Gq', 'RGq', 'G13', 'RG13', 'AC', 'DAG_BP', 'DAGBP']
    _SPECIES_LABELS = {'PI': 'PI', 'PI4K': 'PI4K', 'PIP2': 'PIP2', 'OCRL1': 'OCRL1', 'Ins': 'Ins', 'PLC': 'PLC', 'CDIPT': 'CDIPT', 'PLCa': 'PLCa', 'PI4Ka': 'PI4Ka', 'PIP2_PLB': 'PIP2.PLB', 'PLB': 'PLB', 'PA': 'PA', 'AA': 'AA', 'PLA2': 'PLA2', 'PA_PABP': 'PA.PABP', 'PABP': 'PABP', 'smGa': 'smGa', 'smG': 'smG', 'L_GPCR': 'L.GPCR', 'RGi': 'RGi', 'PLA2a': 'PLA2a', 'DAG': 'DAG', 'IP3': 'IP3', 'DGK': 'DGK', 'IPx': 'IPx', 'IP3E': 'IP3E', 'LPP': 'LPP', 'OCRL1a': 'OCRL1a', 'PI4P': 'PI4P', 'SAC1': 'SAC1', 'PIP5Ka': 'PIP5Ka', 'PIP5K': 'PIP5K', 'P4BP': 'P4BP', 'PI4P_P4BP': 'PI4P.P4BP', 'R': 'R', 'Ra': 'Ra', 'Gq': 'Gq', 'RGq': 'RGq', 'G13': 'G13', 'RG13': 'RG13', 'AC': 'AC', 'DAG_BP': 'DAG.BP', 'DAGBP': 'DAGBP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pi4_p_p4_bp': ('PI4P_P4BP', 1172500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI4P_P4BP`.'), 'initial_pip2_plb': ('PIP2_PLB', 844497.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PIP2_PLB`.'), 'initial_pa_pabp': ('PA_PABP', 161635.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PA_PABP`.'), 'initial_dag_bp': ('DAG_BP', 36470.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `DAG_BP`.'), 'initial_sm_g': ('smG', 20000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `smG`.'), 'initial_sm_ga': ('smGa', 5.83e-12, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `smGa`.')}
    _HEADLINE_OUTPUTS = {'pi4_p_p4_bp': ('PI4P_P4BP', 'native SBML value', 'PI4P.P4BP. Maps to SBML symbol `PI4P_P4BP`.'), 'pip2_plb': ('PIP2_PLB', 'native SBML value', 'PIP2.PLB. Maps to SBML symbol `PIP2_PLB`.'), 'pa_pabp': ('PA_PABP', 'native SBML value', 'PA.PABP. Maps to SBML symbol `PA_PABP`.'), 'dag_bp': ('DAG_BP', 'native SBML value', 'DAG.BP. Maps to SBML symbol `DAG_BP`.'), 'sm_g': ('smG', 'native SBML value', 'smG. Maps to SBML symbol `smG`.'), 'sm_ga': ('smGa', 'native SBML value', 'smGa. Maps to SBML symbol `smGa`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2006300001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
