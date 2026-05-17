# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Dedicated visualisation model for systems-biology SBML labs."""
from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec


GROUP_TITLES = {
    "signaling": ("Signalling response", "Signal-transduction variables over time."),
    "metabolism": ("Metabolic response", "Metabolic pools or flux-linked states over time."),
    "gene_regulation": ("Gene regulation", "Gene-expression and regulatory states over time."),
    "physiology": ("Physiology and tissue state", "Physiological source states over time."),
    "infection_immunity": ("Infection and immunity", "Host, pathogen, or immune states over time."),
    "growth_fate": ("Growth and fate", "Growth, death, tumour, or cell-fate states over time."),
    "core_system_state": ("Core system states", "Conservative trace of source-defined model states."),
}


def _signal_value(signal: BioSignal | None) -> Any:
    if signal is None:
        return None
    value = getattr(signal, "value", signal)
    if isinstance(value, Mapping) and set(value.keys()) == {"payload"}:
        return value["payload"]
    return value


def _num(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


class SystemsBiologyVisualisationModel(BioModule):
    """Render source-traceable visual summaries from systems-biology SBML outputs."""

    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = str(lab_title)
        self.question = str(question)
        self.answer_focus = str(answer_focus)
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {}
        self._summary: dict[str, Mapping[str, Any]] = {}
        self._labels: dict[str, dict[str, str]] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        summary_schema = {
            "duration_simulated": "float",
            "observable_count": "int",
            "largest_change_observable": "str",
            "largest_change_magnitude": "float",
            "peak_observable": "str",
            "peak_value": "float",
        }
        for source in self.sources:
            alias = str(source["alias"])
            ids = [str(item.get("id")) for item in source.get("observables", []) if item.get("id")]
            specs[f"{alias}_state"] = SignalSpec.record(schema={"payload": "json"}, description="Full SBML state record.")
            specs[f"{alias}_summary"] = SignalSpec.record(schema=summary_schema, description="SBML run summary.")
            specs[f"{alias}_species_labels"] = SignalSpec.record(schema={"payload": "json"}, description="Observable display labels.")
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._inputs = {}
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._summary = {}
        self._labels = {}

    def reset(self) -> None:
        self.setup()

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        for source in self.sources:
            alias = str(source["alias"])
            state = _signal_value(self._inputs.get(f"{alias}_state"))
            if isinstance(state, Mapping):
                row = {"t": float(getattr(self._inputs.get(f"{alias}_state"), "emitted_at", end))}
                for key, value in state.items():
                    number = _num(value)
                    if number is not None:
                        row[str(key)] = number
                if len(row) > 1:
                    history = self._history.setdefault(alias, [])
                    if not history or abs(row["t"] - history[-1]["t"]) > 1e-12:
                        history.append(row)
            summary = _signal_value(self._inputs.get(f"{alias}_summary"))
            if isinstance(summary, Mapping):
                self._summary[alias] = dict(summary)
            labels = _signal_value(self._inputs.get(f"{alias}_species_labels"))
            if isinstance(labels, Mapping):
                self._labels[alias] = {str(k): str(v) for k, v in labels.items()}

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            history = self._history.get(alias) or []
            if not history:
                continue
            observables = self._observables(alias, source, history)
            visuals.append(self._qa(alias, observables, history))
            timeseries = self._timeseries(source, observables, history)
            if timeseries is not None:
                visuals.append(timeseries)
            ranges = self._ranges(source, observables, history)
            if ranges is not None:
                visuals.append(ranges)
            snapshot = self._snapshot(source, observables, history)
            if snapshot is not None:
                visuals.append(snapshot)
            scatter = self._scatter(source, observables, history)
            if scatter is not None:
                visuals.append(scatter)
        return visuals or None

    def _observables(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> list[dict[str, str]]:
        latest = history[-1]
        configured = []
        for item in source.get("observables", []):
            obs_id = str(item.get("id") or "")
            if obs_id in latest:
                configured.append({
                    "id": obs_id,
                    "label": str(item.get("label") or self._labels.get(alias, {}).get(obs_id) or obs_id),
                    "group": str(item.get("group") or "core_system_state"),
                })
        if configured:
            return configured
        return [{"id": key, "label": self._labels.get(alias, {}).get(key, key), "group": "core_system_state"} for key in latest if key != "t"][:8]

    def _qa(self, alias: str, observables: list[dict[str, str]], history: list[dict[str, float]]) -> dict[str, Any]:
        summary = self._summary.get(alias, {})
        largest = str(summary.get("largest_change_observable") or "")
        label_by_id = {item["id"]: item["label"] for item in observables}
        change = _num(summary.get("largest_change_magnitude")) or 0.0
        if abs(change) < 1e-12:
            answer = "The sampled baseline run is near steady state for the selected source observables."
            evidence = "No selected observable showed a meaningful excursion over the sampled window."
        else:
            mover = label_by_id.get(largest, largest or "the largest-changing observable")
            answer = f"The run shows measurable activity led by {mover}."
            evidence = f"{mover} had the largest reported excursion ({change:.4g}) in native SBML units."
        groups = sorted({GROUP_TITLES.get(item["group"], GROUP_TITLES["core_system_state"])[0] for item in observables})
        return {
            "render": "table",
            "description": "Direct scientific answer for this lab run.",
            "data": {
                "title": f"{self.lab_title} - run interpretation",
                "columns": ["Prompt", "Answer"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", answer],
                    ["Evidence", evidence],
                    ["Dominant module", ", ".join(groups) or "Core source states"],
                    ["Caveat", "Values are native SBML quantities; the visualisation does not rewrite or reinterpret model equations."],
                ],
            },
        }

    def _timeseries(self, source: Mapping[str, Any], observables: list[dict[str, str]], history: list[dict[str, float]]) -> dict[str, Any] | None:
        ranked = sorted(observables, key=lambda item: self._range(history, item["id"]), reverse=True)[:8]
        series = [
            {"name": item["label"], "points": [[row["t"], row[item["id"]]] for row in history if item["id"] in row]}
            for item in ranked
        ]
        series = [item for item in series if item["points"]]
        if not series:
            return None
        group = ranked[0]["group"] if ranked else "core_system_state"
        title, description = GROUP_TITLES.get(group, GROUP_TITLES["core_system_state"])
        return {
            "render": "timeseries",
            "description": description,
            "data": {"title": f"{source.get('title') or 'Source model'} - {title}", "x_label": "Model time", "y_label": "Native SBML value", "series": series},
        }

    def _ranges(self, source: Mapping[str, Any], observables: list[dict[str, str]], history: list[dict[str, float]]) -> dict[str, Any] | None:
        items = [{"label": item["label"], "value": self._range(history, item["id"])} for item in observables]
        items = [item for item in sorted(items, key=lambda x: x["value"], reverse=True)[:10] if item["value"] > 0]
        if not items:
            return None
        return {"render": "bar", "description": "Selected source variables ranked by within-run excursion.", "data": {"title": f"{source.get('title') or 'Source model'} - largest activity ranges", "items": items, "x_label": "Model variable", "y_label": "Max-min range"}}

    def _snapshot(self, source: Mapping[str, Any], observables: list[dict[str, str]], history: list[dict[str, float]]) -> dict[str, Any] | None:
        latest = history[-1]
        items = [{"label": item["label"], "value": abs(float(latest[item["id"]]))} for item in observables if item["id"] in latest]
        items = [item for item in sorted(items, key=lambda x: x["value"], reverse=True)[:10] if item["value"] > 0]
        if not items:
            return None
        return {"render": "bar", "description": "Final-state magnitude for selected source variables.", "data": {"title": f"{source.get('title') or 'Source model'} - final state snapshot", "items": items, "x_label": "Model variable", "y_label": "Absolute final native SBML value"}}

    def _scatter(self, source: Mapping[str, Any], observables: list[dict[str, str]], history: list[dict[str, float]]) -> dict[str, Any] | None:
        ranked = sorted(observables, key=lambda item: self._range(history, item["id"]), reverse=True)
        if len(ranked) < 2:
            return None
        x_item, y_item = ranked[0], ranked[1]
        if self._range(history, x_item["id"]) <= 0 or self._range(history, y_item["id"]) <= 0:
            return None
        points = [{"x": row[x_item["id"]], "y": row[y_item["id"]], "series": "trajectory"} for row in history if x_item["id"] in row and y_item["id"] in row]
        if not points:
            return None
        return {"render": "scatter", "description": "Phase portrait for the two most active selected source variables.", "data": {"title": f"{source.get('title') or 'Source model'} - activity phase portrait", "x_label": x_item["label"], "y_label": y_item["label"], "connect_points": True, "points": points}}

    @staticmethod
    def _range(history: list[dict[str, float]], key: str) -> float:
        values = [row[key] for row in history if key in row]
        return max(values) - min(values) if values else 0.0
