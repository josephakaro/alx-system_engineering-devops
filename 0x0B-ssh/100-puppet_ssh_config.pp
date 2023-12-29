file{ '/home/joseph/.ssh/config':
    ensure  => file,
    owner   => 'ubuntu'
    group   => 'ubuntu'
    mode    => '0600',
    content => '
}
