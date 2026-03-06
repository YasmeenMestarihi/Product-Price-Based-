#!/bin/bash

# Automated installation script for Odoo module

# Function to install required modules
install_modules() {
    echo 'Installing required modules...'
    pip install -r requirements.txt
}

# Function to set permissions
set_permissions() {
    echo 'Setting permissions...'
    sudo chown -R odoo:odoo .
    sudo chmod -R 755 .
}

# Function to restart Odoo service
restart_odoo() {
    echo 'Restarting Odoo service...'
    sudo systemctl restart odoo.service
}

# Execute functions
install_modules
set_permissions
restart_odoo

echo 'Installation complete!'