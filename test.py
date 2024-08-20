import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from resourcetrack import initialize_tracking, finalize_tracking, save_tracking_data, start_tracking_thread

# Step 1: Initialize tracking
test_description = "Toy Regression Model Training with Continuous Tracking"
tracking_data = initialize_tracking(test_description)

# Step 2: Start resource tracking in a separate thread
stop_event = start_tracking_thread(tracking_data, interval=1)

# Step 3: Create a toy regression dataset
X, y = make_regression(n_samples=10000000, n_features=20, noise=0.1)

# Step 4: Define the regression model
model = LinearRegression()

# Step 5: Train the regression model
model.fit(X, y)

# Step 6: Stop resource tracking after training completes
stop_event.set()

# Step 7: Finalize and save tracking data
finalize_tracking(tracking_data)
save_tracking_data(tracking_data, "continuous_training_tracking_data.json")

print("Tracking data saved to continuous_training_tracking_data.json")
