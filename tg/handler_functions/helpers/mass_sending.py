import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class MassSendingRule:
    user_id: int | None
    message_body: str


def _rule_matches(
    rule: dict[str, Any], *, channel: str, exchange: str, image_id: str, template: str
) -> bool:
    def _eq_or_wildcard(rule_value: Any, actual: str) -> bool:
        if rule_value in (None, "", "*", "any", "default"):
            return True
        return str(rule_value).lower() == actual.lower()

    return (
        _eq_or_wildcard(rule.get("channel"), channel)
        and _eq_or_wildcard(rule.get("exchange"), exchange)
        and _eq_or_wildcard(rule.get("image_id"), image_id)
        and _eq_or_wildcard(rule.get("template"), template)
    )


def load_mass_sending_rules() -> dict[str, Any]:
    rules_path = (
        Path(__file__).resolve().parents[3] / "static" / "mass_sending_rules.json"
    )
    with rules_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def resolve_mass_sending_rule(
    *, channel: str, exchange: str, image_id: str, template: str
) -> MassSendingRule:
    data = load_mass_sending_rules()

    for rule in data.get("rules", []) or []:
        if _rule_matches(
            rule,
            channel=channel,
            exchange=exchange,
            image_id=image_id,
            template=template,
        ):
            return MassSendingRule(
                user_id=rule.get("user_id"),
                message_body=str(rule.get("message_body") or ""),
            )

    default = data.get("default", {}) or {}
    return MassSendingRule(
        user_id=default.get("user_id"),
        message_body=str(default.get("message_body") or ""),
    )
