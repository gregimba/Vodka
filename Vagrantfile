VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  
  config.vm.hostname = "vodka"
  
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end
  
  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "deploy/vagrant.yml"
  end
end
