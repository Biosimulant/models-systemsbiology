# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Proctor2006_telomere."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Proctor2006TelomereBiomd0000000087Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Proctor2006_telomere."""

    _SBML_ID = 'BIOMD0000000087'
    _TITLE = 'Proctor2006_telomere'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ctelo', 'Utelo', 'Cdc13', 'Rad17Utelo', 'Rad17', 'Rad24', 'RPA', 'Mec1', 'ssDNA', 'RPAssDNA', 'RPAssDNA1', 'RPAssDNA2', 'Mec1RPAssDNA', 'ExoXI', 'ExoXA', 'Exo1I', 'Exo1A', 'Rad9I', 'Rad9A', 'Rad53I', 'Rad53A', 'Chk1I', 'Chk1A', 'Dun1I', 'Dun1A', 'ATP', 'ADP', 'Rad9Kin', 'recovery', 'G1', 'S', 'G2', 'M', 'G1cyclin', 'Scyclin', 'G2cyclin', 'Mcyclin', 'G1CdkI', 'G1CdkA', 'SCdkI', 'SCdkA', 'G2CdkI', 'G2CdkA', 'MCdkI', 'MCdkA', 'G1Soff', 'G1Son', 'SG2off', 'SG2on', 'G2Moff', 'G2Mon', 'MG1off', 'MG1on', 'sink', 'budscar']
    _SPECIES_LABELS = {'Ctelo': 'Ctelo', 'Utelo': 'Utelo', 'Cdc13': 'Cdc13', 'Rad17Utelo': 'Rad17Utelo', 'Rad17': 'Rad17', 'Rad24': 'Rad24', 'RPA': 'RPA', 'Mec1': 'Mec1', 'ssDNA': 'SsDNA', 'RPAssDNA': 'RPAssDNA', 'RPAssDNA1': 'RPAssDNA1', 'RPAssDNA2': 'RPAssDNA2', 'Mec1RPAssDNA': 'Mec1RPAssDNA', 'ExoXI': 'ExoXI', 'ExoXA': 'ExoXA', 'Exo1I': 'Exo1I', 'Exo1A': 'Exo1A', 'Rad9I': 'Rad9I', 'Rad9A': 'Rad9A', 'Rad53I': 'Rad53I', 'Rad53A': 'Rad53A', 'Chk1I': 'Chk1I', 'Chk1A': 'Chk1A', 'Dun1I': 'Dun1I', 'Dun1A': 'Dun1A', 'ATP': 'ATP', 'ADP': 'ADP', 'Rad9Kin': 'Rad9Kin', 'recovery': 'Recovery', 'G1': 'G1', 'S': 'S', 'G2': 'G2', 'M': 'M', 'G1cyclin': 'G1cyclin', 'Scyclin': 'Scyclin', 'G2cyclin': 'G2cyclin', 'Mcyclin': 'Mcyclin', 'G1CdkI': 'G1CdkI', 'G1CdkA': 'G1CdkA', 'SCdkI': 'SCdkI', 'SCdkA': 'SCdkA', 'G2CdkI': 'G2CdkI', 'G2CdkA': 'G2CdkA', 'MCdkI': 'MCdkI', 'MCdkA': 'MCdkA', 'G1Soff': 'G1Soff', 'G1Son': 'G1Son', 'SG2off': 'SG2off', 'SG2on': 'SG2on', 'G2Moff': 'G2Moff', 'G2Mon': 'G2Mon', 'MG1off': 'MG1off', 'MG1on': 'MG1on', 'sink': 'Sink', 'budscar': 'Budscar'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_atp': ('ATP', 10000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`.'), 'initial_model_state_adp': ('ADP', 1000.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`.'), 'initial_scyclin': ('Scyclin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Scyclin`.'), 'initial_mcyclin': ('Mcyclin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Mcyclin`.'), 'initial_g2cyclin': ('G2cyclin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G2cyclin`.'), 'initial_g1cyclin': ('G1cyclin', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G1cyclin`.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'scyclin': ('Scyclin', 'native SBML value', 'Scyclin. Maps to SBML symbol `Scyclin`.'), 'mcyclin': ('Mcyclin', 'native SBML value', 'Mcyclin. Maps to SBML symbol `Mcyclin`.'), 'g2cyclin': ('G2cyclin', 'native SBML value', 'G2cyclin. Maps to SBML symbol `G2cyclin`.'), 'g1cyclin': ('G1cyclin', 'native SBML value', 'G1cyclin. Maps to SBML symbol `G1cyclin`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000087.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
