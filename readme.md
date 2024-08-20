# Resourcetrack

Workload Tracker is a Python package for tracking and recording system metrics during data science workloads. It can also compare the results of different runs, generating insights and visualizations to help you assess system performance.

## Features

- Track CPU, memory, disk, and network usage during a workload.
- Continuously monitor system resources in the background.
- Save resource tracking data to a JSON file.
- Compare multiple runs and visualize key metrics.

## Installation

```bash
pip install .
```

## Usage
This can be incorporated into your existing codebase by importing the `resourcetrack` module and using the `track_resources` function to start tracking system resources. You can also use the `compare_runs` function to compare the results of different runs.

```python
# Import the necessary functions from the resourcetrack module
from resourcetrack import initialize_tracking, finalize_tracking, save_tracking_data, start_tracking_thread

# Step 1: Initialize tracking and give a description to your test
test_description = "Toy Regression Model n=100000, p=200"
tracking_data = initialize_tracking(test_description)

# Step 2: Start resource tracking in a separate thread to monitor system resources during the workload execution. The interval parameter specifies the time interval in seconds between each resource measurement.
stop_event = start_tracking_thread(tracking_data, interval=10)

# Step 3: Run your workload
X, y = make_regression(n_samples=100000, n_features=200, noise=0.1)
model = LinearRegression()
model.fit(X, y)

# Step 4: Stop resource tracking after training completes
stop_event.set()

# Step 7: Finalize and save tracking data
finalize_tracking(tracking_data, test_description, outputfile=True)
```

## Comparing Runs

You can compare the results of different runs by loading the tracking data from the JSON files and using the `compare_all_metrics` function.

```python
# Import the necessary functions from the resourcetrack.compare module
from resourcetrack.compare import load_run_data, compare_all_metrics

# Load two different runs
run1 = load_run_data('toy_regression_model_n=100000,_p=20_tracking_data.json')
run2 = load_run_data('toy_regression_model_n=100000,_p=200_tracking_data.json')

# Compare all metrics between the two runs
compare_all_metrics(run1, run2)
```
