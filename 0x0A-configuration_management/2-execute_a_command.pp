# ... Create a manifest that kills a process named killmenow
/*
  - Process bash script file: killmenow
  - Process name: killmenow
*/
exec{'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
}
