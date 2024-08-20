import platform
import psutil

def gather_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "cpu_count": psutil.cpu_count(),
        "total_memory": psutil.virtual_memory().total,
    }

def collect_resource_stats():
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "swap_memory_percent": psutil.swap_memory().percent,
        "disk_read_bytes": psutil.disk_io_counters().read_bytes,
        "disk_write_bytes": psutil.disk_io_counters().write_bytes,
        "net_bytes_sent": psutil.net_io_counters().bytes_sent,
        "net_bytes_recv": psutil.net_io_counters().bytes_recv,
    }
