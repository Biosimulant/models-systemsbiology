# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Olsen2003_peroxidase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Olsen2003PeroxidaseBiomd0000000046Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Olsen2003_peroxidase."""

    _SBML_ID = 'BIOMD0000000046'
    _TITLE = 'Olsen2003_peroxidase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NADH', 'O2', 'H2O2', 'per3', 'coI', 'ArH', 'coII', 'Ar', 'NADrad', 'super', 'coIII', 'per2', 'NAD2', 'NAD', 'O2g', 'NADHres']
    _SPECIES_LABELS = {'NADH': 'NADH', 'O2': 'O2', 'H2O2': 'H2O2', 'per3': 'Per3', 'coI': 'CoI', 'ArH': 'ArH', 'coII': 'CoII', 'Ar': 'Ar', 'NADrad': 'NADrad', 'super': 'Super', 'coIII': 'CoIII', 'per2': 'Per2', 'NAD2': 'NAD2', 'NAD': 'NAD', 'O2g': 'O2G', 'NADHres': 'NADHres'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_na_drad': ('NADrad', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADrad`.'), 'initial_nad_hres': ('NADHres', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADHres`.'), 'initial_nadh': ('NADH', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADH`.'), 'initial_nad2': ('NAD2', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NAD2`.'), 'initial_model_state_nad': ('NAD', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NAD`.'), 'initial_ar_h': ('ArH', 500.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ArH`.')}
    _HEADLINE_OUTPUTS = {'na_drad': ('NADrad', 'native SBML value', 'NADrad. Maps to SBML symbol `NADrad`.'), 'nad_hres': ('NADHres', 'native SBML value', 'NADHres. Maps to SBML symbol `NADHres`.'), 'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'nad2': ('NAD2', 'native SBML value', 'NAD2. Maps to SBML symbol `NAD2`.'), 'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'ar_h': ('ArH', 'native SBML value', 'ArH. Maps to SBML symbol `ArH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000046.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
