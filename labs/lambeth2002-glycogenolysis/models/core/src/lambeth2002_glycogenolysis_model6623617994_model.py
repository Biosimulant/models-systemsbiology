# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Lambeth2002_Glycogenolysis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lambeth2002GlycogenolysisModel6623617994Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Lambeth2002_Glycogenolysis."""

    _SBML_ID = 'MODEL6623617994'
    _TITLE = 'Lambeth2002_Glycogenolysis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['adp', 'NADH', 'atp', 'PCr', 'G1P', 'P', 'G6P', 'F6P', 'FDP', 'DHAP', 'GAP', 'DPG', 'P3G', 'P2G', 'LAC', 'Cr', 'amp', 'PEP', 'PYR', 'NAD', 'Gly', 'LACo']
    _SPECIES_LABELS = {'adp': 'ADP', 'NADH': 'NADH', 'atp': 'ATP', 'PCr': 'PCr', 'G1P': 'G1P', 'P': 'P', 'G6P': 'G6P', 'F6P': 'F6P', 'FDP': 'FDP', 'DHAP': 'DHAP', 'GAP': 'GAP', 'DPG': 'DPG', 'P3G': 'P3G', 'P2G': 'P2G', 'LAC': 'LAC', 'Cr': 'Cr', 'amp': 'AMP', 'PEP': 'PEP', 'PYR': 'PYR', 'NAD': 'NAD', 'Gly': 'Gly', 'LACo': 'LACo'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('atp', 0.0082, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`.'), 'initial_model_state_nad': ('NAD', 0.0005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NAD`.'), 'initial_model_state_adp': ('adp', 1.3e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `adp`.'), 'initial_nadh': ('NADH', 5e-07, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADH`.'), 'initial_model_state_gly': ('Gly', 0.112, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`.'), 'initial_p_cr': ('PCr', 0.03467, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCr`.')}
    _HEADLINE_OUTPUTS = {'atp': ('atp', 'native SBML value', 'ATP. Maps to SBML symbol `atp`.'), 'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'adp': ('adp', 'native SBML value', 'ADP. Maps to SBML symbol `adp`.'), 'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'gly': ('Gly', 'native SBML value', 'Gly. Maps to SBML symbol `Gly`.'), 'p_cr': ('PCr', 'native SBML value', 'PCr. Maps to SBML symbol `PCr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6623617994.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
