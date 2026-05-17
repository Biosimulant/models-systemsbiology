# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rohwer2000_Phosphotransferase_System."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rohwer2000PhosphotransferaseSystemBiomd0000000038Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rohwer2000_Phosphotransferase_System."""

    _SBML_ID = 'BIOMD0000000038'
    _TITLE = 'Rohwer2000_Phosphotransferase_System'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EI', 'PyrPI', 'EIP', 'HPr', 'EIPHPr', 'HPrP', 'EIIA', 'HPrPIIA', 'EIIAP', 'EIICB', 'EIIAPIICB', 'EIICBP', 'EIICBPGlc', 'PEP', 'Pyr', 'GlcP', 'Glc']
    _SPECIES_LABELS = {'EI': 'EI', 'PyrPI': 'PyrPI', 'EIP': 'EIP', 'HPr': 'HPr', 'EIPHPr': 'EIPHPr', 'HPrP': 'HPrP', 'EIIA': 'EIIA', 'HPrPIIA': 'HPrPIIA', 'EIIAP': 'EIIAP', 'EIICB': 'EIICB', 'EIIAPIICB': 'EIIAPIICB', 'EIICBP': 'EIICBP', 'EIICBPGlc': 'EIICBPGlc', 'PEP': 'PEP', 'Pyr': 'Pyr', 'GlcP': 'GlcP', 'Glc': 'Glc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_pep': ('PEP', 2800.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PEP`.'), 'initial_model_state_pyr': ('Pyr', 900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pyr`.'), 'initial_model_state_glc': ('Glc', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Glc`.'), 'initial_glc_p': ('GlcP', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GlcP`.'), 'initial_h_pr_p': ('HPrP', 25.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HPrP`.'), 'initial_h_pr': ('HPr', 25.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HPr`.')}
    _HEADLINE_OUTPUTS = {'pep': ('PEP', 'native SBML value', 'PEP. Maps to SBML symbol `PEP`.'), 'pyr': ('Pyr', 'native SBML value', 'Pyr. Maps to SBML symbol `Pyr`.'), 'glc': ('Glc', 'native SBML value', 'Glc. Maps to SBML symbol `Glc`.'), 'glc_p': ('GlcP', 'native SBML value', 'GlcP. Maps to SBML symbol `GlcP`.'), 'h_pr_p': ('HPrP', 'native SBML value', 'HPrP. Maps to SBML symbol `HPrP`.'), 'h_pr': ('HPr', 'native SBML value', 'HPr. Maps to SBML symbol `HPr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000038.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
