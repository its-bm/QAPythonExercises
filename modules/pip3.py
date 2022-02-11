# If working on a new machine with pre-existing code we may need to make installs, sometimes an app may require 100s of installs
# Can use .txt file called requirements.txt
# Operators 
# == equal to exact version
# ~= latest compatible release in same version
# >= latst version, greater than specified release

# Package | Operator | File version
# requests~=2.23.0
# pytest>=6.1.2
# pytest-cov==2.10.01

# Install - pip3 install -r requirements.txt

# Put previously installed packages in a .txt file - pip3 freeze > requirements.txt