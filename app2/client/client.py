import schedule
import time
import requests


def collect_metrics():
    # collect_from_prometheus
    metrics = {
        'timestamp': time.time(),
        'container_name': 'container_1',
        'container_id': 99999,
        'cpu': 0.3,
        'memory': 0.6,
        'bytes_rx': 123,
        'bytes_tx': 123
    }
    requests.post('http://192.168.50.2:6000/metrics', data=metrics)


schedule.every(1).seconds.do(collect_metrics)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
