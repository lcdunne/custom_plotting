sci_rc = {
    "figure.figsize": [5, 5],
    "figure.autolayout": True,
    "font.size": 24,
    "font.family": "cambria",
    "axes.linewidth": 2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.major.width": 2,
    "ytick.major.width": 2,
    "lines.linewidth": 2}

bar_kw = {
    "edgecolor": "k",
    "linewidth": 2,
    "errcolor": "k",
    "errwidth": 2
}

scatter_kw = {
    "marker":"o",
    "s":100,
    "linewidth":1,
    "facecolors": "none",
    "edgecolors":"k"
}

palettes = {
    "redgrey": ["#de2d26", "#bdbdbd"],
    "greengrey": ["#31a354", "#bdbdbd"],
    "bluegrey": ["#3182bd", "#bdbdbd"],
    "redgrey_dark": ["#de2d26", "#636363"],
    "greengrey_dark": ["#31a354", "#636363"],
    "bluegrey_dark": ["#3182bd", "#636363"],
    "set99": ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"],
    "set99b":["#999999", "#377eb8", "#e41a1c", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf"]
}

palettes = {
    **palettes,
    **{f"{k}_r": v[::-1] for k, v in palettes.items()}
}
