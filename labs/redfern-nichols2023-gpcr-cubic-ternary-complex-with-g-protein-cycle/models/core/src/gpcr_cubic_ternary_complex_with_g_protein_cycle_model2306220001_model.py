# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for GPCR Cubic Ternary Complex with G protein Cycle, Redfern-Nichols 2023."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GpcrCubicTernaryComplexWithGProteinCycleModel2306220001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for GPCR Cubic Ternary Complex with G protein Cycle, Redfern-Nichols 2023."""

    _SBML_ID = 'MODEL2306220001'
    _TITLE = 'GPCR Cubic Ternary Complex with G protein Cycle, Redfern-Nichols 2023'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'LRi', 'Ri', 'Ra', 'G', 'RiG', 'LRa', 'LRiG', 'RaG', 'LRaG', 'GaGTP', 'Gbg', 'GaGDP', 'ATP', 'cAMP', 'AC', 'GaGTPAC']
    _SPECIES_LABELS = {'L': 'L', 'LRi': 'LRi', 'Ri': 'Ri', 'Ra': 'Ra', 'G': 'G', 'RiG': 'RiG', 'LRa': 'LRa', 'LRiG': 'LRiG', 'RaG': 'RaG', 'LRaG': 'LRaG', 'GaGTP': 'GaGTP', 'Gbg': 'Gbg', 'GaGDP': 'GaGDP', 'ATP': 'ATP', 'cAMP': 'cAMP', 'AC': 'AC', 'GaGTPAC': 'GaGTPAC'}
    _PARAMETER_INPUTS = {'event_ligand_applied': ('Event__Ligand__Applied', 1e-06, 'unit_3', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Event__Ligand__Applied`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'camp': ('cAMP', 'substance', 'cAMP. Maps to SBML symbol `cAMP`.'), 'atp': ('ATP', 'substance', 'ATP. Maps to SBML symbol `ATP`.'), 'model_state_ac': ('AC', 'substance', 'AC. Maps to SBML symbol `AC`.'), 'model_state_ri': ('Ri', 'substance', 'Ri. Maps to SBML symbol `Ri`.'), 'ri_g': ('RiG', 'substance', 'RiG. Maps to SBML symbol `RiG`.'), 'ra_g': ('RaG', 'substance', 'RaG. Maps to SBML symbol `RaG`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2306220001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
