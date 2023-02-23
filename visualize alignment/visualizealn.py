from Bio import AlignIO
import matplotlib.pyplot as plt

# load alignment file (in this case, a FASTA file)
alignment = AlignIO.read("alignment.fasta", "fasta")

# set font size and dpi for high resolution image
font_size = 18
dpi = 300

# create figure and axis objects
fig, ax = plt.subplots(figsize=(20,10))

# plot alignment as heatmap
ax.imshow(alignment[:, :], interpolation='nearest', cmap='gist_ncar', aspect='auto')

# set axis labels and tick labels
ax.set_xticks(range(len(alignment[0])))
ax.set_xticklabels([i + 1 for i in range(len(alignment[0]))], fontsize=font_size)
ax.set_yticks(range(len(alignment)))
ax.set_yticklabels([rec.id for rec in alignment], fontsize=font_size)

# set axis limits
ax.set_xlim(-0.5, len(alignment[0]) - 0.5)
ax.set_ylim(len(alignment) - 0.5, -0.5)

# set axis titles
plt.xlabel("Alignment position", fontsize=font_size)
plt.ylabel("Sequence ID", fontsize=font_size)

# set figure title
plt.title("Multiple Sequence Alignment", fontsize=font_size+2)

# set tight layout and save image
fig.tight_layout()
plt.savefig("alignment.png", dpi=dpi)
