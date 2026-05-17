# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Parmar2019 - Iron Mouse PV3 - tracer."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Parmar2019IronMousePv3TracerModel1805140002Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Parmar2019 - Iron Mouse PV3 - tracer."""

    _SBML_ID = 'MODEL1805140002'
    _TITLE = 'Parmar2019 - Iron Mouse PV3 - tracer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FeDuo', 'FeDuo_0', 'FeRBC', 'FeRBC_0', 'FeSpleen', 'FeSpleen_0', 'FeLiver', 'FeLiver_0', 'Fe2Tf', 'NTBI', 'Tf', 'Fe1Tf', 'Hepcidin', 'Fe2Tf_0', 'Fe1Tf_0', 'NTBI_0', 'Fe2Tf_', 'EPO', 'FeRest', 'FeOutside', 'FeRest_0', 'FeOutside_0', 'FeBM', 'FeBM_0']
    _SPECIES_LABELS = {'FeDuo': 'FeDuo*', 'FeDuo_0': 'FeDuo', 'FeRBC': 'FeRBC*', 'FeRBC_0': 'FeRBC', 'FeSpleen': 'FeSpleen*', 'FeSpleen_0': 'FeSpleen', 'FeLiver': 'FeLiver*', 'FeLiver_0': 'FeLiver', 'Fe2Tf': 'Fe2Tf*', 'NTBI': 'NTBI*', 'Tf': 'Tf', 'Fe1Tf': 'Fe1Tf*', 'Hepcidin': 'Hepcidin', 'Fe2Tf_0': 'Fe2Tf', 'Fe1Tf_0': 'Fe1Tf', 'NTBI_0': 'NTBI', 'Fe2Tf_': 'Fe2Tf**', 'EPO': 'EPO', 'FeRest': 'FeRest*', 'FeOutside': 'FeOutside*', 'FeRest_0': 'FeRest', 'FeOutside_0': 'FeOutside', 'FeBM': 'FeBM', 'FeBM_0': 'FeBM*'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fe_rbc': ('FeRBC_0', 0.023, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRBC_0`.'), 'initial_fe_duo': ('FeDuo_0', 0.0100222, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeDuo_0`.'), 'initial_fe_spleen': ('FeSpleen_0', 0.00226838, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeSpleen_0`.'), 'initial_fe_liver': ('FeLiver_0', 0.0013, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeLiver_0`.'), 'initial_fe_rest': ('FeRest_0', 0.00040176, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRest_0`.'), 'initial_fe2_tf': ('Fe2Tf_0', 1.89625e-05, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fe2Tf_0`.')}
    _HEADLINE_OUTPUTS = {'fe_rbc': ('FeRBC_0', 'native SBML value', 'FeRBC. Maps to SBML symbol `FeRBC_0`.'), 'fe_duo': ('FeDuo_0', 'native SBML value', 'FeDuo. Maps to SBML symbol `FeDuo_0`.'), 'fe_spleen': ('FeSpleen_0', 'native SBML value', 'FeSpleen. Maps to SBML symbol `FeSpleen_0`.'), 'fe_liver': ('FeLiver_0', 'native SBML value', 'FeLiver. Maps to SBML symbol `FeLiver_0`.'), 'fe_rest': ('FeRest_0', 'native SBML value', 'FeRest. Maps to SBML symbol `FeRest_0`.'), 'fe2_tf': ('Fe2Tf_0', 'native SBML value', 'Fe2Tf. Maps to SBML symbol `Fe2Tf_0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1805140002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
