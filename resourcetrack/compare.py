import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_run_data(filename):
    """Load run data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def compare_runs(runs, metric):
    """Compare a specific metric across multiple runs and plot the results."""
    stats = [run['summary_stats'][metric] for run in runs]
    
    labels = ['Min', 'Max', 'Average', 'Median']
    run_values = [[stat['min'], stat['max'], stat['average'], stat['median']] for stat in stats]
    
    x = np.arange(len(labels))
    width = 0.8 / len(runs)  # Adjust the width of the bars based on the number of runs
    
    fig, ax = plt.subplots()
    for i, (run, values) in enumerate(zip(runs, run_values)):
        ax.bar(x - width * (len(runs) - 1) / 2 + i * width, values, width, label=run['test_description'])
    
    ax.set_xlabel('Statistics')
    ax.set_ylabel(f'{metric} Value')
    ax.set_title(f'Comparison of {metric} across {len(runs)} Runs')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.tight_layout()
    plt.show()

    labels2 = [metric + ' ' + lab for lab in labels]
    df = pd.DataFrame(run_values, columns=labels2, index=[run['test_description'] for run in runs]).T
    return df

def compare_all_metrics(runs, save_comparison=False):
    """Compare all metrics across multiple runs by generating plots for each metric."""
    metrics = runs[0]['summary_stats'].keys()
    
    for metric in metrics:
        if 'df' not in locals():
            df = compare_runs(runs, metric)
        else:
            df = pd.concat([df, compare_runs(runs, metric)], axis=0, ignore_index=False)
        
        if save_comparison:
            df.to_excel('comparison.xlsx')
    return df
