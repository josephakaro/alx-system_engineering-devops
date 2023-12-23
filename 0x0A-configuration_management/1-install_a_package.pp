# ... Installing Flask from pip3:
# ... Requirements:
# - pip3
# - Flask=2.1.0

package{'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
