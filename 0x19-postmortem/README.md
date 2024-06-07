# Incident Report for 504 Error / Site Outage
<br>

## Summary
On Jun 4th, 2024 at midnight, the server experienced a 504 error, resulting in a website outage. The server operates on a LAMP stack.

## Timeline

- 00:00 CAT - Users encounter 500 error while accessing the website.
- 00:05 CAT - Verified that Apache and MySQL were running.
- 00:10 CAT - The website failed to load properly, but both the server and database were functioning correctly.
- 00:12 CAT - Restarted Apache server, which returned a status 200 (OK) upon using curl on the website.
- 00:18 CAT - Began reviewing error logs to identify the source of the error.
- 00:25 CAT - Discovered that the Apache server was being prematurely shut down; PHP error logs were missing.
- 00:30 CAT - Found that error logging was disabled in the php.ini settings; enabled error logging.
- 00:32 CAT - Restarted Apache server and reviewed PHP error logs.
- 00:36 CAT - Identified a mistyped file name in the PHP error logs, causing incorrect loading and premature shutdown of Apache.
- 00:38 CAT - Corrected the file name and restarted Apache server.
- 00:40 CAT - Server returned to normal operation and the website loaded correctly.

## Root Cause and Resolution
The issue stemmed from a misspelled file name in the wp-settings.php file, leading to a 500 error. Initially, error logging was disabled, preventing immediate identification of the issue. After enabling error logging in the php.ini file and restarting the server, the PHP error logs indicated that a file with a .phpp extension was missing. Correcting the file extension resolved the error. To prevent recurrence across other servers, a Puppet deployment script was used to fix the file name, ensuring all servers were updated. This action restored normal site and server operation.

## Corrective and Preventive Measures
Ensure error logging is always enabled on all servers to facilitate quick identification of issues.
Test all servers and sites locally before deploying to a multi-server setup to minimize downtime and troubleshooting during live deployments.
