Okay, Agent! You've cleared Basic Training. Now, let's forge you into a Python-powered Purple Team operator. This won't be just questions; it's a series of escalating challenges designed to build the practical skills you need.

**Mission Brief:** Your objective is to master Python for Purple Teaming. This involves automating detection, analysis, simulating adversary techniques (safely!), integrating security tools, and enriching data. Each level builds upon the last.

**Rules of Engagement:**
1.  **Understand the *Why*:** Don't just code. Understand the security context of each task.
2.  **Use the Docs:** Python's standard library and third-party package documentation are your best friends. `help()` and `dir()` are useful built-ins.
3.  **Test Incrementally:** Write small pieces, test them, then build.
4.  **Think Defensively:** How could your script fail? Add error handling.
5.  **Safety First:** When simulating attacks, *only* do so on systems you own or have explicit, written permission to test. Start with benign actions.
6.  **Virtual Environments:** Use them (`python -m venv .venv`, `source .venv/bin/activate` or `.\.venv\Scripts\activate` on Windows) for *all* projects from Level 2 onwards to manage dependencies.

---

**Level 1: Foundations Revisited & System Interaction**

*   **Objective:** Solidify basics and learn to interact with the local OS using Python.
*   **Concepts:** Standard Library (`os`, `sys`, `subprocess`, `datetime`), File I/O basics, Error Handling (`try/except`).

1.  **System Info Grabber:** Write a script that prints:
    *   The current working directory (`os.getcwd()`).
    *   The operating system platform (`sys.platform`, `os.name`).
    *   The Python version being used (`sys.version`).
    *   The current date and time (`datetime.datetime.now()`).
2.  **Directory Lister:**
    *   Ask the user for a directory path (`input()`).
    *   List all files and subdirectories within that path (`os.listdir()`).
    *   **Bonus:** Use `os.path.join()` to print the *full* path to each item.
    *   **Error Handling:** What happens if the user enters an invalid path? Use `try/except` with `FileNotFoundError` to print a user-friendly message.
3.  **Simple Command Runner:**
    *   Use the `subprocess` module to run a simple, non-interactive command (like `ping 8.8.8.8` or `ipconfig`/`ifconfig`). Choose one appropriate for your OS.
    *   Capture and print the command's standard output.
    *   **Hint:** Look into `subprocess.run()` or `subprocess.check_output()`. Be mindful of potential security implications when running external commands.
4.  **Log File Creator:**
    *   Write a script that appends a timestamped message to a file named `activity.log`.
    *   Each message should be on a new line, formatted like: `YYYY-MM-DD HH:MM:SS - Script started.`
    *   Run the script multiple times to see the log grow.
    *   **Hint:** Use file mode `'a'` (append). Use `datetime` for the timestamp.

---

**Level 2: Networking Basics & APIs**

*   **Objective:** Make network requests, understand basic HTTP, and interact with simple APIs.
*   **Concepts:** `requests` library (install with `pip install requests`), HTTP Methods (GET, POST), Status Codes, JSON basics (`json` module).

*(Remember to activate your virtual environment and `pip install requests`)*

5.  **Website Status Checker:**
    *   Take a URL as input from the user (e.g., `https://google.com`).
    *   Use the `requests` library to send a GET request to the URL.
    *   Print the HTTP status code (`response.status_code`) and whether it indicates success (e.g., 200 OK).
    *   **Error Handling:** Handle potential `requests.exceptions.RequestException` errors if the URL is invalid or unreachable.
6.  **Public IP Finder:**
    *   Use `requests` to query a public API that returns your public IP address (e.g., `https://api.ipify.org?format=json` or `https://httpbin.org/ip`).
    *   Parse the JSON response (`response.json()`).
    *   Print *only* the IP address.
7.  **JSON Placeholder Interaction:**
    *   The site `https://jsonplaceholder.typicode.com/` offers fake API endpoints.
    *   Write a script to fetch the first 10 "todos" from `https://jsonplaceholder.typicode.com/todos`.
    *   Print the `title` of each "todo" item.
    *   **Bonus:** Modify the script to fetch a *specific* todo by its ID (e.g., `/todos/5`).
8.  **Simple POST Request:**
    *   Use `https://httpbin.org/post`. This endpoint echoes the data you send it.
    *   Create a Python dictionary representing some simple data (e.g., `{'username': 'purple_agent', 'status': 'active'}`).
    *   Use `requests.post()` to send this dictionary as JSON data to the endpoint.
    *   Print the `json` part of the response to verify your data was received.
    *   **Hint:** Use the `json=` parameter in `requests.post()`.

---

**Level 3: Data Parsing & Regular Expressions**

*   **Objective:** Extract information from structured (CSV, JSON) and unstructured (text logs) data. Master basic regular expressions.
*   **Concepts:** `csv` module, `json` module deep dive, `re` module (regular expressions).

9.  **CSV Log Reader:**
    *   Create a simple CSV file named `auth_logs.csv` with columns: `Timestamp,SourceIP,User,Status` (e.g., `2023-10-27T10:00:00,192.168.1.10,admin,Success`). Add a few rows with varying data (Success/Failure, different IPs/Users).
    *   Write a Python script using the `csv` module to read this file.
    *   Print only the rows where the `Status` is "Failure".
    *   **Hint:** Use `csv.reader` or `csv.DictReader`.
10. **JSON Config Parser:**
    *   Create a JSON file `config.json` representing a tool's configuration (e.g., `{"api_key": "...", " monitored_folders": ["/var/log", "/etc"], "threat_level_threshold": 4}`).
    *   Write a script to load this configuration using the `json` module.
    *   Print the API key and the list of monitored folders.
    *   **Error Handling:** Handle `json.JSONDecodeError` if the file is malformed and `FileNotFoundError`.
11. **IP Address Extractor (Regex):**
    *   You have a raw text file (`sample_log.txt`) containing lines like: `INFO: Connection established from 192.168.1.5 port 45678` or `WARN: Failed login attempt for user 'guest' from 10.0.0.25`.
    *   Write a script using the `re` module to find and print *all* valid IPv4 addresses present in the file.
    *   **Hint:** A basic IPv4 regex pattern looks something like `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`. Refine it if needed. Use `re.findall()`.
12. **Log Field Extractor (Regex Groups):**
    *   Assume log lines follow a pattern: `[TIMESTAMP] LEVEL User=USERNAME Action=ACTION_TAKEN Source=IP_ADDRESS`. (e.g., `[2023-10-27T11:15:30] INFO User=jdoe Action=FileAccess Source=172.16.30.5`).
    *   Write a script using `re` with *capturing groups* `(...)` to extract the `User`, `Action`, and `Source` IP from each matching line in a sample log file.
    *   Print the extracted fields for each match.
    *   **Hint:** Use `re.search()` or `re.finditer()` and access groups using `match.group(index_or_name)`.

---

**Level 4: Building Structure & Tooling**

*   **Objective:** Organize code using functions and classes (OOP basics), improve error handling, handle arguments.
*   **Concepts:** Functions with arguments/return values, basic Classes & Objects (`__init__`, methods), `argparse` module for command-line arguments.

13. **Refactor: Log Parser Function:**
    *   Take your IP Address Extractor script (Problem 11) or Log Field Extractor (Problem 12).
    *   Encapsulate the core logic (reading file, applying regex, printing results) inside a function `parse_log(log_file_path)`.
    *   The main part of your script should now just call this function.
14. **Command-Line Log Parser:**
    *   Modify the script from Problem 13. Use the `argparse` module to accept the log file path as a command-line argument instead of hardcoding it or using `input()`.
    *   Your script should be runnable like: `python log_parser.py --file sample_log.txt`.
    *   Add help messages for the argument (`--file` or `-f`).
15. **Simple API Client Class:**
    *   Create a Python class named `ApiClient`.
    *   The constructor (`__init__`) should take a `base_url` (like `https://jsonplaceholder.typicode.com`).
    *   Add a method `get_todos(self, limit=None)` that fetches todos (like Problem 7). It should optionally accept a `limit` for the number of todos.
    *   Add another method `get_todo_by_id(self, todo_id)` that fetches a specific todo.
    *   Instantiate the class and use its methods to fetch data.
    *   **Bonus:** Add basic error handling within the class methods.
16. **Configuration Manager Class:**
    *   Create a class `ConfigManager` that loads and provides access to configuration from a JSON file (like Problem 10).
    *   The `__init__` should take the config file path. It should load the data and store it internally (e.g., in `self.config_data`).
    *   Add a method `get_setting(self, key)` that returns the value for a given configuration key.
    *   Handle `KeyError` gracefully if a requested setting doesn't exist.

---

**Level 5: Advanced Networking & System Interaction**

*   **Objective:** Deeper dive into networking, process management, and interacting with system events (conceptual).
*   **Concepts:** `socket` module basics (optional, lower-level), more `subprocess`, interacting with platform-specific APIs (conceptual).

17. **Basic Port Scanner (Conceptual & Careful!):**
    *   **Theory:** Understand how a basic TCP connect scan works (try to establish a connection; success means open, failure means closed/filtered).
    *   Write a *function* `check_port(ip, port, timeout=1)` that attempts to connect to a given IP and port using the `socket` module.
    *   It should return `True` if the connection succeeds within the timeout, `False` otherwise.
    *   **Main Script:** Use this function to check a *few specific, known-open ports* (like 80, 443) on a *safe target* you control or a public service explicitly allowing checks (e.g., `google.com`). **DO NOT scan wide ranges or targets you don't have permission for.**
    *   Print the results (e.g., `Port 80 on google.com is open`).
    *   **Disclaimer:** Real port scanners are complex. This is a simplified exercise for understanding sockets. Be ethical!
18. **Process Lister:**
    *   Write a script that uses `subprocess` to run a command that lists running processes on your OS (`tasklist` on Windows, `ps aux` on Linux/macOS).
    *   Parse the output (this might be tricky!) to extract and print just the Process ID (PID) and the process name/command for each process.
    *   **Challenge:** This requires string manipulation or potentially regex depending on the command output format.
19. **Threat Intel API Client (Example):**
    *   Choose a free Threat Intelligence API (e.g., AbuseIPDB, VirusTotal - you'll likely need a free API key).
    *   Write a script that takes an IP address or file hash as a command-line argument.
    *   Uses the `requests` library to query the chosen API about the indicator.
    *   Parses the JSON response and prints a summary of the findings (e.g., reputation score, detection ratio).
    *   Remember to handle your API key securely (e.g., environment variable, config file - **don't hardcode it!**). Use the `ConfigManager` class from Problem 16 if you like.
20. **Attack Simulation - Scheduled Task/Cron Job Creation (Benign):**
    *   **Goal:** Simulate an adversary achieving persistence.
    *   Write a script that uses `subprocess` to create a *benign* scheduled task (Windows) or cron job (Linux/macOS).
    *   The task/job should simply run a command like `echo "Purple Team test task ran" >> task_log.txt`.
    *   **Research:** You'll need to find the correct command-line syntax for `schtasks.exe` (Windows) or modifying crontab (Linux/macOS). This requires care!
    *   **Bonus:** Write a corresponding script to *delete* the created task/job.

---

**Level 6: Data Analysis & Security Library Integration**

*   **Objective:** Use data analysis libraries for larger datasets and integrate with security-specific Python tools.
*   **Concepts:** `pandas` library basics, `python-nmap` (optional), interacting with SIEM APIs (conceptual).

*(Remember `pip install pandas python-nmap` if trying those)*

21. **Log Analysis with Pandas:**
    *   Take your `auth_logs.csv` (Problem 9) or generate a larger one.
    *   Load the CSV into a pandas DataFrame (`pd.read_csv()`).
    *   Use pandas to:
        *   Count the number of successful vs. failed logins (`df['Status'].value_counts()`).
        *   Find the top 5 source IPs with the most failed login attempts.
        *   Group by user and count their login attempts.
    *   Print these summary statistics.
22. **Network Scan with python-nmap (Optional & Careful!):**
    *   If you have Nmap installed and the `python-nmap` library.
    *   Write a script that uses `nmap.PortScanner()` to perform a *simple* scan (e.g., top 20 ports) against a *single target you own or have permission for* (like your local machine's IP or `127.0.0.1`).
    *   Iterate through the scan results and print the open ports found for the host.
    *   **Again: Be ethical and responsible with scanning.**
23. **SIEM Query Simulation:**
    *   **Conceptual:** Most SIEMs have REST APIs. Imagine an endpoint `/api/v1/query` that accepts a query string (like Splunk SPL or Elastic KQL) and returns JSON results.
    *   Write a function `query_siem(query_string)` that *simulates* this:
        *   It should print the query it "received".
        *   It should return a *predefined, sample JSON structure* representing potential SIEM results (e.g., a list of log events as dictionaries).
    *   Write a main script part that defines a sample query (e.g., "search failed logins last 24h") and calls `query_siem`, then prints the simulated results prettily (`json.dumps` with indentation). This focuses on the Python client-side interaction pattern.

---

**Level 7: Automation & Integration - Capstone Challenges**

*   **Objective:** Combine multiple skills to build more complex, automated workflows.

24. **Automated Indicator Enrichment Tool:**
    *   Create a script that takes a file containing a list of IP addresses (one per line) as input (`argparse`).
    *   For each IP address:
        *   Query a Threat Intel API (like Problem 19) using your `ApiClient` or a dedicated class.
        *   Optionally, perform a *very limited* port check using your function from Problem 17 (e.g., check only port 80/443). **Be mindful of API rate limits and scanning ethics.**
        *   Append the IP address and its enrichment results (reputation, open ports found) to an output CSV file. Use the `csv` module.
    *   Include robust error handling for file operations and API requests.
25. **Basic Log Anomaly Detector:**
    *   Use pandas (Problem 21) to analyze a log file (e.g., `auth_logs.csv`).
    *   Calculate the baseline: e.g., average number of failed logins per hour or per user.
    *   Process the log chronologically (you might need to parse timestamps properly using `pd.to_datetime`).
    *   Identify and print any time periods or users where the number of failed logins significantly exceeds the baseline (e.g., > 3 standard deviations above the mean, or simply > 10 failures in 5 minutes). This is a very basic anomaly detection approach.
26. **Detection Rule Tester:**
    *   **Concept:** Test if a detection rule (e.g., in a SIEM) triggers correctly.
    *   Write a script that simulates the *action* that *should* trigger a specific, simple detection rule you know exists (or you set up yourself in a lab SIEM/tool).
    *   **Example:** If you have a rule for "Scheduled Task Creation", run your script from Problem 20. If you have a rule for "Potential Password Spray" (e.g., 5 failed logins for the *same* user in 1 minute), simulate those failed login *events* by sending appropriately formatted logs to your log collector (if possible) or interacting with an authentication endpoint (if available in a lab). **This requires a test environment.**
    *   After running the simulation script, manually check (or use an API if available) if the expected alert was generated. The Python script's job is just to perform the trigger action.

---

**Level 8: Advanced Concepts & Refinement**

*   **Objective:** Explore concurrency, packaging code for distribution, and more specialized libraries.

27. **Concurrent Port Checker (Threading):**
    *   Modify your port checking script (Problem 17/24). Use the `threading` module to check multiple ports on a *single* host concurrently. This can speed things up compared to checking sequentially.
    *   **Challenge:** Manage threads correctly, collect results from different threads.
28. **Packaging Your Tool:**
    *   Take one of your more complex tools (e.g., Indicator Enrichment Tool - Problem 24).
    *   Organize it into a proper Python package structure (e.g., a directory with `__init__.py`, your main script, helper modules).
    *   Create a `pyproject.toml` (or `setup.py`) file to make your tool installable via `pip`.
    *   Build a wheel (`pip install build`, `python -m build`) and try installing it locally (`pip install dist/your_tool.whl`).
29. **Explore Scapy (Advanced Packet Crafting):**
    *   *(Requires `pip install scapy` and platform dependencies like Npcap/WinPcap)*. **This is advanced and potentially disruptive if misused.**
    *   Write a script using Scapy to craft and send a *single*, simple packet, like an ICMP echo request (ping). Send it to your local machine (`127.0.0.1`).
    *   Write another script to *sniff* for ICMP packets on your local loopback interface for a few seconds and print a summary of any captured packets.
    *   **Focus:** Understand the basic syntax of packet building (`IP()/ICMP()`) and sniffing (`sniff()`). Use with extreme caution.
30. **Contribute (Simulated):**
    *   Find an open-source security tool written in Python on GitHub.
    *   **Don't actually make changes yet.** Instead, *analyze* a small part of its code.
    *   Identify one small function or class. Read it, understand what it does, and how it fits into the larger tool.
    *   Write comments explaining the code block you analyzed. This practices code reading and comprehension, vital skills.

---

**Debrief:** Completing this extensive mission will give you a powerful Python skillset specifically tailored for Purple Team activities. Remember, mastery comes from continuous practice, building your own tools, and adapting to new challenges and technologies. Good luck, Agent!