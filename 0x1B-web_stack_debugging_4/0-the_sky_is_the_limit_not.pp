# Increase the ULIMIT in the default Nginx file
exec {'increase_ulimit_for_nginx':
	command		=> 'sed -i "s/15/4096/" /etc/default/nginx',
	path		=> ['/usr/local/bin', '/bin'],
	unless		=> 'grep -q "4096" /etc/default/nginx', # Prevents the command from running if the limit is already set
	notify		=> Exec['nginx-restart'],               # Triggers nginx restart after the change
}

# Restart Nginx
exec {'nginx-restart':
	command		=> '/etc/init.d/nginx restart',
	path		=> ['/sbin', '/bin', '/usr/sbin', '/usr/bin'],
	refreshonly	=> true,  # Ensures this exec only runs when notified
}
