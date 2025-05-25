 4-port-MIMO-antenna-design
 Step 1.
# Calculate the resonant frequency of FMSIW cavity 
# Calculate the upper and lower opearting frequencies with effective cavity dimensions 
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

Step 2: Design the antenna with the calculated dimensions in the 3D electromagnetic simulation solver “CST Microwave Studio 2022.”

Step 3: Design a Full-Mode Substrate Integrated Waveguide (FMSIW) cavity in the simulator using the dimensions calculated in the code.

Step 4: Design and optimize the 2-port antenna using HMSIW (Half-Mode SIW) cavities.

Step 5: Incorporate rectangular slots and optimize the proposed 4-port MIMO antenna.

Step 6: Design the 4-port MIMO antenna targeting a lower operating frequency of 5 GHz and an upper frequency of 5.8 GHz. The S-parameters (in dB) are calculated over the frequency range of 4 GHz to 7 GHz. Both reflection and isolation parameters are evaluated.

Step 7: Perform a parametric analysis to evaluate the variation of S-parameters with respect to:
Frequency
Slot lengths (ls1, ls2)
Slot positions (k1, k2)
Gap between the cavities (g1)
Cavity dimensions (w1, w2)

Step 8: Fabricate the prototype and experimentally validate its performance by measuring S-parameters, gain, and radiation patterns.
All the graphs are of the manuscripts are drawn in Sigma plots. 

