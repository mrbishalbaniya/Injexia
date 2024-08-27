import json

class Reporter:
    def __init__(self, results, output_file):
        self.results = results
        self.output_file = output_file
    
    def generate_report(self):
        with open(self.output_file, 'w') as file:
            json.dump(self.results, file, indent=4)
        print(f"Report saved to {self.output_file}")
