import math
# Constants
c = 3e11  # Speed of light in mm/s
m = 1     # Dominant mode
n = 1     # Dominant mode
d = 0.8   # mm
s = 1.1   # mm

# Physical widths of the cavities in mm
w_1 = 29.5  # Cavity 1
w_2 = 25.5  # Cavity 2

# Effective dielectric constant (assumed for substrate, e.g., Rogers)
epsilon_reff = 2.2

# Calculate effective widths w_1eff and w_2eff from equations (3) and (4)
delta = (d ** 2) / (0.95 * s)
w_1eff = w_1 - delta
w_2eff = w_2 - delta

# Compute f(FM) using the general frequency formula
f_FM = (c / (2 * math.sqrt(epsilon_reff))) * math.sqrt((m / w_1eff) ** 2 + (n / w_2eff) ** 2)  # in Hz
f_FM_GHz = f_FM / 1e9

# Compute lower cutoff frequency fL110(HM)
fL110 = c / (w_1eff * math.sqrt(2 * epsilon_reff))  # in Hz
fL110_GHz = fL110 / 1e9

# Compute upper cutoff frequency fH110(HM)
fH110 = c / (w_2eff * math.sqrt(2 * epsilon_reff))  # in Hz
fH110_GHz = fH110 / 1e9

# Print results
print(f"Effective width w_1eff: {w_1eff:.4f} mm")
print(f"Effective width w_2eff: {w_2eff:.4f} mm")
print(f"\nf(FM): {f_FM_GHz:.4f} GHz (general mode frequency)")
print(f"fL110(HM): {fL110_GHz:.4f} GHz (lower cutoff frequency for larger cavity)")
print(f"fH110(HM): {fH110_GHz:.4f} GHz (upper cutoff frequency for smaller cavity)")