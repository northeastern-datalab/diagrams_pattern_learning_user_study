"""
test class for draw_statements.py
1/5/2023
"""


from draw_statements import draw_sql


create_pdf = True
show_pdf = True
create_svg = False
show_plot = False


fig_filename = 'Fig_test_sql'
pattern = 2

table1 = 'Student'
table1alias = 'S'
table2 = 'Passes'
table2alias = 'P'
table3 = 'Exam'
table3alias = 'E'

attribute01 = 'sname'
attribute11 = 'sname'
attribute12 = 'ID'
attribute21 = 'exam_id'
attribute22 = 'ID'
attribute31 = 'exam_id'



draw_sql(table1, table2, table3, table1alias, table2alias, table3alias,
         attribute11, attribute12, attribute21, attribute22, attribute31,
         pattern, fig_filename,
         create_pdf=create_pdf, show_pdf=show_pdf, create_svg=create_svg, show_plot=show_plot)
