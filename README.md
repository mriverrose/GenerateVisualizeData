# Generate and Visualize a Dataset
## Overview.
The `ExploreDataset.ipynb` is the Python notebook that shows how we can explore the `sales_data.csv` file we generated with the `create_sales_data.py` script. 

In the notebook, we look at sales by product, state, sex, and age group, as well as when products are most frequently sold, which products are purchased together, and which age groups prefer certain products. Look at the `.png` files in [NotebookPlotlyImages](https://github.com/mriverrose/GenerateVisualizeData/tree/master/NotebookPlotlyImages) to see how we visualized the data.

## Steps for generating a dataset.
### Step 1: Set the weights and products.
In the `create_sales_data.py` file, set the product and product and address weights as you desire. This will determine how the data will come out when you visualize it. I.e., you can make any product and set the weights to determine who buys it, how often, and so forth.

### Step 2: Create the data files.
From the command line, run `python create_sales_data.py`. This will generate twelve `.csv` files that correspond to each month. It takes 15-20 minutes to run on my computer. 

### Step 3: Merge the data files into one dataset.
From the command line, run `python merge_sales_data.py` to stitch the twelve `.csv` files into one `sales_data.csv` dataset that you can explore in the `ExploreDataset.ipynb` notebook.
