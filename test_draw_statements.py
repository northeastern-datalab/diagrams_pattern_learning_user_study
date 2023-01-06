"""
test class for draw_statements.py
1/5/2023
"""


from draw_statements import draw_sql


create_pdf = True
show_pdf = True
create_svg = True
show_plot = False


fig_filename = 'Fig_test_sql'
pattern = 2

table1 = 'Sailor'
table1alias = 'S'
table2 = 'Reserves'
table2alias = 'R'
table3 = 'Boat'
table3alias = 'B'

attribute01 = 'sname'
attribute11 = 'sname'
attribute12 = 'sid'
attribute21 = 'bid'
attribute22 = 'sid'
attribute31 = 'bid'



draw_sql(table1, table2, table3, table1alias, table2alias, table3alias,
         attribute11, attribute12, attribute21, attribute22, attribute31,
         pattern, fig_filename,
         create_pdf=create_pdf, show_pdf=show_pdf, create_svg=create_svg, show_plot=show_plot)
