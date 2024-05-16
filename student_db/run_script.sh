echo "Installing MySQL server..."
sudo apt-get update
sudo apt-get install -y mysql-server

# Start MySQL service.
echo "Starting MySQL service..."
sudo service mysql start

# Run SQL scripts
echo "Setting up databases and tables..."
sudo mysql -u root << EOF
SOURCE create_table.sql;
SOURCE insert_data.sql;
SOURCE queries.sql;
SOURCE data_manipulation.sql;
EOF

echo "Setup complete! MySQL has been installed and database is set up."
