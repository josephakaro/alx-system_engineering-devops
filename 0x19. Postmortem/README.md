# Incident Report: 504 Error / Site Outage

<div align="center">
  <img src="https://giphy.com/gifs/noodlesagency-fire-server-serveronfire-sMKedUx9w9m8OGwXi6" alt="Server Hell GIF">
</div>

## Summary
On September 11th, 2018, the server experienced an outage at midnight, leading to a 504 error for users attempting to access the website. The server operates on a LAMP stack.

## Timeline
- 00:00 PST: Users encounter a 500 error when attempting to access the website.
- 00:05 PST: Verification of Apache and MySQL status.
- 00:10 PST: Website displays improper loading, investigation reveals proper server and database functioning.
- 00:12 PST: Quick Apache server restart resolves issue, returns status 200 and OK upon curling the website.
- 00:18 PST: Review of error logs to identify the source of the error.
- 00:25 PST: Examination of ``/var/log`` indicates premature shutdown of the Apache server; PHP error logs are missing.
- 00:30 PST: Inspection of ``php.ini`` settings reveals disabled error logging; enabled error logging.
- 00:32 PST: Apache server restarted, error logs checked for PHP error logging.
- 00:36 PST: PHP error logs show mistyped file name causing incorrect loading and premature server closure.
- 00:38 PST: File name corrected, Apache server restarted.
- 00:40 PST: Server resumes normal operation, website loads properly.
## Root Cause and Resolution
The issue stemmed from a misnamed file referenced in ``wp-settings.php``, leading to a 500 error upon server curl. Absence of PHP error logs prompted investigation, revealing disabled error logging in ``php.ini``. Upon enabling error logging and restarting Apache, PHP error logs indicated a misspelled file extension in ``wp-settings.php``. This error likely existed across multiple servers. Rectification involved correcting the file extension via Puppet code deployment, ensuring uniform resolution across servers.

### Corrective and Preventive Measures
- Enable error logging on all servers and sites to facilitate error identification.
- Conduct local testing before deploying on multi-server setups to preemptively address errors, minimizing downtime in case of site failures.