# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Condorelli2001_GuanylateCyclase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Condorelli2001GuanylatecyclaseModel4780441670Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Condorelli2001_GuanylateCyclase."""

    _SBML_ID = 'MODEL4780441670'
    _TITLE = 'Condorelli2001_GuanylateCyclase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GC_slash_NO_sGCpart_act', 'GC_slash_NO_sGCfull_act', 'GC_slash_NO_sGCfull_act_slash_full_act_sGC_slash_full_act_sGC_cplx', 'GC_slash_GTP', 'GC_slash_cGMP', 'GC_slash_NO_a', 'GC_slash_sGC_basal', 'GC_slash_NO']
    _SPECIES_LABELS = {'GC_slash_NO_sGCpart_act': 'GC Slash NO SGCpart Act', 'GC_slash_NO_sGCfull_act': 'GC Slash NO SGCfull Act', 'GC_slash_NO_sGCfull_act_slash_full_act_sGC_slash_full_act_sGC_cplx': 'GC Slash NO SGCfull Act Slash Full Act SGC Slash Full Act SGC Cplx', 'GC_slash_GTP': 'GC Slash GTP', 'GC_slash_cGMP': 'GC Slash CGMP', 'GC_slash_NO_a': 'GC Slash NO A', 'GC_slash_sGC_basal': 'GC Slash SGC Basal', 'GC_slash_NO': 'GC Slash NO'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_gc_slash_gtp': ('GC_slash_GTP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_GTP`.'), 'initial_gc_slash_sgc_basal': ('GC_slash_sGC_basal', 3.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_sGC_basal`.'), 'initial_gc_slash_no_a': ('GC_slash_NO_a', 0.1, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_NO_a`.'), 'initial_gc_slash_no_sg_cpart_act': ('GC_slash_NO_sGCpart_act', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_NO_sGCpart_act`.'), 'initial_gc_slash_no_sg_cfull_act': ('GC_slash_NO_sGCfull_act', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_NO_sGCfull_act`.'), 'initial_gc_slash_no': ('GC_slash_NO', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GC_slash_NO`.')}
    _HEADLINE_OUTPUTS = {'gc_slash_gtp': ('GC_slash_GTP', 'native SBML value', 'GC Slash GTP. Maps to SBML symbol `GC_slash_GTP`.'), 'gc_slash_sgc_basal': ('GC_slash_sGC_basal', 'native SBML value', 'GC Slash SGC Basal. Maps to SBML symbol `GC_slash_sGC_basal`.'), 'gc_slash_no_a': ('GC_slash_NO_a', 'native SBML value', 'GC Slash NO A. Maps to SBML symbol `GC_slash_NO_a`.'), 'gc_slash_no_sg_cpart_act': ('GC_slash_NO_sGCpart_act', 'native SBML value', 'GC Slash NO SGCpart Act. Maps to SBML symbol `GC_slash_NO_sGCpart_act`.'), 'gc_slash_no_sg_cfull_act': ('GC_slash_NO_sGCfull_act', 'native SBML value', 'GC Slash NO SGCfull Act. Maps to SBML symbol `GC_slash_NO_sGCfull_act`.'), 'gc_slash_no': ('GC_slash_NO', 'native SBML value', 'GC Slash NO. Maps to SBML symbol `GC_slash_NO`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL4780441670.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
