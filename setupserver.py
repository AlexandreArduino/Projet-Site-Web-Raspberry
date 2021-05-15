import os
import shutil

#Alexander B.
#Contribution to the Chrapati's project :-)

'''
For the developpers, all the files in files_to_move[] will be move in the web directory :-)
Actually, all the files in this directory including this setup installation :p
'''
input("[WARNING] => This code was not tested !")

def install_server():
    files_to_move = os.listdir()
    input("Welcome to the webserver installation !\nPress enter to start the installation on your Raspberry Pi or Linux Distribution ;) ...")
    os.system('sudo apt-get update -y')
    os.system('sudo apt-get upgrade -y')
    os.system('sudo apt install apache2 -y')
    os.system('sudo chown -R pi:www-data /var/www/html/')
    os.system('sudo chmod -R 770 /var/www/html/')
    for file in range(0, len(files_to_move)):
        shutil.copy(files_to_move[file], "/var/www/html/" + files_to_move[file])
    del file, files_to_move #Just to optimize the RAM if this directory contains a lot of files!
    input("Now, you just need to do port forward and you server is ready ! Now, you can run : http://127.0.0.1/ to test it in your local network!\nPress enter to exit ...")
install_server()