"""Simple reverb-related feature calculations."""


def decay_ratio(early_energy: float, late_energy: float) -> float:
    if early_energy < 0 or late_energy < 0:
        raise ValueError("energies must be non-negative")
    if early_energy == 0:
        return 0.0
    return min(1.0, late_energy / early_energy)
