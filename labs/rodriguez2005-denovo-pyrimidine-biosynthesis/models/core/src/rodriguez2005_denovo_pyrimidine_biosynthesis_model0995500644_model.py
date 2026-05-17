# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Rodriguez2005_denovo_pyrimidine_biosynthesis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rodriguez2005DenovoPyrimidineBiosynthesisModel0995500644Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Rodriguez2005_denovo_pyrimidine_biosynthesis."""

    _SBML_ID = 'MODEL0995500644'
    _TITLE = 'Rodriguez2005_denovo_pyrimidine_biosynthesis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cp', 'ca', 'dho', 'oro', 'omp', 'ump', 'utp', 'ctp', 'ura', 'E1', 'E2', 'atp']
    _SPECIES_LABELS = {'cp': 'Cp', 'ca': 'Ca', 'dho': 'Dho', 'oro': 'Oro', 'omp': 'Omp', 'ump': 'Ump', 'utp': 'Utp', 'ctp': 'Ctp', 'ura': 'Ura', 'E1': 'E1', 'E2': 'E2', 'atp': 'atp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('atp', 6.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`.'), 'initial_model_state_ca': ('ca', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ca`.'), 'initial_model_state_e2': ('E2', 700.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `E2`.'), 'initial_model_state_oro': ('oro', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `oro`.'), 'initial_model_state_omp': ('omp', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `omp`.'), 'initial_model_state_dho': ('dho', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dho`.')}
    _HEADLINE_OUTPUTS = {'atp': ('atp', 'native SBML value', 'atp. Maps to SBML symbol `atp`.'), 'model_state_ca': ('ca', 'native SBML value', 'Ca. Maps to SBML symbol `ca`.'), 'model_state_e2': ('E2', 'native SBML value', 'E2. Maps to SBML symbol `E2`.'), 'oro': ('oro', 'native SBML value', 'Oro. Maps to SBML symbol `oro`.'), 'omp': ('omp', 'native SBML value', 'Omp. Maps to SBML symbol `omp`.'), 'dho': ('dho', 'native SBML value', 'Dho. Maps to SBML symbol `dho`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0995500644.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
