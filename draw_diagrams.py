"""
Code that draws a visual diagram given the schema information and choice of pattern
1/5/2022
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import sys
from os.path import abspath, dirname, join
from inspect import getfile, currentframe


PAD = 0.3   # padding of rounded negation box

l1 = 4      # horizontal length of output table
l2 = 5      # horizontal length of 1st table
l3 = 5      # horizontal length of 2nd table
l4 = 4      # horizontal length of 3rd table
delta = 0.9 # horizontal distance between tables (layers)


def draw_diagram(table1, table2, table3,
                 attribute11, attribute12, attribute21, attribute22, attribute31,
                 pattern, fig_filename,
                 create_pdf=True, show_pdf=True, create_svg=False, show_plot=False, create_png=False):

    mpl.rcParams['font.family'] = "Arial"
    mpl.rcParams['font.size'] = "32"
    mpl.rcParams['xtick.labelsize'] = 4
    mpl.rcParams['ytick.labelsize'] = 4
    mpl.rcParams['figure.figsize'] = [16, 4]


    def draw_box(ax, left, bottom, width, height,
                 content, facecolor='white', edgecolor='black', textcolor='black', linewidth=2, verticaltextadjustment=0.1):
        """code to draw one single box"""
        rect = plt.Rectangle((left, bottom), width, height,
                             facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth)
        ax.add_patch(rect)

        rx, ry = rect.get_xy()
        cx = rx + rect.get_width()/2
        cy = ry + rect.get_height()/2 - verticaltextadjustment
        ax.annotate(content, (cx, cy),
                    color=textcolor,
                    ha='center', va='center')


    def draw_negation(ax, left, bottom, width, height, pad=PAD):
        """code to draw one single negation rounded rectangle"""
        fancybox = mpatches.FancyBboxPatch((left, bottom), width, height,
                                           facecolor='none',
                                           edgecolor='black',
                                           linestyle = '--',
                                           linewidth=2,
                                           boxstyle=mpatches.BoxStyle("Round", pad=pad))
        ax.add_patch(fancybox)


    fig, ax = plt.subplots()

    w1 = l1
    w2 = w1 + delta
    w3 = w2 + l2
    w4 = w3 + delta
    w5 = w4 + l3
    w6 = w5 + delta
    w7 = w6 + l4


    # -- Draw all boxes
    draw_box(ax, 0, 2, w1, 1, content='Q', facecolor='lightgray', edgecolor='black', textcolor='black')
    draw_box(ax, 0, 1, w1, 1, content=attribute11, facecolor='white', edgecolor='black', textcolor='black')

    draw_box(ax, w2, 2, w3 - w2, 1, content=table1, facecolor='black', edgecolor='black', textcolor='white')
    draw_box(ax, w2, 1, w3 - w2, 1, content=attribute11, facecolor='white', edgecolor='black', textcolor='black')
    draw_box(ax, w2, 0, w3 - w2, 1, content=attribute12, facecolor='white', edgecolor='black', textcolor='black')

    draw_box(ax, w4, 2, w5 - w4, 1, content=table2, facecolor='black', edgecolor='black', textcolor='white')
    draw_box(ax, w4, 1, w5 - w4, 1, content=attribute21, facecolor='white', edgecolor='black', textcolor='black')
    draw_box(ax, w4, 0, w5 - w4, 1, content=attribute22, facecolor='white', edgecolor='black', textcolor='black')

    draw_box(ax, w6, 2, w7 - w6, 1, content=table3, facecolor='black', edgecolor='black', textcolor='white')
    draw_box(ax, w6, 1, w7 - w6, 1, content=attribute31, facecolor='white', edgecolor='black', textcolor='black')


    # -- Draw all joins
    ax.plot([w1, w2], [1.5, 1.5], color='black', linewidth=2)
    ax.plot([w3, w4], [0.5, 0.5], color='black', linewidth=2)
    ax.plot([w6, w5], [1.5, 1.5], color='black', linewidth=2)


    # -- Draw all negation boxes
    if pattern == 2:
        draw_negation(ax, w4, 0, w7 - w4, 3)

    if pattern == 3:
        draw_negation(ax, w4, 0, w5 - w4, 3)

    if pattern == 4:
        draw_negation(ax, w4, 0, w5 - w4, 3)
        draw_negation(ax, w4, 0, w7 - w4, 3, pad=PAD*2)


    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.xlim(-1, 22)
    plt.ylim(-0.5, 3.5)


    # -- Determine path to data *irrespective* of where the file is run from
    current_path = dirname(abspath(getfile(currentframe())))
    figure_directory = join(current_path, 'figs')

    if create_pdf:
        fig_filenamepdf = fig_filename + '.pdf'
        plt.savefig(join(figure_directory, fig_filenamepdf), format='pdf',
                    dpi=None,
                    edgecolor='w',
                    orientation='portrait',
                    transparent=False,
                    bbox_inches='tight',
                    pad_inches=0.05,
                    # frameon=None
                    )
    if show_pdf:
        def showfig(filename):
            open_cmd = {'linux': 'xdg-open', 'linux2': 'xdg-open', 'darwin': 'open', 'win32': 'start'}
            os.system('{} "{}"'.format(open_cmd[sys.platform], filename))

        fig_filenamepdf = fig_filename + '.pdf'
        showfig(join(figure_directory, fig_filenamepdf))  # shows actually created PDF

    if create_svg:
        fig_filenamesvg = fig_filename + '.svg'

        plt.savefig(join(figure_directory, fig_filenamesvg), format='svg',
                    dpi=None,
                    edgecolor='w',
                    orientation='portrait',
                    transparent=False,
                    bbox_inches='tight',
                    pad_inches=0.05,
                    # frameon=None
                    )

    if create_png:
        fig_filenamepng = fig_filename + '.png'

        plt.savefig(join(figure_directory, fig_filenamepng), format='png',
                    dpi=200,
                    edgecolor='w',
                    orientation='portrait',
                    transparent=False,
                    bbox_inches='tight',
                    pad_inches=0.05,
                    # frameon=None
                    )

    if show_plot:
        plt.show()

    else:
        plt.close()