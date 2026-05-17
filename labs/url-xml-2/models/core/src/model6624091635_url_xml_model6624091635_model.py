# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for MODEL6624091635_url.xml."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Model6624091635UrlXmlModel6624091635Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for MODEL6624091635_url.xml."""

    _SBML_ID = 'MODEL6624091635'
    _TITLE = 'MODEL6624091635_url.xml'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Gluc', 'Lac', 'ACETOUT', 'BUT', 'FR', 'AC', 'ETOH', 'O2', 'UDP', 'TDP', 'Cellwall', 'F6P', 'ATP', 'FBP', 'G3P', 'DHAP', 'NAD', 'DPG', 'P3G', 'P2G', 'PYR', 'COA', 'P', 'ACP', 'ACAL', 'G1P', 'Glucin', 'ACLAC', 'ACET', 'PEP', 'ACCOA', 'ADP', 'NADH', 'G6P']
    _SPECIES_LABELS = {'Gluc': 'Gluc', 'Lac': 'Lac', 'ACETOUT': 'ACETOUT', 'BUT': 'BUT', 'FR': 'FR', 'AC': 'AC', 'ETOH': 'ETOH', 'O2': 'O2', 'UDP': 'UDP', 'TDP': 'TDP', 'Cellwall': 'Cellwall', 'F6P': 'F6P', 'ATP': 'ATP', 'FBP': 'FBP', 'G3P': 'G3P', 'DHAP': 'DHAP', 'NAD': 'NAD', 'DPG': 'DPG', 'P3G': 'P3G', 'P2G': 'P2G', 'PYR': 'PYR', 'COA': 'COA', 'P': 'P', 'ACP': 'ACP', 'ACAL': 'ACAL', 'G1P': 'G1P', 'Glucin': 'Glucin', 'ACLAC': 'ACLAC', 'ACET': 'ACET', 'PEP': 'PEP', 'ACCOA': 'ACCOA', 'ADP': 'ADP', 'NADH': 'NADH', 'G6P': 'G6P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_nad': ('NAD', 5.2, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NAD`.'), 'initial_model_state_atp': ('ATP', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 5.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_nadh': ('NADH', 0.35, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADH`.'), 'initial_acal': ('ACAL', 0.11, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ACAL`.'), 'initial_cellwall': ('Cellwall', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Cellwall`.')}
    _HEADLINE_OUTPUTS = {'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'acal': ('ACAL', 'native SBML value', 'ACAL. Maps to SBML symbol `ACAL`.'), 'cellwall': ('Cellwall', 'native SBML value', 'Cellwall. Maps to SBML symbol `Cellwall`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6624091635.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
