import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"]
searches = [30, 43, 49, 56, 62]
direct = [47, 60, 63, 51, 51]
social_media = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.25

# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(x - width, searches, width, label='Searches')
ax.bar(x, direct, width, label='Direct')
ax.bar(x + width, social_media, width, label='Social Media')

# Labels and formatting
ax.set_ylabel("Visitors (in thousands)")
ax.set_xlabel("Months")
ax.set_title("Visitors by Web Traffic Sources")
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

plt.tight_layout()
plt.show()
