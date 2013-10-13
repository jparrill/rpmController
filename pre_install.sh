yum install cifs-utils git rpm-build -y
mkdir -p /mnt/artifacts/
mount -t cifs  -o username=contint,password=admintid33,domain=hi,gid=502,uid=502,nobrl \\\\oriente\\artifacts  /mnt/artifacts/

