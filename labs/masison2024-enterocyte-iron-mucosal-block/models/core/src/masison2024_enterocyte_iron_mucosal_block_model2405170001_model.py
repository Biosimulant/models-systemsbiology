# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Masison2024 - Enterocyte Iron Mucosal Block."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Masison2024EnterocyteIronMucosalBlockModel2405170001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Masison2024 - Enterocyte Iron Mucosal Block."""

    _SBML_ID = 'MODEL2405170001'
    _TITLE = 'Masison2024 - Enterocyte Iron Mucosal Block'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FT_cage', 'core', 'DFP', 'LIP', 'DMT1', 'DMT1_vesicular', 'Fe_blood', 'IRPs_active', 'FPN_internalized', 'IRPs_inactive', 'Fe_lumen', 'body_fe', 'FPN_active']
    _SPECIES_LABELS = {'FT_cage': 'FT-cage', 'core': 'core', 'DFP': 'DFP', 'LIP': 'LIP', 'DMT1': 'DMT1', 'DMT1_vesicular': 'DMT1_vesicular', 'Fe_blood': 'Fe_blood', 'IRPs_active': 'IRPs_active', 'FPN_internalized': 'FPN_internalized', 'IRPs_inactive': 'IRPs_inactive', 'Fe_lumen': 'Fe_lumen', 'body_fe': 'body_fe', 'FPN_active': 'FPN_active'}
    _PARAMETER_INPUTS = {'dose_0': ('dose_0', 1.25e-08, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `dose_0`.'), 'dose_fe': ('dose_fe', 1.25e-08, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `dose_fe`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'fpn_internalized': ('FPN_internalized', 'native SBML value', 'FPN_internalized. Maps to SBML symbol `FPN_internalized`.'), 'core': ('core', 'native SBML value', 'core. Maps to SBML symbol `core`.'), 'fe_lumen': ('Fe_lumen', 'native SBML value', 'Fe_lumen. Maps to SBML symbol `Fe_lumen`.'), 'fe_blood': ('Fe_blood', 'native SBML value', 'Fe_blood. Maps to SBML symbol `Fe_blood`.'), 'ft_cage': ('FT_cage', 'native SBML value', 'FT-cage. Maps to SBML symbol `FT_cage`.'), 'ir_ps_active': ('IRPs_active', 'native SBML value', 'IRPs_active. Maps to SBML symbol `IRPs_active`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2405170001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
