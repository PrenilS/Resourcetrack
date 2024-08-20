import json
import matplotlib.pyplot as plt
import numpy as np

def load_run_data(filename):
    """Load run data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def compare_runs(run1, run2, metric):
    """Compare a specific metric between two runs and plot the results."""
    stats1 = run1['summary_stats'][metric]
    stats2 = run2['summary_stats'][metric]
    
    labels = ['Min', 'Max', 'Average', 'Median']
    run1_values = [stats1['min'], stats1['max'], stats1['average'], stats1['median']]
    run2_values = [stats2['min'], stats2['max'], stats2['average'], stats2['median']]
    
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots()
    ax.bar(x - width/2, run1_values, width, label=run1['test_description'])
    ax.bar(x + width/2, run2_values, width, label=run2['test_description'])
    
    ax.set_xlabel('Statistics')
    ax.set_ylabel(f'{metric} Value')
    ax.set_title(f'Comparison of {metric} between Two Runs')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.tight_layout()
    plt.show()

def compare_all_metrics(run1, run2):
    """Compare all metrics between two runs by generating plots for each metric."""
    metrics = run1['summary_stats'].keys()
    
    for metric in metrics:
        compare_runs(run1, run2, metric)
