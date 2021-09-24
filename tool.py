#SECURITY_GANG//
import os

#OS
while True:
    print('''
    Select your OS:
        [1] = Termux
        [2] = Linux
    \n''')

    cmd = input('==> ')
    if cmd == "1":
        print('''
    [1] Install tools Termux
    [2] Download Tor Browser [Android] 
    [3] Coming soon...
            ''')
        tmx_1 = input('==> ')
        if tmx_1 == "1":
            print('[+] Please Wait!')
            os.system('apt-get install tor wget curl git >> install.log')
            os.system('termux-setup-storage')
            os.system('rm install.log')
            print('[+] INSTALLED!')
        elif tmx_1 == "2":
            print('''Select your architecture:
    [1] = aarch64
    [2] = arm(hf/64/v7)
    [3] = x86_64 (64 bit)
    [4] = x86 (32 bit)
            ''')
            tor_br = input('==> ')
            if tor_br == "1":
                print('aarch64')
                os.system('wget https://dist.torproject.org/torbrowser/10.5.5/tor-browser-10.5.5-android-aarch64-multi.apk')
                os.system('mv tor-browser-10.5.5-android-aarch64-multi.apk storage/shared/')
                print('[+] All Good!')
            elif tor_br == "2":
                print('arm')
                os.system('wget https://dist.torproject.org/torbrowser/10.5.5/tor-browser-10.5.5-android-armv7-multi.apk')
                os.system('mv tor-browser-10.5.5-android-armv7-multi.apk storage/shared/')
                print('[+] All Good!')
            elif tor_br == "3":
                print('64 bit')
                os.system('wget https://dist.torproject.org/torbrowser/10.5.5/tor-browser-10.5.5-android-x86_64-multi.apk')
                os.system('mv tor-browser-10.5.5-android-x86_64-multi.apk storage/shared/')
                print('[+] All Good!')
            elif tor_br == "4":
                print('32 bit')
                os.system('wget https://dist.torproject.org/torbrowser/10.5.5/tor-browser-10.5.5-android-x86-multi.apk')
                os.system('mv tor-browser-10.5.5-android-x86-multi.apk storage/shared/')

    if cmd == "2":
        print(''' Select:
    [1] = Install TOOLS
    [2] = Install TOR_Browser
    ''')
        tor_br_2 = input('==> ')
        if tor_br_2 == "1":
            os.system('sudo apt-get install tor proxychains4 wget gcc make git xz-utils >> install.log')
            os.system('rm install.log')
            os.system('sudo service tor start')
            tor_ip = input('Show your Tor IP? (y/n): ')
            if tor_ip == "y":
                os.system('proxychains4 curl ident.me')

            elif tor_ip == "n":
                print('[!] Ok.')
        if tor_br_2 == "2":
            print('''
    Select your Arch:
    [1] = 32bit
    [2] = 64bit        
            ''')
            tor_linux = input('==> ')
            if tor_linux == "1":
                print('[32bit]')
                os.system('wget https://www.torproject.org/dist/torbrowser/11.0a5/tor-browser-linux32-11.0a5_en-US.tar.xz')
                os.system('tar -xf tor-browser-linux32-11.0a5_en-US.tar.xz')
                os.system('rm -rf tor-browser-linux32-11.0a5_en-US.tar.xz')
                print('[+] All Good!')
            elif tor_linux == "2":
                print('[64bit]')
                os.system('wget https://www.torproject.org/dist/torbrowser/11.0a5/tor-browser-linux64-11.0a5_en-US.tar.xz')
                os.system('tar -xf tor-browser-linux64-11.0a5_en-US.tar.xz')
                os.system('rm -rf tor-browser-linux64-11.0a5_en-US.tar.xz')
            else:
                print('Unknown')
