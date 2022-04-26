#installing and configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
