# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Palmer2014 - Effect of IL-1β-Blocking therapies in T2DM - Healthy Condition."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Palmer2014EffectOfIl1BlockingTherapiesInBiomd0000000621Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Palmer2014 - Effect of IL-1β-Blocking therapies in T2DM - Healthy Condition."""

    _SBML_ID = 'BIOMD0000000621'
    _TITLE = 'Palmer2014 - Effect of IL-1β-Blocking therapies in T2DM - Healthy Condition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IL1b', 'IL1Ra', 'Anakinra', 'Proinsulin', 'Insulin', 'TigB', 'B', 'f', 'Anakinrasc', 'Glucose', 'a1c1', 'rbc1', 'a1c2', 'rbc2', 'a1c3', 'rbc3', 'a1c4', 'rbc4', 'a1c5', 'rbc5', 'a1c6', 'rbc6', 'a1c7', 'rbc7', 'a1c8', 'rbc8', 'a1c9', 'rbc9', 'a1c10', 'rbc10', 'a1c11', 'rbc11', 'a1c12', 'rbc12', 'hba1c']
    _SPECIES_LABELS = {'IL1b': 'IL1b', 'IL1Ra': 'IL1Ra', 'Anakinra': 'Anakinra', 'Proinsulin': 'Proinsulin', 'Insulin': 'Insulin', 'TigB': 'TigB', 'B': 'B', 'f': 'F', 'Anakinrasc': 'Anakinrasc', 'Glucose': 'Glucose', 'a1c1': 'A1c1', 'rbc1': 'Rbc1', 'a1c2': 'A1c2', 'rbc2': 'Rbc2', 'a1c3': 'A1c3', 'rbc3': 'Rbc3', 'a1c4': 'A1c4', 'rbc4': 'Rbc4', 'a1c5': 'A1c5', 'rbc5': 'Rbc5', 'a1c6': 'A1c6', 'rbc6': 'Rbc6', 'a1c7': 'A1c7', 'rbc7': 'Rbc7', 'a1c8': 'A1c8', 'rbc8': 'Rbc8', 'a1c9': 'A1c9', 'rbc9': 'Rbc9', 'a1c10': 'A1c10', 'rbc10': 'Rbc10', 'a1c11': 'A1c11', 'rbc11': 'Rbc11', 'a1c12': 'A1c12', 'rbc12': 'Rbc12', 'hba1c': 'Hba1c'}
    _PARAMETER_INPUTS = {'kglucose': ('Kglucose', 0.000292, 'native SBML value', 'Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `Kglucose`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'insulin': ('Insulin', 'native SBML value', 'Insulin. Maps to SBML symbol `Insulin`.'), 'proinsulin': ('Proinsulin', 'native SBML value', 'Proinsulin. Maps to SBML symbol `Proinsulin`.'), 'glucose': ('Glucose', 'native SBML value', 'Glucose. Maps to SBML symbol `Glucose`.'), 'il1_ra': ('IL1Ra', 'native SBML value', 'IL1Ra. Maps to SBML symbol `IL1Ra`.'), 'rbc1': ('rbc1', 'native SBML value', 'Rbc1. Maps to SBML symbol `rbc1`.'), 'rbc2': ('rbc2', 'native SBML value', 'Rbc2. Maps to SBML symbol `rbc2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000621.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
