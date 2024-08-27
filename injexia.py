from scanner import Scanner
from reporter import Reporter
import argparse

def main():
    parser = argparse.ArgumentParser(description="   - Advanced XSS Detection and Exploitation Tool")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-p", "--params", help="Parameters to test, separated by commas", default="")
    parser.add_argument("-o", "--output", help="Output file for results", default="results.txt")
    parser.add_argument("--threads", help="Number of threads to use", type=int, default=5)
    parser.add_argument("--timeout", help="Request timeout in seconds", type=int, default=10)
    parser.add_argument("--user-agent", help="Custom User-Agent", default="Injexia/1.0")
    
    args = parser.parse_args()

    scanner = Scanner(args.url, args.params.split(','), args.threads, args.timeout, args.user_agent)
    results = scanner.scan()
    
    reporter = Reporter(results, args.output)
    reporter.generate_report()

if __name__ == "__main__":
    main()
