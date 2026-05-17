# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Haffez2017 - RAR interaction with synthetic analogues."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Haffez2017RarInteractionWithSyntheticAnalogBiomd0000000629Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Haffez2017 - RAR interaction with synthetic analogues."""

    _SBML_ID = 'BIOMD0000000629'
    _TITLE = 'Haffez2017 - RAR interaction with synthetic analogues'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'LR', 'R', 'CA', 'LRCA']
    _SPECIES_LABELS = {'L': 'Ligand', 'LR': 'Ligand-Receptor', 'R': 'Receptor', 'CA': 'CoActivator', 'LRCA': 'Ligand-Receptor-CoActivator'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_co_activator': ('CA', 30.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CA`.'), 'initial_ligand_receptor_co_activator': ('LRCA', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LRCA`.'), 'initial_ligand_receptor': ('LR', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LR`.'), 'initial_receptor': ('R', 0.0035, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R`.'), 'initial_ligand': ('L', 0.0005, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`.')}
    _HEADLINE_OUTPUTS = {'co_activator': ('CA', 'native SBML value', 'CoActivator. Maps to SBML symbol `CA`.'), 'ligand_receptor_co_activator': ('LRCA', 'native SBML value', 'Ligand-Receptor-CoActivator. Maps to SBML symbol `LRCA`.'), 'ligand_receptor': ('LR', 'native SBML value', 'Ligand-Receptor. Maps to SBML symbol `LR`.'), 'receptor': ('R', 'native SBML value', 'Receptor. Maps to SBML symbol `R`.'), 'ligand': ('L', 'native SBML value', 'Ligand. Maps to SBML symbol `L`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000629.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
