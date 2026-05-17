# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fuentes2005_ZymogenActivation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fuentes2005ZymogenactivationBiomd0000000092Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fuentes2005_ZymogenActivation."""

    _SBML_ID = 'BIOMD0000000092'
    _TITLE = 'Fuentes2005_ZymogenActivation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['z', 'e', 'w', 'ez']
    _SPECIES_LABELS = {'z': 'Zymogen', 'e': 'Enzyme', 'w': 'Peptide', 'ez': 'Enzyme-Substrate complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_enzyme_substrate_complex': ('ez', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ez`.'), 'initial_zymogen': ('z', 2.4e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`.'), 'initial_peptide': ('w', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `w`.'), 'initial_enzyme': ('e', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `e`.')}
    _HEADLINE_OUTPUTS = {'enzyme_substrate_complex': ('ez', 'native SBML value', 'Enzyme-Substrate complex. Maps to SBML symbol `ez`.'), 'zymogen': ('z', 'native SBML value', 'Zymogen. Maps to SBML symbol `z`.'), 'peptide': ('w', 'native SBML value', 'Peptide. Maps to SBML symbol `w`.'), 'enzyme': ('e', 'native SBML value', 'Enzyme. Maps to SBML symbol `e`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000092.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
