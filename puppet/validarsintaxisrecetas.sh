#/bin/bash

result=`gem query --local | grep puppet-lint | wc -l`
if [ $result == 0 ]; then
         echo "Installing puppet-lint..."
     gem install puppet-lint
fi

echo "Check Syntaxis:"
echo "###################"
find . -type f -size +0 -name *.pp | grep -v site.pp | xargs puppet parser validate

echo "Check that your Puppet manifest conform to the style guide"
echo "##########################################################"
find . -type f -size +0 -name *.pp | grep -v site.pp | xargs puppet-lint --with-filename
puppet-lint 
