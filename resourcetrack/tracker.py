import threading
import time
from datetime import datetime
import json
from .utils import gather_system_info, collect_resource_stats

def initialize_tracking(test_description):
    start_time = datetime.now()
    system_info = gather_system_info()
    
    tracking_data = {
        "test_description": test_description,
        "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
        "system_info": system_info,
        "resource_stats": [],
    }
    
    return tracking_data

def track_resources_continuously(tracking_data, interval=1, stop_event=None):
    while not stop_event.is_set():
        resource_stats = collect_resource_stats()
        tracking_data["resource_stats"].append(resource_stats)
        time.sleep(interval)

def start_tracking_thread(tracking_data, interval=1):
    stop_event = threading.Event()
    tracking_thread = threading.Thread(target=track_resources_continuously, args=(tracking_data, interval, stop_event))
    tracking_thread.start()
    return stop_event

def finalize_tracking(tracking_data):
    end_time = datetime.now()
    tracking_data["end_time"] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Calculate summary statistics
    tracking_data["summary_stats"] = calculate_summary_stats(tracking_data["resource_stats"])

def calculate_summary_stats(stats):
    from statistics import mean, median

    summary = {}
    for key in stats[0].keys():
        values = [stat[key] for stat in stats]
        summary[key] = {
            "min": min(values),
            "max": max(values),
            "average": mean(values),
            "median": median(values),
        }
    return summary

def save_tracking_data(tracking_data, filename="tracking_data.json"):
    with open(filename, 'w') as outfile:
        json.dump(tracking_data, outfile, indent=4)
