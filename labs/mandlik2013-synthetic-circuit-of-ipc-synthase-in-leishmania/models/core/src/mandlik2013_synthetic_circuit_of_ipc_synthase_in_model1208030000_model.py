# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mandlik2013 - Synthetic circuit of IPC synthase in Leishmania."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mandlik2013SyntheticCircuitOfIpcSynthaseInModel1208030000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mandlik2013 - Synthetic circuit of IPC synthase in Leishmania."""

    _SBML_ID = 'MODEL1208030000'
    _TITLE = 'Mandlik2013 - Synthetic circuit of IPC synthase in Leishmania'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IPCS1protein', 'IPCS2protein', 'IPCS_1', 'IPCS_2', 'TetrRepressor', 'Tetrgene', 'lacI', 'lactoserepressor', 'lamdar', 'lamdarepressor', 'rp1', 'rp2', 'rp3', 'rp4', 'rp5', 'rs1']
    _SPECIES_LABELS = {'IPCS1protein': 'IPCS1protein', 'IPCS2protein': 'IPCS2protein', 'IPCS_1': 'IPCS_1', 'IPCS_2': 'IPCS_2', 'TetrRepressor': 'TetrRepressor', 'Tetrgene': 'Tetrgene', 'lacI': 'lacI', 'lactoserepressor': 'lactoserepressor', 'lamdar': 'lamdar', 'lamdarepressor': 'lamdarepressor', 'rp1': 'rp1', 'rp2': 'rp2', 'rp3': 'rp3', 'rp4': 'rp4', 'rp5': 'rp5', 'rs1': 'rs1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_rs1': ('rs1', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rs1`.'), 'initial_model_state_rp5': ('rp5', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rp5`.'), 'initial_model_state_rp4': ('rp4', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rp4`.'), 'initial_model_state_rp3': ('rp3', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rp3`.'), 'initial_model_state_rp2': ('rp2', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rp2`.'), 'initial_model_state_rp1': ('rp1', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rp1`.')}
    _HEADLINE_OUTPUTS = {'rs1': ('rs1', 'native SBML value', 'rs1. Maps to SBML symbol `rs1`.'), 'rp5': ('rp5', 'native SBML value', 'rp5. Maps to SBML symbol `rp5`.'), 'rp4': ('rp4', 'native SBML value', 'rp4. Maps to SBML symbol `rp4`.'), 'rp3': ('rp3', 'native SBML value', 'rp3. Maps to SBML symbol `rp3`.'), 'rp2': ('rp2', 'native SBML value', 'rp2. Maps to SBML symbol `rp2`.'), 'rp1': ('rp1', 'native SBML value', 'rp1. Maps to SBML symbol `rp1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1208030000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
