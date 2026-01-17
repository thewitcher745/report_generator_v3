import copy
import random
from typing import Any

from image.report_generator.report_classes.BaseReport import BaseReport
from static.report_class_mapping import MAPPING
from tg.handler_functions.helpers.calc_report_numbers import calc_report_numbers
from tg.handler_functions.helpers.extra_features import get_extra_features
from tg.handler_functions.helpers.mass_sending import (
    resolve_mass_sending_rule,
    MassSendingRule,
)
from tg.handler_functions.helpers.multiple_config import (
    MIN_TARGET_ADJUSTMENT,
    MAX_TARGET_ADJUSTMENT,
    LEVERAGE_SEQUENCE,
)


def get_requester_chat_id(update) -> int:
    return (
        update.callback_query.message.chat_id
        if update.callback_query
        else update.message.chat_id
    )


def build_multiple_snapshot(user_data: dict[str, Any]) -> dict[str, Any]:
    snapshot = copy.deepcopy(user_data)
    for key in [
        "multiple_queue",
        "multiple_current_index",
        "multiple_n_reports",
        "multiple_mode",
        "current_feature",
    ]:
        snapshot.pop(key, None)
    return snapshot


def reset_user_data_for_next_multiple_report(user_data: dict[str, Any]) -> None:
    preserved_channel = user_data.get("channel")

    for key in [
        "channel",
        "exchange",
        "image_id",
        "template",
        "precision",
        "qr",
        "referral",
        "username",
        "avatar",
        "date",
        "input_date",
        "period_start",
        "period_end",
        "pnl_usd",
        "pnl_percent",
        "input_symbol",
        "input_signal_type",
        "leverage_type",
        "input_leverage",
        "risk_percent",
        "input_entry_price",
        "input_target_price",
        "liq_price",
        "position_size",
        "margin",
    ]:
        user_data.pop(key, None)

    user_data.pop("current_feature", None)

    if preserved_channel is not None:
        user_data["channel"] = preserved_channel


def resolve_report_class(image_id: str) -> type[BaseReport]:
    ReportClass: type[BaseReport] | None = MAPPING.get(image_id, None)
    if ReportClass is None:
        raise ValueError("Report class not found.")
    return ReportClass


def get_mass_sending_destination(
    *, queued: dict[str, Any], requester_chat_id: int
) -> tuple[int, MassSendingRule]:
    channel = str(queued.get("channel") or "")
    exchange = str(queued.get("exchange") or "")
    template = str(queued.get("template") or "")

    rule = resolve_mass_sending_rule(
        channel=channel, exchange=exchange, template=template
    )
    destination_chat_id = rule.user_id or requester_chat_id
    return destination_chat_id, rule


def apply_multiple_mode_leverage_override(
    *, queued: dict[str, Any], counters: dict[str, int]
) -> None:
    if not LEVERAGE_SEQUENCE:
        return
    bundle_index = int(counters.get("global", 0) or 0)

    leverage = LEVERAGE_SEQUENCE[bundle_index % len(LEVERAGE_SEQUENCE)]

    queued["leverage"] = leverage
    queued["input_leverage"] = leverage

    counters["global"] = bundle_index + 1


def build_report_inputs(
    queued: dict[str, Any],
) -> tuple[list[dict[str, Any]], Any, type[BaseReport]]:
    image_id = str(queued.get("image_id") or "")
    report_data_array = calc_report_numbers(queued)
    extra_features = get_extra_features(image_id)
    ReportClass = resolve_report_class(image_id)
    return report_data_array, extra_features, ReportClass


def maybe_adjust_targets_inplace(
    *,
    queued: dict[str, Any],
) -> None:
    precision = queued.get("precision")
    signal_type = (queued.get("signal_type") or "").lower()

    if not (isinstance(precision, int) and precision >= 0):
        return

    if not (MIN_TARGET_ADJUSTMENT <= MAX_TARGET_ADJUSTMENT):
        return

    if signal_type not in {"long", "short"}:
        return

    pip_size = 10 ** (-precision)

    targets = queued.get("targets")
    if isinstance(targets, list) and targets:
        adjusted_targets: list[Any] = []
        for t in targets:
            try:
                adjustment_pips = random.randint(
                    MIN_TARGET_ADJUSTMENT, MAX_TARGET_ADJUSTMENT
                )
                adjustment = adjustment_pips * pip_size
                adjusted = (
                    float(t) - adjustment
                    if signal_type == "long"
                    else float(t) + adjustment
                )
                adjusted_targets.append(round(adjusted, precision))
            except Exception:
                adjusted_targets.append(t)
        queued["targets"] = adjusted_targets
        return
