# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for A quantitative model of the initiation of DNA replication in Saccharomyces cerevisiae predicts the effects of system perturbations."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AQuantitativeModelOfTheInitiationOfDnaReModel1812050001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for A quantitative model of the initiation of DNA replication in Saccharomyces cerevisiae predicts the effects of system perturbations."""

    _SBML_ID = 'MODEL1812050001'
    _TITLE = 'A quantitative model of the initiation of DNA replication in Saccharomyces cerevisiae predicts the effects of system perturbations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CDC6', 'DBF4', 'ORC', 'ORC_CDC6', 'CDT1', 'MCM', 'MCM_CDT1', 'ORC_CDC6_MCM', 'ORC_MCM', 'ORC_MCM_DBF4', 'CDC45', 'ORC_MCM_DBF4_CDC45', 'CDC45_MCM', 'ORC_P', 'ORC_Total', 'CDT1_Total', 'MCM_Total', 'CDC45_Total', 'CDT1c', 'MCMc', 'CLB5']
    _SPECIES_LABELS = {'CDC6': 'CDC6', 'DBF4': 'DBF4', 'ORC': 'ORC', 'ORC_CDC6': 'ORC_CDC6', 'CDT1': 'CDT1', 'MCM': 'MCM', 'MCM_CDT1': 'MCM_CDT1', 'ORC_CDC6_MCM': 'ORC_CDC6_MCM', 'ORC_MCM': 'ORC_MCM', 'ORC_MCM_DBF4': 'ORC_MCM_DBF4', 'CDC45': 'CDC45', 'ORC_MCM_DBF4_CDC45': 'ORC_MCM_DBF4_CDC45', 'CDC45_MCM': 'CDC45_MCM', 'ORC_P': 'ORC_P', 'ORC_Total': 'ORC-Total', 'CDT1_Total': 'CDT1-Total', 'MCM_Total': 'MCM-Total', 'CDC45_Total': 'CDC45-Total', 'CDT1c': 'CDT1c', 'MCMc': 'MCMc', 'CLB5': 'CLB5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_orc_total': ('ORC_Total', 332.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ORC_Total`.'), 'initial_mcm_total': ('MCM_Total', 332.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MCM_Total`.'), 'initial_cdt1_total': ('CDT1_Total', 332.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CDT1_Total`.'), 'initial_cdc45_total': ('CDC45_Total', 332.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CDC45_Total`.'), 'initial_orc_p': ('ORC_P', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ORC_P`.'), 'initial_orc_mcm_dbf4_cdc45': ('ORC_MCM_DBF4_CDC45', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ORC_MCM_DBF4_CDC45`.')}
    _HEADLINE_OUTPUTS = {'orc_total': ('ORC_Total', 'native SBML value', 'ORC-Total. Maps to SBML symbol `ORC_Total`.'), 'mcm_total': ('MCM_Total', 'native SBML value', 'MCM-Total. Maps to SBML symbol `MCM_Total`.'), 'cdt1_total': ('CDT1_Total', 'native SBML value', 'CDT1-Total. Maps to SBML symbol `CDT1_Total`.'), 'cdc45_total': ('CDC45_Total', 'native SBML value', 'CDC45-Total. Maps to SBML symbol `CDC45_Total`.'), 'orc_p': ('ORC_P', 'native SBML value', 'ORC_P. Maps to SBML symbol `ORC_P`.'), 'orc_mcm_dbf4_cdc45': ('ORC_MCM_DBF4_CDC45', 'native SBML value', 'ORC_MCM_DBF4_CDC45. Maps to SBML symbol `ORC_MCM_DBF4_CDC45`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812050001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
