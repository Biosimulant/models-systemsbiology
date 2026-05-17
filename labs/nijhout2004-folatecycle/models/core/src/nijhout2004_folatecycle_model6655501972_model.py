# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Nijhout2004_FolateCycle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nijhout2004FolatecycleModel6655501972Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Nijhout2004_FolateCycle."""

    _SBML_ID = 'MODEL6655501972'
    _TITLE = 'Nijhout2004_FolateCycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['_5mTHF', 'THF', 'DHF', '_5_10_CH2THF', '_5_10_CHTHF', '_10fTHF', 'Ser', 'Gly', 'dUMP', 'GAR', 'AICAR', 'HCOOH', 'NADPH', 'Hcy', 'F', 'purine_synth', 'Met', 'NADP', 'dTMP_pyrimidine_synth']
    _SPECIES_LABELS = {'_5mTHF': '5mTHF', 'THF': 'THF', 'DHF': 'DHF', '_5_10_CH2THF': '5 10 CH2THF', '_5_10_CHTHF': '5 10 CHTHF', '_10fTHF': '10fTHF', 'Ser': 'Ser', 'Gly': 'Gly', 'dUMP': 'DUMP', 'GAR': 'GAR', 'AICAR': 'AICAR', 'HCOOH': 'HCOOH', 'NADPH': 'NADPH', 'Hcy': 'Hcy', 'F': 'F', 'purine_synth': 'Purine Synth', 'Met': 'Met', 'NADP': 'NADP', 'dTMP_pyrimidine_synth': 'DTMP Pyrimidine Synth'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nadph': ('NADPH', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`.'), 'initial_nadp': ('NADP', 50.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`.'), 'initial_model_state_gly': ('Gly', 1850.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`.'), 'initial_hcooh': ('HCOOH', 900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HCOOH`.'), 'initial_model_state_ser': ('Ser', 468.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ser`.'), 'initial_dump': ('dUMP', 20.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `dUMP`.')}
    _HEADLINE_OUTPUTS = {'nadph': ('NADPH', 'native SBML value', 'NADPH. Maps to SBML symbol `NADPH`.'), 'nadp': ('NADP', 'native SBML value', 'NADP. Maps to SBML symbol `NADP`.'), 'gly': ('Gly', 'native SBML value', 'Gly. Maps to SBML symbol `Gly`.'), 'hcooh': ('HCOOH', 'native SBML value', 'HCOOH. Maps to SBML symbol `HCOOH`.'), 'ser': ('Ser', 'native SBML value', 'Ser. Maps to SBML symbol `Ser`.'), 'dump': ('dUMP', 'native SBML value', 'DUMP. Maps to SBML symbol `dUMP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL6655501972.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
