# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Fisher2006_Ca_Oscillation_dpdnt_NFAT_dynamics."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fisher2006CaOscillationDpdntNfatDynamicsBiomd0000000122Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Fisher2006_Ca_Oscillation_dpdnt_NFAT_dynamics."""

    _SBML_ID = 'BIOMD0000000122'
    _TITLE = 'Fisher2006_Ca_Oscillation_dpdnt_NFAT_dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ca_Nuc', 'Ca_Cyt', 'NFAT_Nuc', 'Act_C_Nuc', 'NFAT_Pi_Nuc', 'NFAT_Act_C_Nuc', 'NFAT_Pi_Act_C_Nuc', 'Inact_C_Nuc', 'NFAT_Cyt', 'Act_C_Cyt', 'NFAT_Pi_Cyt', 'NFAT_Act_C_Cyt', 'NFAT_Pi_Act_C_Cyt', 'Inact_C_Cyt']
    _SPECIES_LABELS = {'Ca_Nuc': 'Calcium in Nucleus', 'Ca_Cyt': 'Calcium in Cytosol', 'NFAT_Nuc': 'NFAT_nuc', 'Act_C_Nuc': 'Active Calcineurin in Nucleus', 'NFAT_Pi_Nuc': 'Phosphorylated NFAT in nucleus', 'NFAT_Act_C_Nuc': 'NFAT Calcineurin complex in nucleus', 'NFAT_Pi_Act_C_Nuc': 'Phosphorylated NFAT Calcineurin complex in nucleus', 'Inact_C_Nuc': 'Inactive Calcineurin in nucleus', 'NFAT_Cyt': 'NFAT_Cyt', 'Act_C_Cyt': 'Active Calcineurin in cytosol', 'NFAT_Pi_Cyt': 'Phosphorylated NFAT in cytosol', 'NFAT_Act_C_Cyt': 'NFAT Calcineurin complex in cytosol', 'NFAT_Pi_Act_C_Cyt': 'Phosphorylated NFAT Calcineurin complex in cytosol', 'Inact_C_Cyt': 'Inactive Calcineurin in cytosol'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_in_nucleus': ('Ca_Nuc', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_Nuc`.'), 'initial_calcium_in_cytosol': ('Ca_Cyt', 1.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_Cyt`.'), 'initial_inactive_calcineurin_in_nucleus': ('Inact_C_Nuc', 0.049198, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Inact_C_Nuc`.'), 'initial_inactive_calcineurin_in_cytosol': ('Inact_C_Cyt', 0.0097108, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Inact_C_Cyt`.'), 'initial_phosphorylated_nfat_in_cytosol': ('NFAT_Pi_Cyt', 0.0094397, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFAT_Pi_Cyt`.'), 'initial_nfat_calcineurin_complex_in_nucleus': ('NFAT_Act_C_Nuc', 0.0009477, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFAT_Act_C_Nuc`.')}
    _HEADLINE_OUTPUTS = {'calcium_in_nucleus': ('Ca_Nuc', 'native SBML value', 'Calcium in Nucleus. Maps to SBML symbol `Ca_Nuc`.'), 'calcium_in_cytosol': ('Ca_Cyt', 'native SBML value', 'Calcium in Cytosol. Maps to SBML symbol `Ca_Cyt`.'), 'inactive_calcineurin_in_nucleus': ('Inact_C_Nuc', 'native SBML value', 'Inactive Calcineurin in nucleus. Maps to SBML symbol `Inact_C_Nuc`.'), 'inactive_calcineurin_in_cytosol': ('Inact_C_Cyt', 'native SBML value', 'Inactive Calcineurin in cytosol. Maps to SBML symbol `Inact_C_Cyt`.'), 'phosphorylated_nfat_in_cytosol': ('NFAT_Pi_Cyt', 'native SBML value', 'Phosphorylated NFAT in cytosol. Maps to SBML symbol `NFAT_Pi_Cyt`.'), 'nfat_calcineurin_complex_in_nucleus': ('NFAT_Act_C_Nuc', 'native SBML value', 'NFAT Calcineurin complex in nucleus. Maps to SBML symbol `NFAT_Act_C_Nuc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000122.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
