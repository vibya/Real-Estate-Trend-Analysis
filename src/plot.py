import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck


def trend(x, y,
          color="blue",
          linewidth=2,
          xscale=None,
          yscale="plain",
          xlabelfontsize=18,
          ylabelfontsize=18,
          xtickfontsize=16,
          ytickfontsize=16,
          titlefontsize=20,
          xlabel="x",
          ylabel="y",
          title=None,
          label="",
          xticks=None,
          yticks=None,
          xtickspace=1,
          xtickformat=None,
          ytickformat=None,
          figzie=(12, 10),
          leftborder=False,
          rightborder=False,
          topborder=True,
          bottomborder=True,
          grid=True,
          ax=None,
          **kwargs):

    n_y = len(y)
    if ax is None:
        fig = plt.figure(figsize=figzie)
        ax = fig.subplots(nrows=1,ncols=1)
    ax.spines["top"].set_visible(topborder)
    ax.spines["bottom"].set_visible(bottomborder)
    ax.spines["right"].set_visible(rightborder)
    ax.spines["left"].set_visible(leftborder)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=xlabelfontsize)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=ylabelfontsize)
    if title is not None:
        ax.set_title(title, fontsize=titlefontsize)

    if yticks is None:
        if yscale == 'log':
            yticks = np.logspace(-4, -1, num=5)
        elif yscale == 'plain':
            yticks = np.linspace(0.9*min(y), 1.1 * max(y), 5).astype(int)

    ax.set_yticks(yticks)
    #ax.set_yticklabels(yticks)
    if xticks is not None:
        ax.set_xticks(xticks[::xtickspace])
        ax.set_xticklabels(xticks[::xtickspace])

    # add horizontal grid lines
    if grid:
        ax.grid(which='both',
                axis='y',
                linestyle='--',
                alpha=0.7,
                color="grey",
                linewidth=1.2,
                )
    if ytickformat == 'sci':
        plt.gca().yaxis.set_major_formatter(tck.FormatStrFormatter('%.0e'))

    ax.plot(x, y,
            color=color,
            linewidth=linewidth,
            label=label,
            **kwargs,)
    ax.xaxis.set_tick_params(width=3, length=6, labelsize=xtickfontsize)
    ax.yaxis.set_tick_params(width=3, length=8, labelsize=ytickfontsize)
    ax.tick_params(which="both", direction="out")
    print(yticks)

    return ax


def scatter(x, y,
            marker: str = "o",
            markersize: int = 6,
            markeredgecolor: str = "black",
            markeredgewidth: float = 1,
            markerfacecolor: str = "black",
            fillstyle: str = "full",
            linestyle: str = "",
            alpha: float = .7,
            xlabel: str = "",
            ylabel: str = "",
            label: str = "",
            title: str = "",
            xlim: object = None,
            ylim: object = None,
            titlefontsize: int = 16,
            labelfontsize: int = 15,
            xtickfontsize: int = 14,
            ytickfontsize: int = 14,
            leftborder=True,
            rightborder=True,
            topborder=True,
            bottomborder=True,
            figsize: tuple = (7, 5),
            dpi=400,
            legend: bool = False,
            grid: bool = True,
            ax: object = None,) :

    # create figure/axis handler
    if ax is None:
        fig = plt.figure(figsize=figsize, dpi=dpi)
        ax = fig.subplots(1, 1)

    ax.spines["top"].set_visible(topborder)
    ax.spines["bottom"].set_visible(bottomborder)
    ax.spines["right"].set_visible(rightborder)
    ax.spines["left"].set_visible(leftborder)

    # scatter plot
    ax.plot(
        x, y,
        marker=marker,
        markersize=markersize,
        markeredgecolor=markeredgecolor,
        markeredgewidth=markeredgewidth,
        markerfacecolor=markerfacecolor,
        fillstyle=fillstyle,
        linestyle=linestyle,
        alpha=alpha,
        label=label,
    )
    # set title
    _ = ax.set_title(
        title,
        fontsize=titlefontsize,
        fontweight="bold"
    )
    # set axis labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.xaxis.label.set_size(labelfontsize)
    ax.yaxis.label.set_size(labelfontsize)

    # set axis ticks
    [tick.label.set_fontsize(xtickfontsize) for tick in ax.xaxis.get_major_ticks()]
    [tick.label.set_fontsize(ytickfontsize) for tick in ax.yaxis.get_major_ticks()]

    # set axis range limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    ax.xaxis.set_tick_params(width=2, length=6)
    ax.yaxis.set_tick_params(width=2, length=6)

    # set legend
    if legend and (label is not ""):
        ax.legend()

    # set grid
    ax.grid(
        grid,
        color="grey",
        linestyle=":",
        linewidth=1.5,
        alpha=0.5)

    return ax


def pie(labels, sizes, explode,
        title=None,
        autopct='%1.0f%%',
        propfontsize=16,
        titlefontsize=16,
        linewidth=3,
        edgecolor="black",
        shadow=False,
        startangle=90,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(nrows=1, ncols=1)

    ax.pie(sizes,
           explode=explode,
           labels=labels,
           autopct=autopct,
           shadow=shadow,
           wedgeprops={'linewidth': linewidth,
                       'edgecolor': edgecolor},
           textprops={'fontsize': propfontsize},
           startangle=startangle,
           )

    ax.set_ylabel("")
    if title is not None:
        ax.set_title(title, fontsize=titlefontsize, fontweight='bold')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    return ax


def bar(height, x=None,
        color="blue",
        opacity=0.6,
        edgecolor="black",
        width=1,
        linewidth=2,
        aligh="center",
        xlabel=None,
        ylabel=None,
        title=None,
        titlefontsize=16,
        xlabelfontsize=15,
        ylabelfontsize=15,
        leftborder=True,
        rightborder=True,
        topborder=True,
        bottomborder=True,
        showlabels=True,
        labelcolor="white",
        labelfontsize=15,
        labelpose=0.7,
        ticklabels=None,
        xticklabelfontsize=14,
        yticklabelfontsize=14,
        xtickrotation=0,
        ytickrotation=0,
        grid=True,
        ax=None,):
    if ax is None:
        fig, ax = plt.subplots(nrows=1, ncols=1)

    ax.spines["top"].set_visible(topborder)
    ax.spines["bottom"].set_visible(bottomborder)
    ax.spines["right"].set_visible(rightborder)
    ax.spines["left"].set_visible(leftborder)

    if x is None:
        x = np.arange(1, len(height)+1, 1).astype(int)
    if ticklabels is None:
        ticklabels = x
    ax.bar(
        x=x,
        height=height,
        color=color,
        alpha=opacity,
        edgecolor=edgecolor,
        linewidth=linewidth,
        tick_label=ticklabels,
        width=width,
        align=aligh,)
    if title is not None:
        _ = ax.set_title(title,
                         fontsize=titlefontsize,
                         fontweight="bold")
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    ax.xaxis.label.set_size(xlabelfontsize)
    ax.yaxis.label.set_size(ylabelfontsize)
    if grid:
        ax.grid(grid, color="grey", linestyle=":", linewidth=1.5, alpha=0.5)

    ax.tick_params(axis="x",
                   direction='out',
                   labelsize=xticklabelfontsize,
                   length=8,
                   width=3,
                   colors='black',
                   labelrotation=xtickrotation)
    ax.tick_params(axis="y",
                   direction='out',
                   labelsize=yticklabelfontsize,
                   length=8,
                   width=3,
                   colors='black',
                   labelrotation=ytickrotation)

    if showlabels:
        for (xi, hi) in zip(x, height):
            ax.text(
                x=xi, y= hi - min(height) * (1-labelpose),
                s="{:333.0f}".format(hi),
                color=labelcolor,
                horizontalalignment="center",
                fontsize=labelfontsize,
                fontweight="bold")

    plt.tight_layout()
    return ax