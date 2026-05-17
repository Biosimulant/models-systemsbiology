# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for dAlcantara2003_SynapticPlasticity."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dalcantara2003SynapticplasticityModel8938094216Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for dAlcantara2003_SynapticPlasticity."""

    _SBML_ID = 'MODEL8938094216'
    _TITLE = 'dAlcantara2003_SynapticPlasticity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Sstar', 'K', 'Kprime', 'Kstar', 'N', 'Nstar', 'D', 'Dstar', 'R', 'Rprime', 'Rstar', 'Pstar', 'DstarP', 'Stotal', 'Ca2plus']
    _SPECIES_LABELS = {'Sstar': 'S*', 'K': 'K', 'Kprime': "K'", 'Kstar': 'K*', 'N': 'N', 'Nstar': 'N*', 'D': 'D', 'Dstar': 'D*', 'R': 'R', 'Rprime': "R'", 'Rstar': 'R*', 'Pstar': 'P*', 'DstarP': 'D*P', 'Stotal': 'S total', 'Ca2plus': 'Ca2plus'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_s_total': ('Stotal', 30.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Stotal`.'), 'initial_model_state_p': ('Pstar', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pstar`.'), 'initial_model_state_s': ('Sstar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sstar`.'), 'initial_model_state_r': ('Rstar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rstar`.'), 'initial_model_state_r_2': ('Rprime', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rprime`.'), 'initial_model_state_n': ('Nstar', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Nstar`.')}
    _HEADLINE_OUTPUTS = {'s_total': ('Stotal', 'native SBML value', 'S total. Maps to SBML symbol `Stotal`.'), 'model_state_p': ('Pstar', 'native SBML value', 'P*. Maps to SBML symbol `Pstar`.'), 'model_state_s': ('Sstar', 'native SBML value', 'S*. Maps to SBML symbol `Sstar`.'), 'model_state_r': ('Rstar', 'native SBML value', 'R*. Maps to SBML symbol `Rstar`.'), 'model_state_r_2': ('Rprime', 'native SBML value', "R'. Maps to SBML symbol `Rprime`."), 'model_state_n': ('Nstar', 'native SBML value', 'N*. Maps to SBML symbol `Nstar`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL8938094216.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
