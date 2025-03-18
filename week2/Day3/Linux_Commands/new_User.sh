#!\bin\bash

if [ -z "$1" ]; then
    echo "Error: Missing parameter username."
    exit 1
fi

if id "$1" >/dev/null 2>&1; then
    echo "User '$1' already exists."
else
    echo "Adding user '$1'..."
    sudo adduser "$1"
    sudo passwd "$1"
fi

sudo usermod -aG wheel "$1"
echo "User '$1' added to the 'wheel' group."

echo "Enter the group name in which you want to add user:"
read group

sudo usermod -aG "$group" "$1"
echo "User '$1' added to the '$group' group."