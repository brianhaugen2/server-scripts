# Reverse SSH Tunnel Instructions

The reverse SSH tunnel is created on the computer you want to SSH into (home) and creating a path to a public computer (server).
Once this tunnel is created, you can use a third computer to SSH into your home computer through the public server tunnel.
1. Home Computer: 
    1. `ssh -R 1234:localhost:22 [server_username]@[server_ip] -p 22`
2. Random Computer:
    1. `ssh [server_username]@[server_ip] -p 22`
    2. Now in the server
    3. `ssh [home_username]@localhost -p 1234`
    4. Now in the home computer
