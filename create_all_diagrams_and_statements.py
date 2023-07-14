"""
code that creates visual diagrams and SQL statements, for different schemas, and 4 patterns.
takes an input CSV file with various schemas information
1/5/2023
"""

from draw_diagrams import draw_diagram
from draw_statements import draw_sql
import pandas as pd
from os.path import abspath, dirname, join
from inspect import getfile, currentframe


create_pdf = True
show_pdf = False
create_svg = True
show_plot = False
create_png = True


# -- Determine path to data *irrespective* of where the file is run from
fileName = 'input.csv'
current_path = dirname(abspath(getfile(currentframe())))
data_directory = join(current_path, 'data')


# -- Load data from file
try:
    data = pd.read_csv(join(data_directory, fileName), delimiter=',', skiprows=0, header=0)
except IOError as error:
    raise error

print(data)

jsonFileName = 'output.json'
data.to_json(join(data_directory,jsonFileName), orient='records', date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True, indent=None, storage_options=None)


# -- Iterate over file rows (and the 4 patterns) and call the create diagram and sql function
for index, row in data.iterrows():

    # row contains 4 filenames, one for each of the 4 pattern per row
    for (pattern, filenameindex) in zip([1, 2, 3, 4], ['diagrampattern1', 'diagrampattern2', 'diagrampattern3', 'diagrampattern4']):
        draw_diagram(row['table1'], row['table2'], row['table3'],
                     row['attribute11'], row['attribute12'], row['attribute21'], row['attribute22'], row['attribute31'],
                     pattern, row[filenameindex],
                     create_pdf=create_pdf, show_pdf=show_pdf, create_svg=create_svg, show_plot=show_plot, create_png=create_png)

    # row contains 4 filenames, one for each of the 4 pattern per row
    for (pattern, filenameindex) in zip([1, 2, 3, 4], ['sqlpattern1', 'sqlpattern2', 'sqlpattern3', 'sqlpattern4']):
        draw_sql(row['table1'], row['table2'], row['table3'], row['table1alias'], row['table2alias'], row['table3alias'],
                 row['attribute11'], row['attribute12'], row['attribute21'], row['attribute22'], row['attribute31'],
                 pattern, row[filenameindex],
                 create_pdf=create_pdf, show_pdf=show_pdf, create_svg=create_svg, show_plot=show_plot, create_png=create_png)

    print('{}.'.format(index+1))
    print('{}({},{})   {}'.format(row['table1'], row['attribute11'], row['attribute12'], row['table1alias']))
    print('{}({},{})   {}'.format(row['table2'], row['attribute21'], row['attribute22'], row['table2alias']))
    print('{}({})   {}'.format(row['table3'], row['attribute31'], row['table3alias']))
    print('1. {}'.format(row['answer1']))
    print('2. {}'.format(row['answer2']))
    print('3. {}'.format(row['answer3']))
    print('4. {}'.format(row['answer4']))
    print()