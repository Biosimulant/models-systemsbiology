# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Peterson2010 - Integrated calcium homeostasis and bone remodelling."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Peterson2010IntegratedCalciumHomeostasisAndBiomd0000000613Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Peterson2010 - Integrated calcium homeostasis and bone remodelling."""

    _SBML_ID = 'BIOMD0000000613'
    _TITLE = 'Peterson2010 - Integrated calcium homeostasis and bone remodelling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PTH', 'S', 'PTmax', 'B', 'SC', 'P', 'ECCPhos', 'T', 'R', 'HAp', 'OB', 'PhosGut', 'IntraPO', 'OC', 'ROB1', 'L', 'RNK', 'O', 'Q', 'Qbone', 'RX2', 'CREB', 'BCL2', 'TERISC', 'A', 'TGFB', 'TGFBact', 'OBfast', 'OBslow', 'M', 'N']
    _SPECIES_LABELS = {'PTH': 'PTH', 'S': 'S', 'PTmax': 'PTmax', 'B': 'B', 'SC': 'SC', 'P': 'P', 'ECCPhos': 'ECCPhos', 'T': 'T', 'R': 'R', 'HAp': 'HAp', 'OB': 'OB', 'PhosGut': 'PhosGut', 'IntraPO': 'IntraPO', 'OC': 'OC', 'ROB1': 'ROB1', 'L': 'L', 'RNK': 'RNK', 'O': 'O', 'Q': 'Q', 'Qbone': 'Qbone', 'RX2': 'RX2', 'CREB': 'CREB', 'BCL2': 'BCL2', 'TERISC': 'TERISC', 'A': 'A', 'TGFB': 'TGFB', 'TGFBact': 'TGFBact', 'OBfast': 'OBfast', 'OBslow': 'OBslow', 'M': 'M', 'N': 'N'}
    _PARAMETER_INPUTS = {'teri_dose_mcg': ('teri_dose_mcg', 20.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `teri_dose_mcg`.'), 'teri_number_of_doses': ('teri_number_of_doses', 3.0, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `teri_number_of_doses`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'tgf_bact': ('TGFBact', 'native SBML value', 'TGFBact. Maps to SBML symbol `TGFBact`.'), 'tgfb': ('TGFB', 'native SBML value', 'TGFB. Maps to SBML symbol `TGFB`.'), 'qbone': ('Qbone', 'native SBML value', 'Qbone. Maps to SBML symbol `Qbone`.'), 'intra_po': ('IntraPO', 'native SBML value', 'IntraPO. Maps to SBML symbol `IntraPO`.'), 'bcl2': ('BCL2', 'native SBML value', 'BCL2. Maps to SBML symbol `BCL2`.'), 'pth': ('PTH', 'native SBML value', 'PTH. Maps to SBML symbol `PTH`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000613.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
