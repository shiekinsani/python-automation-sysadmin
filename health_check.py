import psutil
import platform
from datetime import datetime

def check_system():
    os_name = platform.system()
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    print(f"--- Laporan Sistem ({os_name}) ---")
    print(f"Masa: {datetime.now().strftime('%H:%M:%S')}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM Usage: {memory.percent}%")
    s
    # Save ke file text
    with open("health_log.txt", "a") as f:
        f.write(f"{datetime.now()}: CPU {cpu_usage}%, RAM {memory.percent}%\n")

if __name__ == "__main__":
    try:
        check_system()
        print("\nBerjaya! File 'health_log.txt' telah dikemaskini.")
    except Exception as e:
        print(f"Alamak, ada error: {e}")