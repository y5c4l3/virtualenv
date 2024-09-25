from __future__ import annotations

from virtualenv.activation.via_template import ViaTemplateActivator


class PowerShellActivator(ViaTemplateActivator):
    def templates(self):
        yield "activate.ps1"

    @staticmethod
    def quote(string):
        return f"'{string.replace("'", "''")}'"


__all__ = [
    "PowerShellActivator",
]
