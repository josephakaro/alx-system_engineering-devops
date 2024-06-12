# Ensure the Holberton user has appropriate file limits

# Increase hard file limit for Holberton user
exec {'increase-hard-file-limit-for-holberton-user':
	command		=> 'sed -i "s/holberton hard nofile [0-9]*/holberton hard nofile 50000/" /etc/security/limits.conf',
	path		=> ['/usr/local/bin', '/bin'],
	unless		=> 'grep -q "holberton hard nofile 50000" /etc/security/limits.conf', # Prevents the command from running if the limit is already set
}

# Increase soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command	=> 'sed -i "s/holberton soft nofile [0-9]*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path		=> ['/usr/local/bin', '/bin'],
  unless	=> 'grep -q "holberton soft nofile 50000" /etc/security/limits.conf', # Prevents the command from running if the limit is already set
}
