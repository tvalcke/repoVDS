import subprocess

subprocess.run('dir', shell=True)

my_sub = subprocess.run('dir', shell=True)
print("Résultat sans capture de sortie : ", my_sub.stdout)

my_sub = subprocess.run('dir', shell=True, capture_output=True)
print("Résultat avec capture de la sortie : ", my_sub.stdout)

my_sub = subprocess.run('dir', shell=True, capture_output=True,
                        universal_newlines=True)
print("Avec capture de la sortie et texte brut : ", my_sub.stdout)

my_sub = subprocess.run('ls tartempion.txt', shell=True, capture_output=True,
                        universal_newlines=True)
print("Sortie lorsque le fichier n'existe pas : ", my_sub.stdout)
print("Message d'erreur (stderr) : ", my_sub.stderr)

my_sub = subprocess.run('dir', shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, universal_newlines=True)
print("Sortie standard : ", my_sub.stdout)
print("Erreurs : ", my_sub.stderr)

my_text = """
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
        options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
        nd6 options=201<PERFORMNUD,DAD>
    gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
    stf0: flags=0<> mtu 1280
    ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3e:22:fb:60:4a:5f
        media: autoselect
        status: inactive
    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=400<CHANNEL_IO>
        ether 3c:22:fb:60:4a:5f
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect (<unknown type>)
        status: inactive
    en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST>
        mtu 1500 options=460<TSO4,TSO6,CHANNEL_IO> ether d2:c0:77:f9:9c:00
        media: autoselect <full-duplex> status: inactive"""

my_sub2 = subprocess.run('findstr "flag"', input=my_text,
                         text=True, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Lignes contenant 'flag' : ", my_sub2.stdout)
print("Messages d'erreur : ", my_sub2.stderr)

ifconfig_process = subprocess.Popen(
    'ifconfig', shell=True, stdout=subprocess.PIPE)

grep_process = subprocess.run('grep "en0"', shell=True,
                              stdin=ifconfig_process.stdout,
                              capture_output=True, text=True)
print("Interface réseau principale trouvée : ", grep_process.stdout)
