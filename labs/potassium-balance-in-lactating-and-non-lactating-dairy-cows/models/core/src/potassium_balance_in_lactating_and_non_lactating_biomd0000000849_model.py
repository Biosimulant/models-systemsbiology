# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Potassium balance in lactating and non-lactating dairy cows."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class PotassiumBalanceInLactatingAndNonLactatingBiomd0000000849Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Potassium balance in lactating and non-lactating dairy cows."""

    _SBML_ID = 'BIOMD0000000849'
    _TITLE = 'Potassium balance in lactating and non-lactating dairy cows'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['K_ECF', 'K_ICF', 'K_urin', 'K_tiss', 'K_sal', 'met_act', 'K_milk', 'K_ECF_mmol', 'K_ICF_mmol', 'K_git', 'Gluc_b', 'ins_b', 'Gluc_stor', 'Gluc_prod', 'src_metact', 'snk_metact', 'src_Kgit', 'src_Glucblood', 's23', 'sa4_degraded', 's24', 'src_insnew', 'snk_insnew']
    _SPECIES_LABELS = {'K_ECF': 'K_ECF', 'K_ICF': 'K_ICF', 'K_urin': 'K_urin', 'K_tiss': 'K_tiss', 'K_sal': 'K_sal', 'met_act': 'met_act', 'K_milk': 'K_milk', 'K_ECF_mmol': 'K_ECF_mmol', 'K_ICF_mmol': 'K_ICF_mmol', 'K_git': 'K_git', 'Gluc_b': 'Gluc_b', 'ins_b': 'ins_b', 'Gluc_stor': 'Gluc_stor', 'Gluc_prod': 'Gluc_prod', 'src_metact': 'src_metact', 'snk_metact': 'snk_metact', 'src_Kgit': 'src_Kgit', 'src_Glucblood': 'src_Glucb', 's23': 'src_Gprod', 'sa4_degraded': 'snk_Kecf', 's24': 'Gluc_use', 'src_insnew': 'src_ins', 'snk_insnew': 'snk_ins'}
    _PARAMETER_INPUTS = {'src_glucfeed': ('p46', 0.0854, 'unit_0', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `p46`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'gluc_stor': ('Gluc_stor', 'native SBML value', 'Gluc_stor. Maps to SBML symbol `Gluc_stor`.'), 'k_tiss': ('K_tiss', 'native SBML value', 'K_tiss. Maps to SBML symbol `K_tiss`.'), 'k_git': ('K_git', 'native SBML value', 'K_git. Maps to SBML symbol `K_git`.'), 'gluc_prod': ('Gluc_prod', 'native SBML value', 'Gluc_prod. Maps to SBML symbol `Gluc_prod`.'), 'k_icf_mmol': ('K_ICF_mmol', 'native SBML value', 'K_ICF_mmol. Maps to SBML symbol `K_ICF_mmol`.'), 'ins_b': ('ins_b', 'native SBML value', 'ins_b. Maps to SBML symbol `ins_b`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000849.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
