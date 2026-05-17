# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Romano-Nguyen2014 - MST2 and Raf1 Crosstalk."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class RomanoNguyen2014Mst2AndRaf1CrosstalkModel1506070001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Romano-Nguyen2014 - MST2 and Raf1 Crosstalk."""

    _SBML_ID = 'MODEL1506070001'
    _TITLE = 'Romano-Nguyen2014 - MST2 and Raf1 Crosstalk'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['pRaf_1i', 'Raf_1', 'LATS1a', 'Raf_1a', 'ppERK', 'pMST2i', 'pMi_pRi', 'MST2', 'M_pRi', 'MST2a', 'F1A', 'Ma_F1A', 'M_F1A', 'LATS1', 'MEK', 'Ra_Mk', 'pMEK', 'ppMEK', 'Ra_pMk', 'ERK', 'pERK']
    _SPECIES_LABELS = {'pRaf_1i': 'PRaf 1I', 'Raf_1': 'RAF 1', 'LATS1a': 'LATS1a', 'Raf_1a': 'RAF 1A', 'ppERK': 'PpERK', 'pMST2i': 'PMST2i', 'pMi_pRi': 'PMi PRi', 'MST2': 'MST2', 'M_pRi': 'M PRi', 'MST2a': 'MST2a', 'F1A': 'F1A', 'Ma_F1A': 'Ma F1A', 'M_F1A': 'M F1A', 'LATS1': 'LATS1', 'MEK': 'MEK', 'Ra_Mk': 'Ra Mk', 'pMEK': 'PMEK', 'ppMEK': 'PpMEK', 'Ra_pMk': 'Ra PMk', 'ERK': 'ERK', 'pERK': 'PERK'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_erk': ('ERK', 3000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ERK`.'), 'initial_model_state_mek': ('MEK', 1600.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MEK`.'), 'initial_mst2': ('MST2', 1500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MST2`.'), 'initial_p_raf_1_i': ('pRaf_1i', 750.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pRaf_1i`.'), 'initial_lats1': ('LATS1', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LATS1`.'), 'initial_f1_a': ('F1A', 100.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `F1A`.')}
    _HEADLINE_OUTPUTS = {'erk': ('ERK', 'native SBML value', 'ERK. Maps to SBML symbol `ERK`.'), 'mek': ('MEK', 'native SBML value', 'MEK. Maps to SBML symbol `MEK`.'), 'mst2': ('MST2', 'native SBML value', 'MST2. Maps to SBML symbol `MST2`.'), 'p_raf_1_i': ('pRaf_1i', 'native SBML value', 'PRaf 1I. Maps to SBML symbol `pRaf_1i`.'), 'lats1': ('LATS1', 'native SBML value', 'LATS1. Maps to SBML symbol `LATS1`.'), 'f1_a': ('F1A', 'native SBML value', 'F1A. Maps to SBML symbol `F1A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1506070001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
