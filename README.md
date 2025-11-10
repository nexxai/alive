# Alive

A Python tool to discover alive subdomains for a given domain by querying
crt.sh certificate transparency logs and verifying DNS resolution.

## Why This Matters

Certificate Transparency (CT) logs like crt.sh provide a public record of
SSL/TLS certificates issued for domains. This tool leverages CT data to find
subdomains that may not be publicly listed, which is valuable for:

- Security research and reconnaissance
- Bug bounty hunting
- Network mapping and asset discovery
- Identifying potentially forgotten or misconfigured subdomains

## Features

- Fetches certificate data from crt.sh API
- Extracts unique hostnames from certificates (excluding wildcards)
- Verifies DNS resolution to find "alive" domains
- Saves results to timestamped files
- Comprehensive test suite with mocked API and DNS calls

## Installation

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Setup

1. Clone or download the repository
2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool with a root domain:

```bash
python main.py example.com
```

The tool will:

1. Query crt.sh for certificates issued to `example.com`
2. Extract unique hostnames from certificate data
3. Check DNS resolution for each hostname
4. Save alive domains to `results/alive_example_com_YYYYMMDD_HHMMSS.txt`

### Output

The tool provides real-time progress:

```
[-] Fetching certificates for example.com from crt.sh...
[+] Fetched 150 certificates
[-] Extracting unique hostnames from certificates...
[+] Extracted 45 unique hostnames
[-] Checking DNS resolution...
[+] Found 32 alive domains
[-] Saving results to results/alive_example_com_20251110_125644.txt
[+] Saved results to results/alive_example_com_20251110_125644.txt
```

## Testing

Run the test suite:

```bash
pytest
```

The tests include:

- Unit tests for each module with mocked dependencies
- Integration tests for the main workflow
- API response mocking and DNS resolution simulation

## Project Structure

```
alive/
├── src/                   # Core modules
│   ├── __init__.py
│   ├── cert_utils.py      # Certificate fetching and parsing
│   ├── dns_utils.py       # DNS resolution checking
│   └── save_utils.py      # Result file saving
├── tests/                 # Test suite
│   ├── test_cert_utils.py
│   ├── test_dns_utils.py
│   ├── test_integration.py
│   └── test_save_utils.py
├── main.py                # Entry point
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## Dependencies

- `requests` - HTTP client for API calls
- `pytest` - Testing framework
- `pytest-mock` - Mocking utilities for tests

## Contributing

All contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. **Add comprehensive test cases** for any new functionality
5. Ensure all existing tests pass
6. Submit a pull request

All contributions **must** include appropriate test coverage. This helps maintain
code quality and prevents regressions.

## License

MIT License - see LICENSE file for details

## Disclaimer

Use responsibly and in accordance with applicable laws and terms of service.
Certificate transparency data is public, but always respect rate limits and
avoid excessive querying.
