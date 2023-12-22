# ... Create a file in '\tmp' directory with the following requirements:
# - Filename: school
# - File content: I love Puppet
# - File permissions: 0744
# - File owner: www-data
# - File group: www-data
# - File location: /tmp/school

file{ '0-create_a_file':
  ensure  => 'file',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
