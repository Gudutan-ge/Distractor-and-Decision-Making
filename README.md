# Distractor and Decision-Making

This project explores the effects of distractor value on decision-making behavior through experiments, data processing, modeling, and simulations. Below is an overview of the project structure.

---

## Project Structure

### Main Scripts
1. **`data_process.py`**  
   - Processes experimental data from participants.
   - Generates visualizations of results, including accuracy curves, target choice curve and reaction time analysis.
   - Outputs summary statistics and plots.

2. **`data_process_mode.py`**  
   - Processes data from model simulations.
   - Creates visualizations of model performance, comparing simulation results with experimental data.

3. **`mode.py`**  
   - Constructs the normalized value coding model for decision-making.
   - Simulates decisions based on model parameters.
   - Outputs simulation results to the `model_data` folder.

4. **`trail.py`**  
   - Used for conducting decision-making experiments with participants.
   - Manages task presentations and records participant responses and reaction times.

---

### Data Files and Folders

1. **`products_data.csv`**  
   - Stores all product information, including attributes such as brand, price, and quality.  
   - Used to rank and classify products into target and distractor groups.

2. **`images/`**  
   - Contains images of all decision-making products used in experiments.

3. **`trail_data/`**  
   - Stores experimental setup data for each participant's decision-making trials.

4. **`data/`**  
   - Contains all experimental results, including choices and reaction times.

5. **`model_data/`**  
   - Contains results from model simulations, including decision outcomes and reaction times.
