import requests
import concurrent.futures
import time
import random


class LoadTester:
    def __init__(self, base_url, num_workers=50, duration_seconds=60, delay=0.01):
        self.base_url = base_url + '/api'
        self.num_workers = num_workers
        self.duration = duration_seconds
        self.delay = delay
        self.stop_flag = False
        self.success_count = 0
        self.error_count = 0
        self.endpoints = ['/doctor_specialization', '/coach_specialization', '/program', '/dish', '/sportsman']

    def make_request(self):
        if self.stop_flag:
            return
        
        try:
            url = self.base_url + random.choice(self.endpoints)
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                self.success_count += 1
            else:
                self.error_count += 1
        except:
            self.error_count += 1

    def run(self):
        start_time = time.time()
        print('Starting load test.')
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = []
            
            while time.time() - start_time < self.duration:
                future = executor.submit(self.make_request)
                futures.append(future)
                time.sleep(self.delay)
            
            self.stop_flag = True
            concurrent.futures.wait(futures, timeout=30)
        
        total = self.success_count + self.error_count
        print(f"Successful: {self.success_count} | Failed: {self.error_count} | Total: {total}")


if __name__ == "__main__":
    tester = LoadTester(
        base_url="https://ca-clouds-lab2.whitecliff-197d7c49.uksouth.azurecontainerapps.io",
        num_workers=300,
        duration_seconds=30,
        delay=0
    )
    tester.run()