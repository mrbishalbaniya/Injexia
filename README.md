# Injexia

**Injexia** is an  XSS detection and exploitation tool designed to identify and exploit Cross-Site Scripting (XSS) vulnerabilities in web applications. It offers a flexible and powerful way to perform XSS testing, leveraging multithreading to efficiently handle large numbers of requests.

## Features

- **Custom Payloads:** Use a variety of payloads to test for XSS vulnerabilities.
- **Multithreaded Fuzzing:** Speed up the testing process by using multiple threads.
- **Detailed Reporting:** Generate comprehensive reports of detected vulnerabilities.
- **Configurable Options:** Customize request timeouts, user-agent strings, and more.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mrbishalbaniya/Injexia.git
   cd Injexia```
   
## Install Dependencies:

```bash

pip install -r requirements.txt
```
## Usage
To run the tool, use the following command:

``` bash
python injexia.py <url> [options]
```
## Options
<url> (required): The target URL to scan for XSS vulnerabilities.
- -p, --params (optional): Comma-separated list of parameters to test (e.g., param1,param2).
- -o, --output (optional): Path to the file where results will be saved. Defaults to results.txt.
- --threads (optional): Number of threads to use for scanning. Defaults to 5.
- --timeout (optional): Request timeout in seconds. Defaults to 10.
- --user-agent (optional): Custom User-Agent string. Defaults to Injexia/1.0.
- 
## Examples
Basic Scan:

```bash
python injexia.py "http://example.com/?search=test"
```
Scan with Specific Parameters:

```bash
python injexia.py "http://example.com/?search=test&lang=en" -p search,lang
```
Save Results to a File:

```bash
python injexia.py "http://example.com/?search=test" -o output.json
```
Using Multiple Threads:

``` bash

python injexia.py "http://example.com/?search=test" --threads 10
```
Custom User-Agent:

``` bash

python injexia.py "http://example.com/?search=test" --user-agent "MyCustomAgent/2.0
```
