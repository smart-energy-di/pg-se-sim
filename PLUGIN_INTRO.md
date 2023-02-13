# some initial thoughts on a plugin mechanism

> **_NOTE:_**  this idea draft is not yet implemented

````text
$ src/se_sim/cli.py \
    --inp_plugin=.input.excel.reader --input_file=members.xls --input_format=vers1 \
    --filter_plugin=.filter.type --type='consumer' \
    --sim_plugin=.simulate.add_power_consumption --type=consumer \
    --output_plugin=.output.csv --output_file=added_mebers.csv \
    --output_plugin=.output.xy_graph --type=png --output_file=added_mebers.png size=xl

````
