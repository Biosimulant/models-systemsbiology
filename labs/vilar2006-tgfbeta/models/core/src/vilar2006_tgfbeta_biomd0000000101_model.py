# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Vilar2006_TGFbeta."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vilar2006TgfbetaBiomd0000000101Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Vilar2006_TGFbeta."""

    _SBML_ID = 'BIOMD0000000101'
    _TITLE = 'Vilar2006_TGFbeta'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['RI', 'RII', 'lRIRII', 'lRIRII_endo', 'RI_endo', 'RII_endo']
    _SPECIES_LABELS = {'RI': 'Receptor 1', 'RII': 'Receptor 2', 'lRIRII': 'ligand receptor complex-plasma membrane', 'lRIRII_endo': 'ligand receptor complex-endosome', 'RI_endo': 'Receptor 1-endosome', 'RII_endo': 'Receptor 2 endosome'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ligand_receptor_complex_endosome': ('lRIRII_endo', 40.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `lRIRII_endo`.'), 'initial_receptor_2': ('RII', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RII`.'), 'initial_receptor_1': ('RI', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI`.'), 'initial_ligand_receptor_complex_plasma_membrane': ('lRIRII', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `lRIRII`.'), 'initial_receptor_2_endosome': ('RII_endo', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RII_endo`.'), 'initial_receptor_1_endosome': ('RI_endo', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI_endo`.')}
    _HEADLINE_OUTPUTS = {'ligand_receptor_complex_endosome': ('lRIRII_endo', 'native SBML value', 'ligand receptor complex-endosome. Maps to SBML symbol `lRIRII_endo`.'), 'receptor_2': ('RII', 'native SBML value', 'Receptor 2. Maps to SBML symbol `RII`.'), 'receptor_1': ('RI', 'native SBML value', 'Receptor 1. Maps to SBML symbol `RI`.'), 'ligand_receptor_complex_plasma_membrane': ('lRIRII', 'native SBML value', 'ligand receptor complex-plasma membrane. Maps to SBML symbol `lRIRII`.'), 'receptor_2_endosome': ('RII_endo', 'native SBML value', 'Receptor 2 endosome. Maps to SBML symbol `RII_endo`.'), 'receptor_1_endosome': ('RI_endo', 'native SBML value', 'Receptor 1-endosome. Maps to SBML symbol `RI_endo`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000101.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
