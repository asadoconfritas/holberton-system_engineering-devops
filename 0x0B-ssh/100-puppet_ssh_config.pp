# setting up a client SSH configuration file
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0744',
  content => 'Host * \n PasswordAuthentication no\n IdentityFile ~/.ssh/school'
}
