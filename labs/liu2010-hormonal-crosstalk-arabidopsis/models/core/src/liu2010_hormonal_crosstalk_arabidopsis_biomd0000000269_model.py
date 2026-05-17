# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Liu2010_Hormonal_Crosstalk_Arabidopsis."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Liu2010HormonalCrosstalkArabidopsisBiomd0000000269Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Liu2010_Hormonal_Crosstalk_Arabidopsis."""

    _SBML_ID = 'BIOMD0000000269'
    _TITLE = 'Liu2010_Hormonal_Crosstalk_Arabidopsis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Auxin', 'X', 'PLSp', 'Ra', 'Ra_star', 'RaT', 'CK', 'ET', 'PLSm', 'Re', 'ReT', 'Re_star', 'CTR1', 'CTR1T', 'CTR1_star', 'IAA', 'ACC', 'CK_ex']
    _SPECIES_LABELS = {'Auxin': 'Auxin', 'X': 'X', 'PLSp': 'PLSp', 'Ra': 'Ra', 'Ra_star': 'Ra*', 'RaT': 'Ra_total', 'CK': 'CK', 'ET': 'ET', 'PLSm': 'PLSm', 'Re': 'Re', 'ReT': 'Re_total', 'Re_star': 'Re*', 'CTR1': 'CTR1', 'CTR1T': 'CTR1_total', 'CTR1_star': 'CTR1*', 'IAA': 'IAA', 'ACC': 'ACC', 'CK_ex': 'Cytokinin_ext'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ra_total': ('RaT', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RaT`.'), 'initial_model_state_ra': ('Ra_star', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ra_star`.'), 'initial_re_total': ('ReT', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ReT`.'), 'initial_model_state_re': ('Re_star', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Re_star`.'), 'initial_ctr1_total': ('CTR1T', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CTR1T`.'), 'initial_ctr1': ('CTR1_star', 0.3, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CTR1_star`.')}
    _HEADLINE_OUTPUTS = {'ra_total': ('RaT', 'native SBML value', 'Ra_total. Maps to SBML symbol `RaT`.'), 'model_state_ra': ('Ra_star', 'native SBML value', 'Ra*. Maps to SBML symbol `Ra_star`.'), 're_total': ('ReT', 'native SBML value', 'Re_total. Maps to SBML symbol `ReT`.'), 'model_state_re': ('Re_star', 'native SBML value', 'Re*. Maps to SBML symbol `Re_star`.'), 'ctr1_total': ('CTR1T', 'native SBML value', 'CTR1_total. Maps to SBML symbol `CTR1T`.'), 'ctr1': ('CTR1_star', 'native SBML value', 'CTR1*. Maps to SBML symbol `CTR1_star`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000269.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
