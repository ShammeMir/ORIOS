#!/usr/bin/env python3
"""
Generate a publication-ready grouped bar chart for academic paper
Showing self-assessed ideation quality comparing Human-Only vs AI-Augmented conditions
"""

import matplotlib.pyplot as plt
import numpy as np

# Set publication-quality parameters
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300

# Data
categories = ['Novelty Composite', 'Feasibility Composite']

human_only_means = [3.13, 3.92]
human_only_sds = [0.56, 0.53]

ai_augmented_means = [2.75, 3.34]
ai_augmented_sds = [0.43, 0.62]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set the width of bars and positions
bar_width = 0.35
x_pos = np.arange(len(categories))

# Define colors
human_color = '#2E86AB'  # Blue
ai_color = '#F77F00'     # Orange

# Create bars
bars1 = ax.bar(x_pos - bar_width/2, human_only_means, bar_width,
               yerr=human_only_sds, capsize=5,
               label='Human-Only (n=8)', color=human_color,
               error_kw={'elinewidth': 1.5, 'capthick': 1.5},
               edgecolor='black', linewidth=0.7)

bars2 = ax.bar(x_pos + bar_width/2, ai_augmented_means, bar_width,
               yerr=ai_augmented_sds, capsize=5,
               label='AI-Augmented (n=8)', color=ai_color,
               error_kw={'elinewidth': 1.5, 'capthick': 1.5},
               edgecolor='black', linewidth=0.7)

# Add value labels on top of bars
def add_value_labels(bars, means, sds):
    for bar, mean, sd in zip(bars, means, sds):
        height = mean + sd + 0.08  # Position above error bar
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{mean:.2f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

add_value_labels(bars1, human_only_means, human_only_sds)
add_value_labels(bars2, ai_augmented_means, ai_augmented_sds)

# Customize the plot
ax.set_xlabel('Dimension', fontweight='bold')
ax.set_ylabel('Mean Rating (1-5 Likert Scale)', fontweight='bold')
ax.set_title('Figure 1. Self-Assessed Ideation Quality: Novelty and Feasibility Composites',
             fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_ylim(1.0, 5.0)

# Add subtle grid lines for y-axis only
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)  # Grid lines behind bars

# Add legend
ax.legend(loc='upper right', frameon=True, shadow=False,
          fancybox=False, edgecolor='black', framealpha=1)

# Add y-axis ticks at every 0.5
ax.set_yticks(np.arange(1.0, 5.5, 0.5))

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure at high resolution
output_filename = 'ideation_quality_chart.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

print(f"Chart successfully created and saved as '{output_filename}'")
print(f"Resolution: 300 DPI")
print(f"Format: PNG")
print("\nChart Details:")
print("=" * 50)
print(f"Human-Only Novelty: M={human_only_means[0]:.2f}, SD={human_only_sds[0]:.2f}")
print(f"AI-Augmented Novelty: M={ai_augmented_means[0]:.2f}, SD={ai_augmented_sds[0]:.2f}")
print(f"Human-Only Feasibility: M={human_only_means[1]:.2f}, SD={human_only_sds[1]:.2f}")
print(f"AI-Augmented Feasibility: M={ai_augmented_means[1]:.2f}, SD={ai_augmented_sds[1]:.2f}")

# Also display the plot (optional, commented out for headless environments)
# plt.show()
