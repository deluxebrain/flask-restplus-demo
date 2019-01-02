# flask-restplus-demo

Quick demo of using Flask, Flask-RestPlus and Flask-Marshmallow to deliver a RESTful Web api.

## Vagrant usage

### Basic workflow

```sh
# Fire up virtual machine
vagrant up

# Connect to virual machine over ssh
vagrant ssh

# Tear down virtual machine
vagrant destroy --force
```

## Development workflow

```sh
# Re-run Ansible provisioners
vagrant provision --provision-with ansible_local
```
