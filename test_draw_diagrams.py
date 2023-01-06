"""
test class for draw_diagrams.py
1/5/2023
"""


from draw_diagrams import draw_diagram


create_pdf = True
show_pdf = True
create_svg = True
show_plot = False


fig_filename = 'Fig_test_rd'
pattern = 2

table1 = 'Sailor'
table2 = 'Reserves'
table3 = 'Boat'

attribute11 = 'sname'
attribute12 = 'sid'
attribute21 = 'bid'
attribute22 = 'sid'
attribute31 = 'bid'



draw_diagram(table1, table2, table3,
             attribute11, attribute12, attribute21, attribute22, attribute31,
             pattern, fig_filename,
             create_pdf=create_pdf, show_pdf=show_pdf, create_svg=create_svg, show_plot=show_plot)

