# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Yuraszeck2010 - Vulnerabilities in the Tau Network in Tau Pathophysiology."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yuraszeck2010VulnerabilitiesInTheTauNetworkBiomd0000000542Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Yuraszeck2010 - Vulnerabilities in the Tau Network in Tau Pathophysiology."""

    _SBML_ID = 'BIOMD0000000542'
    _TITLE = 'Yuraszeck2010 - Vulnerabilities in the Tau Network in Tau Pathophysiology'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ADP', 'ATP', 'MT', '_20S', 'Hsc70', 'Hsp90', 'CHIP', 'Bag2', '_26S', 'TauH3RUb', 'TauH4RUb', 'Nucleus3', 'Nucleus4', 'Agg33', 'Ap', 'Agg43', 'Bp', 'Tau03R', 'TauN3R', 'TauH3R', 'Tau0_3R', 'Tau03RMT', 'TauN_3R', 'TauN3RMT', 'TauH_3R', 'TauH3RMT', 'TauH3R_Hsc70', 'TauH3R_Hsp90', 'Tau03R_Hsp90', 'TauH3R_CHIP_Hsc70', 'TauH3R_CHIP_Hsc70_Bag2', 'Tau04R', 'TauN4R', 'TauH4R', 'Tau0_4R', 'Tau04RMT', 'TauN_4R', 'TauN4RMT', 'TauH_4R', 'TauH4RMT', 'TauH4R_Hsc70', 'TauH4R_Hsp90', 'Tau04R_Hsp90', 'TauH4R_CHIP_Hsc70', 'TauH4R_CHIP_Hsc70_Bag2']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'MT': 'MT', '_20S': '20S', 'Hsc70': 'Hsc70', 'Hsp90': 'Hsp90', 'CHIP': 'CHIP', 'Bag2': 'Bag2', '_26S': '26S', 'TauH3RUb': 'TauH3RUb', 'TauH4RUb': 'TauH4RUb', 'Nucleus3': 'Nucleus3', 'Nucleus4': 'Nucleus4', 'Agg33': 'Agg33', 'Ap': 'Ap', 'Agg43': 'Agg43', 'Bp': 'Bp', 'Tau03R': 'Tau03R', 'TauN3R': 'TauN3R', 'TauH3R': 'TauH3R', 'Tau0_3R': 'Tau0*3R', 'Tau03RMT': 'Tau03RMT', 'TauN_3R': 'TauN*3R', 'TauN3RMT': 'TauN3RMT', 'TauH_3R': 'TauH*3R', 'TauH3RMT': 'TauH3RMT', 'TauH3R_Hsc70': 'TauH3R-Hsc70', 'TauH3R_Hsp90': 'TauH3R-Hsp90', 'Tau03R_Hsp90': 'Tau03R-Hsp90', 'TauH3R_CHIP_Hsc70': 'TauH3R-CHIP-Hsc70', 'TauH3R_CHIP_Hsc70_Bag2': 'TauH3R-CHIP-Hsc70-Bag2', 'Tau04R': 'Tau04R', 'TauN4R': 'TauN4R', 'TauH4R': 'TauH4R', 'Tau0_4R': 'Tau0*4R', 'Tau04RMT': 'Tau04RMT', 'TauN_4R': 'TauN*4R', 'TauN4RMT': 'TauN4RMT', 'TauH_4R': 'TauH*4R', 'TauH4RMT': 'TauH4RMT', 'TauH4R_Hsc70': 'TauH4R-Hsc70', 'TauH4R_Hsp90': 'TauH4R-Hsp90', 'Tau04R_Hsp90': 'Tau04R-Hsp90', 'TauH4R_CHIP_Hsc70': 'TauH4R-CHIP-Hsc70', 'TauH4R_CHIP_Hsc70_Bag2': 'TauH4R-CHIP-Hsc70-Bag2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_adp': ('ADP', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_model_state_atp': ('ATP', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_tau_n_4_r': ('TauN_4R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TauN_4R`.'), 'initial_tau_n_3_r': ('TauN_3R', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TauN_3R`.'), 'initial_tau_h4_r_hsp90': ('TauH4R_Hsp90', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TauH4R_Hsp90`.'), 'initial_tau_h4_r_hsc70': ('TauH4R_Hsc70', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TauH4R_Hsc70`.')}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'tau_n_4_r': ('TauN_4R', 'native SBML value', 'TauN*4R. Maps to SBML symbol `TauN_4R`.'), 'tau_n_3_r': ('TauN_3R', 'native SBML value', 'TauN*3R. Maps to SBML symbol `TauN_3R`.'), 'tau_h4_r_hsp90': ('TauH4R_Hsp90', 'native SBML value', 'TauH4R-Hsp90. Maps to SBML symbol `TauH4R_Hsp90`.'), 'tau_h4_r_hsc70': ('TauH4R_Hsc70', 'native SBML value', 'TauH4R-Hsc70. Maps to SBML symbol `TauH4R_Hsc70`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000542.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
