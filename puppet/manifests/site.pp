import 'nodes/*.pp'
notify {"Installing rpmcrontoller...":}


Exec{
     logoutput => true,
}



