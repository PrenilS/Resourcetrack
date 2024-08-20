import threading
import time
from datetime import datetime
import json
from .utils import gather_system_info, collect_resource_stats

def initialize_tracking(test_description):
    """Initialize tracking by gathering system information and starting a tracking dictionary."""
    start_time = datetime.now()  # Capture the start time of the test
    system_info = gather_system_info()  # Gather system info like OS, CPU, etc.
    
    tracking_data = {
        "test_description": test_description,
        "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
        "system_info": system_info,
        "resource_stats": [],  # List to hold resource stats snapshots
    }
    
    return tracking_data

def track_resources_continuously(tracking_data, interval=1, stop_event=None):
    """Track resources at regular intervals in a separate thread."""
    while not stop_event.is_set():
        resource_stats = collect_resource_stats()  # Collect the current resource stats
        tracking_data["resource_stats"].append(resource_stats)  # Append to tracking data
        time.sleep(interval)  # Wait for the specified interval before collecting again

def start_tracking_thread(tracking_data, interval=1):
    """Start a background thread for continuous resource tracking."""
    stop_event = threading.Event()  # Event to signal when to stop tracking
    tracking_thread = threading.Thread(target=track_resources_continuously, args=(tracking_data, interval, stop_event))
    tracking_thread.start()  # Start the tracking thread
    return stop_event  # Return the stop event to be used later to stop the thread

def finalize_tracking(tracking_data):
    """Finalize the tracking by calculating the total time and summary statistics."""
    end_time = datetime.now()  # Capture the end time of the test
    tracking_data["end_time"] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    tracking_data["total_time"] = (end_time - datetime.strptime(tracking_data["start_time"], '%Y-%m-%d %H:%M:%S')).total_seconds()
    
    # Calculate summary statistics like min, max, average, and median
    tracking_data["summary_stats"] = calculate_summary_stats(tracking_data["resource_stats"])

def calculate_summary_stats(stats):
    """Calculate summary statistics (min, max, average, median) for the collected metrics."""
    from statistics import mean, median

    summary = {}
    for key in stats[0].keys():
        if key == "timestamp":  # Skip timestamp as it's not a numeric metric
            continue
        values = [stat[key] for stat in stats]
        summary[key] = {
            "min": min(values),
            "max": max(values),
            "average": mean(values),
            "median": median(values),
        }
    return summary

def save_tracking_data(tracking_data, filename="tracking_data.json"):
    """Save the tracking data to a JSON file."""
    with open(filename, 'w') as outfile:
        json.dump(tracking_data, outfile, indent=4)
