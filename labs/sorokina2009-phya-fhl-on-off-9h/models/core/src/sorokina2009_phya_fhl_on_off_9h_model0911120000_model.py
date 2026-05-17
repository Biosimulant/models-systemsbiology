# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Sorokina2009_PhyA_FHL_ON_OFF_9h."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sorokina2009PhyaFhlOnOff9hModel0911120000Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Sorokina2009_PhyA_FHL_ON_OFF_9h."""

    _SBML_ID = 'MODEL0911120000'
    _TITLE = 'Sorokina2009_PhyA_FHL_ON_OFF_9h'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FRL', 'Pfr_GBD_c', 'Pfr_GBD_f', 'Pfr_PIF3', 'Pr_GBD_f', 'Pr_PIF3', 'RL', 'nLUC', 'nLuc']
    _SPECIES_LABELS = {'FRL': 'FRL', 'Pfr_GBD_c': 'Pfr_GBD_c', 'Pfr_GBD_f': 'Pfr_GBD_f', 'Pfr_PIF3': 'Pfr_PIF3', 'Pr_GBD_f': 'Pr_GBD_f', 'Pr_PIF3': 'Pr_PIF3', 'RL': 'RL', 'nLUC': 'nLUC', 'nLuc': 'nLuc'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_n_luc': ('nLuc', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nLuc`.'), 'initial_n_luc_2': ('nLUC', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `nLUC`.'), 'initial_pr_pif3': ('Pr_PIF3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pr_PIF3`.'), 'initial_pr_gbd_f': ('Pr_GBD_f', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pr_GBD_f`.'), 'initial_pfr_pif3': ('Pfr_PIF3', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pfr_PIF3`.'), 'initial_pfr_gbd_f': ('Pfr_GBD_f', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pfr_GBD_f`.')}
    _HEADLINE_OUTPUTS = {'n_luc': ('nLuc', 'native SBML value', 'nLuc. Maps to SBML symbol `nLuc`.'), 'n_luc_2': ('nLUC', 'native SBML value', 'nLUC. Maps to SBML symbol `nLUC`.'), 'pr_pif3': ('Pr_PIF3', 'native SBML value', 'Pr_PIF3. Maps to SBML symbol `Pr_PIF3`.'), 'pr_gbd_f': ('Pr_GBD_f', 'native SBML value', 'Pr_GBD_f. Maps to SBML symbol `Pr_GBD_f`.'), 'pfr_pif3': ('Pfr_PIF3', 'native SBML value', 'Pfr_PIF3. Maps to SBML symbol `Pfr_PIF3`.'), 'pfr_gbd_f': ('Pfr_GBD_f', 'native SBML value', 'Pfr_GBD_f. Maps to SBML symbol `Pfr_GBD_f`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0911120000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
