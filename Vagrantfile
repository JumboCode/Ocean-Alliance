# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vagrant.plugins = "vagrant-vbguest"

  # config.ssh.forward_agent = true
  config.ssh.forward_x11 = true
  
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # allow for symlinks in vb
    vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant/", "1"]

    # windows path limit fix
    # vb.customize ["sharedfolder", "add", :id, "--name", "www", "--hostpath", (("//?/" + File.dirname(__FILE__) + "/www").gsub("/","\\"))]
    
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # windows path limit fix
  # config.vm.provision :shell, inline: "mkdir /home/vagrant/www"
  # config.vm.provision :shell, inline: "mount -t vboxsf -o uid=`id -u vagrant`,gid=`getent group vagrant | cut -d: -f3` > www /home/vagrant/www", run: "always"
  
  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
  
  # remember to setup environment variable https://superuser.com/a/392263
  # as well as running electron rebuild

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    apt-get -y update
    apt-get -y upgrade

    apt-get -y install cmake

    #x11 forwarding
    apt-get -y install xauth
    apt-get -y install x11-apps

    apt-get -y install python3
    apt-get -y install python3-pip
    
    apt-get -y install emacs
    
    apt-get -y install nodejs
    apt-get -y install npm
    apt-get -y install build-essential
    
    apt-get -y install libzmq3-dev
    apt-get -y install libnss3
    apt-get -y install libxss1

    
    cd /vagrant
    pip3 install -r /vagrant/requirements.txt
    npm install --force

    ./node_modules/.bin/electron-rebuild
    
    SHELL
end
