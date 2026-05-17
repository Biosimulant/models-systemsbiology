# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for LlorénsRico2016 - Effects of cis-Encoded antisense RNAs (asRNAs) - Case2."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class LlorNsrico2016EffectsOfCisEncodedAntisenseModel1511170001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for LlorénsRico2016 - Effects of cis-Encoded antisense RNAs (asRNAs) - Case2."""

    _SBML_ID = 'MODEL1511170001'
    _TITLE = 'LlorénsRico2016 - Effects of cis-Encoded antisense RNAs (asRNAs) - Case2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['mrna', 'asrna', 'protein', 'rib', 'mrnarib']
    _SPECIES_LABELS = {'mrna': 'mrna', 'asrna': 'asrna', 'protein': 'protein', 'rib': 'rib', 'mrnarib': 'mrnarib'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_rib': ('rib', 6.03811178998255e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rib`.'), 'initial_protein': ('protein', 5.04520833250758e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `protein`.'), 'initial_mrna': ('mrna', 3.11023622047244e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mrna`.'), 'initial_asrna': ('asrna', 1.7007299270073e-09, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `asrna`.'), 'initial_mrnarib': ('mrnarib', 2.11057881910267e-10, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mrnarib`.')}
    _HEADLINE_OUTPUTS = {'rib': ('rib', 'native SBML value', 'rib. Maps to SBML symbol `rib`.'), 'protein': ('protein', 'native SBML value', 'protein. Maps to SBML symbol `protein`.'), 'mrna': ('mrna', 'native SBML value', 'mrna. Maps to SBML symbol `mrna`.'), 'asrna': ('asrna', 'native SBML value', 'asrna. Maps to SBML symbol `asrna`.'), 'mrnarib': ('mrnarib', 'native SBML value', 'mrnarib. Maps to SBML symbol `mrnarib`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1511170001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
