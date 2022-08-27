# create a file in /tmp/school with permissions 0744
# owner is www-data, group is www-data

  file { '/tmp/school':
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data'
  }
