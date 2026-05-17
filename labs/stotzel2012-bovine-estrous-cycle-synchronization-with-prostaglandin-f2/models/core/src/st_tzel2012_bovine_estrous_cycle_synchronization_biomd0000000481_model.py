# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Stötzel2012 - Bovine estrous cycle, synchronization with prostaglandin F2α."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class StTzel2012BovineEstrousCycleSynchronizationBiomd0000000481Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Stötzel2012 - Bovine estrous cycle, synchronization with prostaglandin F2α."""

    _SBML_ID = 'BIOMD0000000481'
    _TITLE = 'Stötzel2012 - Bovine estrous cycle, synchronization with prostaglandin F2α'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GnRH_Pit', 'LH_Pit', 'LH_Bld', 'GnRH_Hyp', 'FSH_Pit', 'FSH_Bld', 'Foll', 'CL', 'E2', 'P4', 'Inh', 'OT', 'Enz', 'PGF', 'IOF']
    _SPECIES_LABELS = {'GnRH_Pit': 'GnRH_Pit', 'LH_Pit': 'LH_Pit', 'LH_Bld': 'LH_Bld', 'GnRH_Hyp': 'GnRH_Hyp', 'FSH_Pit': 'FSH_Pit', 'FSH_Bld': 'FSH_Bld', 'Foll': 'Foll', 'CL': 'CL', 'E2': 'E2', 'P4': 'P4', 'Inh': 'Inh', 'OT': 'OT', 'Enz': 'Enz', 'PGF': 'PGF', 'IOF': 'IOF'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lh_pit': ('LH_Pit', 2.25000957482152, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LH_Pit`.'), 'initial_gn_rh_hyp': ('GnRH_Hyp', 0.740638780629751, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GnRH_Hyp`.'), 'initial_gn_rh_pit': ('GnRH_Pit', 0.219992404098564, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `GnRH_Pit`.'), 'initial_fsh_bld': ('FSH_Bld', 0.0168604631992291, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FSH_Bld`.'), 'initial_lh_bld': ('LH_Bld', 0.00633682772990623, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `LH_Bld`.'), 'initial_fsh_pit': ('FSH_Pit', 0.00579108659591004, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FSH_Pit`.')}
    _HEADLINE_OUTPUTS = {'lh_pit': ('LH_Pit', 'native SBML value', 'LH_Pit. Maps to SBML symbol `LH_Pit`.'), 'gn_rh_hyp': ('GnRH_Hyp', 'native SBML value', 'GnRH_Hyp. Maps to SBML symbol `GnRH_Hyp`.'), 'gn_rh_pit': ('GnRH_Pit', 'native SBML value', 'GnRH_Pit. Maps to SBML symbol `GnRH_Pit`.'), 'fsh_bld': ('FSH_Bld', 'native SBML value', 'FSH_Bld. Maps to SBML symbol `FSH_Bld`.'), 'lh_bld': ('LH_Bld', 'native SBML value', 'LH_Bld. Maps to SBML symbol `LH_Bld`.'), 'fsh_pit': ('FSH_Pit', 'native SBML value', 'FSH_Pit. Maps to SBML symbol `FSH_Pit`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000481.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
