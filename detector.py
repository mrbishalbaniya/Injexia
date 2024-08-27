import requests
from payloads import Payloads  # Import the Payloads class

class Detector:
    def __init__(self, urls):
        self.urls = urls
    
    def detect(self):
        results = []
        for url in self.urls:
            try:
                response = requests.get(url, timeout=10)
                if self._check_payload_in_response(response.text):
                    results.append({"url": url, "vulnerable": True})
                else:
                    results.append({"url": url, "vulnerable": False})
            except requests.RequestException:
                results.append({"url": url, "vulnerable": False, "error": "Request failed"})
        return results
    
    def _check_payload_in_response(self, response_text):
        for payload in Payloads().get_payloads():
            if payload in response_text:
                return True
        return False
