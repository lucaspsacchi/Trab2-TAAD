import schedule
import time
import requests


def collect_metrics():
    # collect_from_prometheus
    metrics = {
        'timestamp': time.time(),
        'vm_name': 'vm_1',
        'cpu': 0.3,
        'memory': 0.6,
        'bytes_rx': 123,
        'bytes_tx': 123,
        'tool': 'prometheus'
    }
    requests.post('http://192.168.50.2:9000/metrics', data=metrics)


schedule.every(15).seconds.do(collect_metrics)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
