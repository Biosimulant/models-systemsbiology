# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Wu2006_ATPsynthesis_SkeletalMuscle."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wu2006AtpsynthesisSkeletalmuscleModel1006230034Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Wu2006_ATPsynthesis_SkeletalMuscle."""

    _SBML_ID = 'MODEL1006230034'
    _TITLE = 'Wu2006_ATPsynthesis_SkeletalMuscle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['pH_x', 'K_x', 'Mg_x', 'NADH_x', 'Q_x', 'Cox_x', 'ATP_x', 'ADP_x', 'ATP_mx', 'ADP_mx', 'PI_x', 'ATP_i', 'ADP_i', 'AMP_i', 'ATP_mi', 'ADP_mi', 'PI_i', 'Mg_i', 'ATP_c', 'ADP_c', 'AMP_c', 'ATP_mc', 'ADP_mc', 'PI_c', 'Mg_c', 'PCr_c', 'deltaPsi']
    _SPECIES_LABELS = {'pH_x': 'PH X', 'K_x': 'K X', 'Mg_x': 'Mg X', 'NADH_x': 'NADH X', 'Q_x': 'Q X', 'Cox_x': 'Cox X', 'ATP_x': 'ATP X', 'ADP_x': 'ADP X', 'ATP_mx': 'ATP Mx', 'ADP_mx': 'ADP Mx', 'PI_x': 'PI X', 'ATP_i': 'ATP I', 'ADP_i': 'ADP I', 'AMP_i': 'AMP I', 'ATP_mi': 'ATP Mi', 'ADP_mi': 'ADP Mi', 'PI_i': 'PI I', 'Mg_i': 'Mg I', 'ATP_c': 'ATP C', 'ADP_c': 'ADP C', 'AMP_c': 'AMP C', 'ATP_mc': 'ATP Mc', 'ADP_mc': 'ADP Mc', 'PI_c': 'PI C', 'Mg_c': 'Mg C', 'PCr_c': 'PCr C', 'deltaPsi': 'DeltaPsi'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_model_state_q_x': ('Q_x', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Q_x`.'), 'initial_pi_x': ('PI_x', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI_x`.'), 'initial_pi_i': ('PI_i', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI_i`.'), 'initial_pi_c': ('PI_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PI_c`.'), 'initial_ph_x': ('pH_x', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pH_x`.'), 'initial_p_cr_c': ('PCr_c', 0.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCr_c`.')}
    _HEADLINE_OUTPUTS = {'q_x': ('Q_x', 'native SBML value', 'Q X. Maps to SBML symbol `Q_x`.'), 'pi_x': ('PI_x', 'native SBML value', 'PI X. Maps to SBML symbol `PI_x`.'), 'pi_i': ('PI_i', 'native SBML value', 'PI I. Maps to SBML symbol `PI_i`.'), 'pi_c': ('PI_c', 'native SBML value', 'PI C. Maps to SBML symbol `PI_c`.'), 'ph_x': ('pH_x', 'native SBML value', 'PH X. Maps to SBML symbol `pH_x`.'), 'p_cr_c': ('PCr_c', 'native SBML value', 'PCr C. Maps to SBML symbol `PCr_c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230034.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
