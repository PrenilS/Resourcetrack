import platform
import psutil
from datetime import datetime

def gather_system_info():
    """Gather basic system information such as OS, CPU, and total memory."""
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "cpu_count": psutil.cpu_count(),
        "total_memory_gb": psutil.virtual_memory().total / (1024 ** 3),  # Convert bytes to GB
    }

def collect_resource_stats():
    """Collect current resource usage statistics including CPU, memory, disk, and network usage."""
    return {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Convert timestamp to string
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "swap_memory_percent": psutil.swap_memory().percent,
        "disk_read_gigabytes": psutil.disk_io_counters().read_bytes / (1024 ** 3),
        "disk_write_gigabytes": psutil.disk_io_counters().write_bytes / (1024 ** 3),
        "net_gigabytes_sent": psutil.net_io_counters().bytes_sent / (1024 ** 3),
        "net_gigabytes_recv": psutil.net_io_counters().bytes_recv / (1024 ** 3),
    }
