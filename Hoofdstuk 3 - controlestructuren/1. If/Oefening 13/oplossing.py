bestandsgrootte_MB = float(input("Bestandsgrootte (in MB): "))
downloadsnelheid_Mbps = float(input("Downloadsnelheid (in Mbps): "))

downloadsnelheid_MBps = downloadsnelheid_Mbps / 8

seconden = bestandsgrootte_MB / downloadsnelheid_MBps

if seconden > 60*60:
    print("Opgelet: download duurt langer dan een uur.")