# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            # Return Hello World! for GET requests to /
            if ($request_method = 'GET') {
                return 200 'Hello World!\n';
            }
        }

        location /redirect_me {
            # Perform a 301 redirect
            return 301 /new_location;
        }

        location /new_location {
            # Example page for redirected URL
            return 200 'This page was redirected!\n';
        }
    }
  ",
  notify  => Service['nginx'],
}

# Create symlink to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

