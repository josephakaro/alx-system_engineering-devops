# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { 'nginx':
  manage_repo => true,
}

# Configure Nginx with custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}

# Custom HTTP header template
file { '/etc/nginx/custom_header.template':
  ensure  => file,
  content => "add_header X-Served-By $hostname;",
}

exec { 'generate_custom_header':
  command     => 'envsubst < /etc/nginx/custom_header.template > /etc/nginx/custom_header.conf',
  refreshonly => true,
  subscribe   => File['/etc/nginx/custom_header.template'],
  notify      => Service['nginx'],
}

