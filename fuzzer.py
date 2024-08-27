from urllib.parse import urlencode, urlunparse, urlparse
import requests
from concurrent.futures import ThreadPoolExecutor
from payloads import Payloads  # Import the Payloads class

class Fuzzer:
    def __init__(self, url, params, threads, timeout, user_agent):
        self.url = url
        self.params = params
        self.threads = threads
        self.timeout = timeout
        self.user_agent = user_agent
    
    def fuzz(self):
        fuzzed_urls = []
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(self._fuzz_single, payload) for payload in Payloads().get_payloads()]
            for future in futures:
                fuzzed_urls.append(future.result())
        return fuzzed_urls

    def _fuzz_single(self, payload):
        parsed_url = urlparse(self.url)
        query_params = {param: payload for param in self.params}
        query_string = urlencode(query_params)
        url_parts = list(parsed_url)
        url_parts[4] = query_string
        return urlunparse(url_parts)
