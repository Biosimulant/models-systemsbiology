# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Valero2016 - Ascorbate-Glutathione cycle in chloroplasts under light/dark conditions."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Valero2016AscorbateGlutathioneCycleInChloroBiomd0000000589Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Valero2016 - Ascorbate-Glutathione cycle in chloroplasts under light/dark conditions."""

    _SBML_ID = 'BIOMD0000000589'
    _TITLE = 'Valero2016 - Ascorbate-Glutathione cycle in chloroplasts under light/dark conditions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NADPH', 'NADPplus', 'GSH', 'GSSG', 'ASC', 'DHA', 'MDA', 'H2O2', 'APX', 'CoI', 'CoII', 'APXi', 'O2neg']
    _SPECIES_LABELS = {'NADPH': 'NADPH', 'NADPplus': 'NADPplus', 'GSH': 'GSH', 'GSSG': 'GSSG', 'ASC': 'ASC', 'DHA': 'DHA', 'MDA': 'MDA', 'H2O2': 'H2O2', 'APX': 'APX', 'CoI': 'CoI', 'CoII': 'CoII', 'APXi': 'APXi', 'O2neg': 'O2neg'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nadph': ('NADPH', 110.000032696018, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`.'), 'initial_nad_pplus': ('NADPplus', 40.0000118894612, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPplus`.'), 'initial_model_state_asc': ('ASC', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ASC`.'), 'initial_model_state_gsh': ('GSH', 4000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GSH`.'), 'initial_model_state_apx': ('APX', 40.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `APX`.'), 'initial_o2neg': ('O2neg', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O2neg`.')}
    _HEADLINE_OUTPUTS = {'nadph': ('NADPH', 'native SBML value', 'NADPH. Maps to SBML symbol `NADPH`.'), 'nad_pplus': ('NADPplus', 'native SBML value', 'NADPplus. Maps to SBML symbol `NADPplus`.'), 'asc': ('ASC', 'native SBML value', 'ASC. Maps to SBML symbol `ASC`.'), 'gsh': ('GSH', 'native SBML value', 'GSH. Maps to SBML symbol `GSH`.'), 'apx': ('APX', 'native SBML value', 'APX. Maps to SBML symbol `APX`.'), 'o2neg': ('O2neg', 'native SBML value', 'O2neg. Maps to SBML symbol `O2neg`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000589.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
