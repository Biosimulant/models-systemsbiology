# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Kowald2006_SOD."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kowald2006SodBiomd0000000108Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Kowald2006_SOD."""

    _SBML_ID = 'BIOMD0000000108'
    _TITLE = 'Kowald2006_SOD'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_0000001', 'species_0000002', 'species_0000006', 'species_0000007', 'species_0000008', 'species_0000009', 'species_0000011', 'species_0000016', 'species_0000017']
    _SPECIES_LABELS = {'species_0000001': 'O2*-', 'species_0000002': 'Cu(II)ZnSOD', 'species_0000006': 'H2O2', 'species_0000007': 'LOO*', 'species_0000008': 'HO*', 'species_0000009': 'LOOH', 'species_0000011': 'L*', 'species_0000016': 'SODtotal', 'species_0000017': 'Cat'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_so_dtotal': ('species_0000016', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000016`.'), 'initial_model_state_cat': ('species_0000017', 1e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000017`.'), 'initial_cu_ii_zn_sod': ('species_0000002', 5e-06, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000002`.'), 'initial_model_state_o2': ('species_0000001', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000001`.'), 'initial_looh': ('species_0000009', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000009`.'), 'initial_model_state_loo': ('species_0000007', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `species_0000007`.')}
    _HEADLINE_OUTPUTS = {'so_dtotal': ('species_0000016', 'native SBML value', 'SODtotal. Maps to SBML symbol `species_0000016`.'), 'cat': ('species_0000017', 'native SBML value', 'Cat. Maps to SBML symbol `species_0000017`.'), 'cu_ii_zn_sod': ('species_0000002', 'native SBML value', 'Cu(II)ZnSOD. Maps to SBML symbol `species_0000002`.'), 'model_state_o2': ('species_0000001', 'native SBML value', 'O2*-. Maps to SBML symbol `species_0000001`.'), 'looh': ('species_0000009', 'native SBML value', 'LOOH. Maps to SBML symbol `species_0000009`.'), 'loo': ('species_0000007', 'native SBML value', 'LOO*. Maps to SBML symbol `species_0000007`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000108.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
