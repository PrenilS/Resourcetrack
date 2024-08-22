import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from resourcetrack import initialize_tracking, finalize_tracking, save_tracking_data, start_tracking_thread

# Step 1: Initialize tracking
test_description = "Toy Regression Model n=100000, p=2000"
tracking_data = initialize_tracking(test_description)

# Step 2: Start resource tracking in a separate thread
stop_event = start_tracking_thread(tracking_data, interval=1)

# Step 3: Create a toy regression dataset
X, y = make_regression(n_samples=100000, n_features=2000, noise=0.1)

# Step 4: Define the regression model
model = LinearRegression()

# Step 5: Train the regression model
model.fit(X, y)

# Step 6: Stop resource tracking after training completes
stop_event.set()

# Step 7: Finalize and save tracking data
finalize_tracking(tracking_data, test_description, outputfile=True)


# %%
from resourcetrack.compare import load_run_data, compare_all_metrics

# Load two different runs
run1 = load_run_data('toy_regression_model_n=1000,_p=200_tracking_data.json')
run2 = load_run_data('toy_regression_model_n=100000,_p=2000_tracking_data.json')

# Compare all metrics between the two runs
compare_all_metrics(run1, run2)

# %%
