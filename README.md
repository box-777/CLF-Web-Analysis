# CLF-Web-Analysis
Simple CLI tool that analyses IPs, Useragents and peak hours for CLF web server logs.  Type -h to get started.

```usage: clf_web_analysis.py [-h] [-i] [-b] [-u] [-s] PATH

Analyse CLF format web server logs.

positional arguments:
  PATH              Path to .log file

options:
  -h, --help        show this help message and exit
  -i, --ipcounts    Find unique IPs and the number of HTTP requests sent.
  -b, --busyhours   Find the busiest hour of each day (in chronological order).
  -u, --useragents  Find unique User Agents and number of occurrences.
  -s, --sort        Sorts results DESC (only for -i|-u)```
