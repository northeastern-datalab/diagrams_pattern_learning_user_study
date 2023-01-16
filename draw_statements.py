"""
Code that draws a sql statement given the schema information and choice of pattern
1/5/2022
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
from matplotlib import font_manager
from os.path import abspath, dirname, join
from inspect import getfile, currentframe


ydelta = 0.95  # vertical adjustment
xdelta = 0.28  # horizontal adjustment: size of one letter


def draw_sql(table1, table2, table3, table1alias, table2alias, table3alias,
             attribute11, attribute12, attribute21, attribute22, attribute31,
             pattern, fig_filename,
             create_pdf=True, show_pdf=True, create_svg=False, show_plot=False, create_png=False):

    mpl.rcParams['font.size'] = "32"
    mpl.rcParams['figure.figsize'] = [11, 7]
    font_manager.fontManager.addfont(
        './fonts/OTF/SourceCodePro-Regular.otf')   # SQL font used by PgAdmin
    # SQL font used by PgAdmin
    mpl.rcParams['font.family'] = "Source Code Pro"

    # # Add every font at the specified location
    # font_dir = ['/Users/gatt/Library/Fonts']
    # for font in font_manager.findSystemFonts(font_dir):
    #     print(font)
    #     font_manager.fontManager.addfont(font)
    #
    # print(font_manager.findfont("Source Code Pro"))         # find fonts

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    ax.axis([-1, 9, -9, 1])

    if pattern in (1, 2):
        ax.text(0, 0, 'SELECT', color='#990088')
        ax.text(xdelta*7, 0, '{}.{}'.format(table1alias, attribute11))
        ax.text(0, -ydelta, 'FROM', color='#990088')
        ax.text(xdelta*5, -ydelta, '{} {}'.format(table1, table1alias))
        if pattern == 1:
            ax.text(0, -2*ydelta, 'WHERE EXISTS', color='#990088')
            ax.text(xdelta*12, -2*ydelta, '(')
        if pattern == 2:
            ax.text(0, -2*ydelta, 'WHERE NOT EXISTS', color='#990088')
            ax.text(xdelta*16, -2*ydelta, '(')

        ax.text(xdelta*2, -3*ydelta, 'SELECT', color='#990088')
        ax.text(xdelta*9, -3*ydelta, '*')
        ax.text(xdelta*2, -4*ydelta, 'FROM', color='#990088')
        ax.text(xdelta*7, -4*ydelta, '{} {}'.format(table2, table2alias))
        ax.text(xdelta*2, -5*ydelta, 'WHERE', color='#990088')
        ax.text(xdelta*8, -5*ydelta, '{}.{} = {}.{}'.format(table2alias,
                attribute22, table1alias, attribute12))
        ax.text(xdelta*2, -6*ydelta, 'AND EXISTS', color='#990088')
        ax.text(xdelta*12, -6*ydelta, '(')

        ax.text(xdelta*4, -7*ydelta, 'SELECT', color='#990088')
        ax.text(xdelta*11, -7*ydelta, '*')
        ax.text(xdelta*4, -8*ydelta, 'FROM', color='#990088')
        ax.text(xdelta*9, -8*ydelta, '{} {}'.format(table3, table3alias))
        ax.text(xdelta*4, -9*ydelta, 'WHERE', color='#990088')
        ax.text(xdelta*10, -9*ydelta, '{}.{} = {}.{}))'.format(table3alias,
                attribute31, table2alias, attribute21))

    if pattern in (3, 4):
        ax.text(0, 0, 'SELECT', color='#990088')
        ax.text(xdelta*7, 0, '{}.{}'.format(table1alias, attribute11))
        ax.text(0, -ydelta, 'FROM', color='#990088')
        ax.text(xdelta*5, -ydelta, '{} {}'.format(table1, table1alias))
        if pattern == 3:
            ax.text(0, -2*ydelta, 'WHERE EXISTS', color='#990088')
            ax.text(xdelta*12, -2*ydelta, '(')
        if pattern == 4:
            ax.text(0, -2*ydelta, 'WHERE NOT EXISTS', color='#990088')
            ax.text(xdelta*16, -2*ydelta, '(')

        ax.text(xdelta*2, -3*ydelta, 'SELECT', color='#990088')
        ax.text(xdelta*9, -3*ydelta, '*')
        ax.text(xdelta*2, -4*ydelta, 'FROM', color='#990088')
        ax.text(xdelta*7, -4*ydelta, '{} {}'.format(table3, table3alias))
        ax.text(xdelta*2, -5*ydelta, 'WHERE NOT EXISTS', color='#990088')
        ax.text(xdelta*18, -5*ydelta, '(')

        ax.text(xdelta*4, -6*ydelta, 'SELECT', color='#990088')
        ax.text(xdelta*11, -6*ydelta, '*')
        ax.text(xdelta*4, -7*ydelta, 'FROM', color='#990088')
        ax.text(xdelta*9, -7*ydelta, '{} {}'.format(table2, table2alias))
        ax.text(xdelta*4, -8*ydelta, 'WHERE', color='#990088')
        ax.text(xdelta*10, -8*ydelta, '{}.{} = {}.{}'.format(table2alias,
                attribute21, table3alias, attribute31))
        ax.text(xdelta*4, -9*ydelta, 'AND', color='#990088')
        ax.text(xdelta*8, -9*ydelta, '{}.{} = {}.{}))'.format(table2alias,
                attribute22, table1alias, attribute12))

    plt.axis('off')
    plt.tight_layout()
    plt.xlim(-0.5, 10)
    plt.ylim(-9, 1)

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
            open_cmd = {'linux': 'xdg-open', 'linux2': 'xdg-open',
                        'darwin': 'open', 'win32': 'start'}
            os.system('{} "{}"'.format(open_cmd[sys.platform], filename))

        fig_filenamepdf = fig_filename + '.pdf'
        # shows actually created PDF
        showfig(join(figure_directory, fig_filenamepdf))

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
