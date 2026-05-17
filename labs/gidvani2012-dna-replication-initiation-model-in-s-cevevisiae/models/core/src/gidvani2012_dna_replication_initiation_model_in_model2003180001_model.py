# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Gidvani2012 - DNA replication initiation model in S. Cevevisiae."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gidvani2012DnaReplicationInitiationModelInModel2003180001Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Gidvani2012 - DNA replication initiation model in S. Cevevisiae."""

    _SBML_ID = 'MODEL2003180001'
    _TITLE = 'Gidvani2012 - DNA replication initiation model in S. Cevevisiae'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['rc1', 'rc2', 'cdt1c', 'mcmc', 'cdt1n', 'clb5', 'mcmn', 'rc3', 'rc4', 'rc5', 'rc6', 'cdc45n', 'dbf4n', 'fork', 'rc7', 'cdc6n', 'mcm_cdt1n', 'rc_total', 'cdt1_total', 'mcm_total', 'cdc45_total']
    _SPECIES_LABELS = {'rc1': 'rc1', 'rc2': 'rc2', 'cdt1c': 'cdt1c', 'mcmc': 'mcmc', 'cdt1n': 'cdt1n', 'clb5': 'clb5', 'mcmn': 'mcmn', 'rc3': 'rc3', 'rc4': 'rc4', 'rc5': 'rc5', 'rc6': 'rc6', 'cdc45n': 'cdc45n', 'dbf4n': 'dbf4n', 'fork': 'fork', 'rc7': 'rc7', 'cdc6n': 'cdc6n', 'mcm_cdt1n': 'mcm_cdt1n', 'rc_total': 'rc_total', 'cdt1_total': 'cdt1_total', 'mcm_total': 'mcm_total', 'cdc45_total': 'cdc45_total'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cdt1c': ('cdt1c', 2000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cdt1c`.'), 'initial_cdt1_total': ('cdt1_total', 2000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cdt1_total`.'), 'initial_cdc45n': ('cdc45n', 900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cdc45n`.'), 'initial_cdc45_total': ('cdc45_total', 900.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `cdc45_total`.'), 'initial_rc_total': ('rc_total', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rc_total`.'), 'initial_model_state_rc7': ('rc7', 300.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rc7`.')}
    _HEADLINE_OUTPUTS = {'cdt1c': ('cdt1c', 'native SBML value', 'cdt1c. Maps to SBML symbol `cdt1c`.'), 'cdt1_total': ('cdt1_total', 'native SBML value', 'cdt1_total. Maps to SBML symbol `cdt1_total`.'), 'cdc45n': ('cdc45n', 'native SBML value', 'cdc45n. Maps to SBML symbol `cdc45n`.'), 'cdc45_total': ('cdc45_total', 'native SBML value', 'cdc45_total. Maps to SBML symbol `cdc45_total`.'), 'rc_total': ('rc_total', 'native SBML value', 'rc_total. Maps to SBML symbol `rc_total`.'), 'rc7': ('rc7', 'native SBML value', 'rc7. Maps to SBML symbol `rc7`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003180001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
