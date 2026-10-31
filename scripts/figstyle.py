"""Shared matplotlib styling for the study's figures: validated categorical palette, thin marks, recessive axes,
light and dark exports (PNG + SVG). Import and call `setup()` once; use `save(fig, name)`."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
CAT_LIGHT=["#2a78d6","#eb6834","#1baf7a","#eda100","#e87ba4","#008300","#6250d6","#e34948"]
CAT_DARK=["#3987e5","#d95926","#199e70","#c98500","#d55181","#008300","#9085e9","#e66767"]
SEQ=["#cde2fb","#b7d3f6","#9ec5f4","#86b6ef","#6da7ec","#5598e7","#3987e5","#2a78d6","#256abf","#1c5cab","#184f95","#104281","#0d366b"]
DIV_BLUE,DIV_RED="#2a78d6","#e34948"
THEMES={"light":dict(surface="#fcfcfb",page="#f9f9f7",ink="#0b0b0b",ink2="#52514e",muted="#898781",grid="#e1e0d9",axis="#c3c2b7",cat=CAT_LIGHT,mid="#f0efec"),
        "dark":dict(surface="#1a1a19",page="#0d0d0d",ink="#f0efec",ink2="#c3c2b7",muted="#898781",grid="#2c2c2a",axis="#383835",cat=CAT_DARK,mid="#383835")}
FIGDIR="/home/user/embodied-ai-governance-v4/figures/"
def setup(theme="light"):
    t=THEMES[theme]
    rcParams.update({"font.family":["DejaVu Sans"],"font.size":9,"axes.titlesize":10,"axes.titleweight":"semibold","axes.labelsize":9,"xtick.labelsize":8,"ytick.labelsize":8,"legend.fontsize":8,
        "figure.facecolor":t["surface"],"axes.facecolor":t["surface"],"savefig.facecolor":t["surface"],"text.color":t["ink"],"axes.labelcolor":t["ink2"],"xtick.color":t["ink2"],"ytick.color":t["ink2"],
        "axes.edgecolor":t["axis"],"axes.linewidth":0.8,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"grid.color":t["grid"],"grid.linewidth":0.6,"grid.linestyle":"-","axes.axisbelow":True,
        "xtick.major.size":0,"ytick.major.size":0,"legend.frameon":False,"figure.dpi":150,"savefig.dpi":200,"axes.prop_cycle":matplotlib.cycler(color=t["cat"]),"lines.linewidth":1.8,"patch.linewidth":0})
    return t
def save(fig,name,theme="light",formats=("png","svg")):
    for f in formats: fig.savefig(f"{FIGDIR}{name}{'' if theme=='light' else '_dark'}.{f}",bbox_inches="tight")
    plt.close(fig)
def hbar(ax,labels,values,color=None,label_values=True,theme="light"):
    t=THEMES[theme]; color=color or t["cat"][0]
    bars=ax.barh(labels,values,color=color,height=0.62)
    for b in bars: b.set_linewidth(0)
    ax.invert_yaxis(); ax.set_axisbelow(True); ax.xaxis.grid(True); ax.yaxis.grid(False)
    if label_values:
        mx=max(values) if len(values) else 1
        for b,v in zip(bars,values): ax.text(b.get_width()+mx*0.01,b.get_y()+b.get_height()/2,f"{v:g}",va="center",ha="left",fontsize=7.5,color=t["ink2"])
    return bars
