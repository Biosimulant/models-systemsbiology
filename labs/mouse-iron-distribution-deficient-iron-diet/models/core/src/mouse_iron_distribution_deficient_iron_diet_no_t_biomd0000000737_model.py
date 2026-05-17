# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Mouse Iron Distribution - Deficient iron diet (No Tracer)."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class MouseIronDistributionDeficientIronDietNoTBiomd0000000737Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Mouse Iron Distribution - Deficient iron diet (No Tracer)."""

    _SBML_ID = 'BIOMD0000000737'
    _TITLE = 'Mouse Iron Distribution - Deficient iron diet (No Tracer)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FeDuo', 'FeRBC', 'FeSpleen', 'FeLiver', 'Tf', 'Hepcidin', 'Fe2Tf', 'Fe1Tf', 'NTBI', 'FeRest', 'FeOutside', 'FeBM']
    _SPECIES_LABELS = {'FeDuo': 'FeDuo', 'FeRBC': 'FeRBC', 'FeSpleen': 'FeSpleen', 'FeLiver': 'FeLiver', 'Tf': 'Tf', 'Hepcidin': 'Hepcidin', 'Fe2Tf': 'Fe2Tf', 'Fe1Tf': 'Fe1Tf', 'NTBI': 'NTBI', 'FeRest': 'FeRest', 'FeOutside': 'FeOutside', 'FeBM': 'FeBM'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fe_liver': ('FeLiver', 0.00200010981212238, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeLiver`.'), 'initial_fe_rbc': ('FeRBC', 0.0379799887571665, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRBC`.'), 'initial_fe_duo': ('FeDuo', 0.0117590568706314, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeDuo`.'), 'initial_fe_spleen': ('FeSpleen', 0.00394239990123767, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeSpleen`.'), 'initial_fe_bm': ('FeBM', 0.00303783614844319, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeBM`.'), 'initial_fe_rest': ('FeRest', 0.000286841656341217, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRest`.')}
    _HEADLINE_OUTPUTS = {'fe_liver': ('FeLiver', 'native SBML value', 'FeLiver. Maps to SBML symbol `FeLiver`.'), 'fe_rbc': ('FeRBC', 'native SBML value', 'FeRBC. Maps to SBML symbol `FeRBC`.'), 'fe_duo': ('FeDuo', 'native SBML value', 'FeDuo. Maps to SBML symbol `FeDuo`.'), 'fe_spleen': ('FeSpleen', 'native SBML value', 'FeSpleen. Maps to SBML symbol `FeSpleen`.'), 'fe_bm': ('FeBM', 'native SBML value', 'FeBM. Maps to SBML symbol `FeBM`.'), 'fe_rest': ('FeRest', 'native SBML value', 'FeRest. Maps to SBML symbol `FeRest`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000737.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
