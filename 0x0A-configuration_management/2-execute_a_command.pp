# ... Create a manifest that kills a process named killmenow
# - Process bash script file: killmenow
# - Process name: killmenow

exec{'killmenow':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
