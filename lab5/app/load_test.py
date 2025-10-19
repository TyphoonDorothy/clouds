import requests
import threading
import time
import random


class LoadTester:
    def __init__(self, base_url, num_threads=10, duration_seconds=60):
        self.base_url = base_url
        self.num_threads = num_threads
        self.duration = duration_seconds
        self.stop_flag = False

    def simulate_requests(self):
        endpoints = ['/doctor_specialization', '/coach_specialization', '/program']

        while not self.stop_flag:
            try:
                url = self.base_url + random.choice(endpoints)
                requests.get(url, timeout=10)
            except:
                pass

            time.sleep(random.uniform(0.1, 0.5))

    def run(self):
        print(f"Starting load test: {self.num_threads} threads for {self.duration}s")
        start_time = time.time()
        threads = []

        for _ in range(self.num_threads):
            t = threading.Thread(target=self.simulate_requests)
            t.daemon = True
            t.start()
            threads.append(t)

        try:
            while time.time() - start_time < self.duration:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        self.stop_flag = True
        print("Load test completed")


if __name__ == "__main__":
    tester = LoadTester(
        base_url="https://ca-clouds-lab2.whitecliff-197d7c49.uksouth.azurecontainerapps.io",
        num_threads=20,
        duration_seconds=120
    )
    tester.run()