# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule wrapper for Banaji2005_Brain_Cell_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Banaji2005BrainCellMetabolismModel4992089662Model(TelluriumSBMLBioModule):
    """Faithful SBML execution wrapper for Banaji2005_Brain_Cell_Metabolism."""

    _SBML_ID = 'MODEL4992089662'
    _TITLE = 'Banaji2005_Brain_Cell_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['_Ad', '_eAd', '_ADP', '_mADP', '_AKG', '_AMP', '_ATP', '_mATP', '_mBiC', '_BiC', '_eBiC', '_mCO2', '_CO2', '_eCO2', '_Cr', '_mFAD', '_mFADH', '_gluc', '_egluc', '_Hy', '_mHy', '_eHy', '_Phos', '_mPhos', '_L0', '_eL0', '_lac', '_eL', '_NAD', '_mNAD', '_NADH', '_mNADH', '_Ox', '_mO2', '_O2', '_eO2', '_PCr', '_eK', '_K', '_Py0', '_mPy0', '_ePy0', 'PbufH', 'Pbuf', '_Na', '_eNa', '_suc']
    _SPECIES_LABELS = {'_Ad': 'adenosine', '_eAd': 'adenosine', '_ADP': 'ADP', '_mADP': 'ADP', '_AKG': 'alpha-ketoglutarate', '_AMP': 'AMP', '_ATP': 'ATP', '_mATP': 'ATP', '_mBiC': 'bicarbonate ion', '_BiC': 'bicarbonate ion', '_eBiC': 'bicarbonate ion', '_mCO2': 'carbon dioxide', '_CO2': 'carbon dioxide', '_eCO2': 'carbon dioxide', '_Cr': 'creatine', '_mFAD': 'FAD', '_mFADH': 'FADH2', '_gluc': 'glucose', '_egluc': 'glucose', '_Hy': 'hydrogen ion', '_mHy': 'hydrogen ion', '_eHy': 'hydrogen ion', '_Phos': 'inorganic phosphate', '_mPhos': 'inorganic phosphate', '_L0': 'lactate', '_eL0': 'lactate', '_lac': 'lactic acid', '_eL': 'lactic acid', '_NAD': 'NAD', '_mNAD': 'NAD', '_NADH': 'NADH', '_mNADH': 'NADH', '_Ox': 'oxaloacetate', '_mO2': 'oxygen', '_O2': 'oxygen', '_eO2': 'oxygen', '_PCr': 'phosphocreatine', '_eK': 'potassium ion', '_K': 'potassium ion', '_Py0': 'pyruvate', '_mPy0': 'pyruvate', '_ePy0': 'pyruvate', 'PbufH': 'sites on cellular proteins bound to protons', 'Pbuf': 'sites on cellular proteins capable of binding protons', '_Na': 'sodium ion', '_eNa': 'sodium ion', '_suc': 'succinate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_sites_on_cellular_proteins_capable_of_binding_protons': ('Pbuf', 10.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pbuf`.'), 'initial_sites_on_cellular_proteins_bound_to_protons': ('PbufH', 2.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PbufH`.'), 'initial_potassium_ion': ('_K', 180.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `_K`.'), 'initial_sodium_ion': ('_eNa', 138.0, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `_eNa`.'), 'initial_bicarbonate_ion': ('_mBiC', 90.9883299405421, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `_mBiC`.'), 'initial_bicarbonate_ion_2': ('_eBiC', 25.0599030317216, 'native SBML value', 'Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `_eBiC`.')}
    _HEADLINE_OUTPUTS = {'sites_on_cellular_proteins_capable_of_binding_protons': ('Pbuf', 'native SBML value', 'sites on cellular proteins capable of binding protons. Maps to SBML symbol `Pbuf`.'), 'sites_on_cellular_proteins_bound_to_protons': ('PbufH', 'native SBML value', 'sites on cellular proteins bound to protons. Maps to SBML symbol `PbufH`.'), 'potassium_ion': ('_K', 'native SBML value', 'potassium ion. Maps to SBML symbol `_K`.'), 'sodium_ion': ('_eNa', 'native SBML value', 'sodium ion. Maps to SBML symbol `_eNa`.'), 'bicarbonate_ion': ('_mBiC', 'native SBML value', 'bicarbonate ion. Maps to SBML symbol `_mBiC`.'), 'bicarbonate_ion_2': ('_eBiC', 'native SBML value', 'bicarbonate ion. Maps to SBML symbol `_eBiC`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL4992089662.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
