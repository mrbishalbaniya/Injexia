from fuzzer import Fuzzer
from detector import Detector
from utils import parse_url

class Scanner:
    def __init__(self, url, params, threads, timeout, user_agent):
        self.url = url
        self.params = params
        self.threads = threads
        self.timeout = timeout
        self.user_agent = user_agent
    
    def scan(self):
        fuzzer = Fuzzer(self.url, self.params, self.threads, self.timeout, self.user_agent)
        fuzzed_urls = fuzzer.fuzz()

        detector = Detector(fuzzed_urls)
        results = detector.detect()
        
        return results
