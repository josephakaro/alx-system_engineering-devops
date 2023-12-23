# ... Installing Flask from pip3:
# ... Requirements:
# - pip3
# - Flask=2.1.0

package{'Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider  => 'pip3',
}
