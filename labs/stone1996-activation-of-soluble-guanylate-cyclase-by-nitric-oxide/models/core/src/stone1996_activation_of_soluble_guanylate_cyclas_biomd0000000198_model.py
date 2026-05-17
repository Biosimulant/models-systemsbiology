# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Stone1996 - activation of soluble guanylate cyclase by nitric oxide."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Stone1996ActivationOfSolubleGuanylateCyclasBiomd0000000198Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Stone1996 - activation of soluble guanylate cyclase by nitric oxide."""

    _SBML_ID = 'BIOMD0000000198'
    _TITLE = 'Stone1996 - activation of soluble guanylate cyclase by nitric oxide'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NO', 'sGCfast', 'NO_sGCfast', 'NO_sGCfast_6coord', 'NO_sGCfast_5coord', 'sGCslow', 'NO_sGCslow', 'NO_sGCslow_6coord', 'NO_sGCslow_6coord_NO_int', 'NO_sGCslow_5coord', 'NO_sGC_5coord_tot', 'sGC_inact_tot']
    _SPECIES_LABELS = {'NO': 'NO', 'sGCfast': 'SGCfast', 'NO_sGCfast': 'NO SGCfast', 'NO_sGCfast_6coord': 'NO SGCfast 6coord', 'NO_sGCfast_5coord': 'NO SGCfast 5coord', 'sGCslow': 'SGCslow', 'NO_sGCslow': 'NO SGCslow', 'NO_sGCslow_6coord': 'NO SGCslow 6coord', 'NO_sGCslow_6coord_NO_int': 'NO SGCslow 6coord NO Int', 'NO_sGCslow_5coord': 'NO SGCslow 5coord', 'NO_sGC_5coord_tot': 'NO SGC 5coord Tot', 'sGC_inact_tot': 'SGC Inact Tot'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_no': ('NO', 0.5, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NO`.'), 'initial_sg_cslow': ('sGCslow', 0.288, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `sGCslow`.'), 'initial_sg_cfast': ('sGCfast', 0.112, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `sGCfast`.'), 'initial_sgc_inact_tot': ('sGC_inact_tot', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `sGC_inact_tot`.'), 'initial_no_sg_cslow_6coord_no_int': ('NO_sGCslow_6coord_NO_int', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NO_sGCslow_6coord_NO_int`.'), 'initial_no_sg_cslow_6coord': ('NO_sGCslow_6coord', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NO_sGCslow_6coord`.')}
    _HEADLINE_OUTPUTS = {'model_state_no': ('NO', 'native SBML value', 'NO. Maps to SBML symbol `NO`.'), 'sg_cslow': ('sGCslow', 'native SBML value', 'SGCslow. Maps to SBML symbol `sGCslow`.'), 'sg_cfast': ('sGCfast', 'native SBML value', 'SGCfast. Maps to SBML symbol `sGCfast`.'), 'sgc_inact_tot': ('sGC_inact_tot', 'native SBML value', 'SGC Inact Tot. Maps to SBML symbol `sGC_inact_tot`.'), 'no_sg_cslow_6coord_no_int': ('NO_sGCslow_6coord_NO_int', 'native SBML value', 'NO SGCslow 6coord NO Int. Maps to SBML symbol `NO_sGCslow_6coord_NO_int`.'), 'no_sg_cslow_6coord': ('NO_sGCslow_6coord', 'native SBML value', 'NO SGCslow 6coord. Maps to SBML symbol `NO_sGCslow_6coord`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000198.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
