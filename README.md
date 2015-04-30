# Awesome CTF [![Build Status](https://travis-ci.org/apsdehal/awesome-ctf.svg?branch=master)](https://travis-ci.org/apsdehal/awesome-ctf)

A curated list of [Capture The Flag](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) (CTF) frameworks, libraries, resources and softwares.

### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md) first.

#### _If you know a tool that isn't present here, feel free to open a pull request._

### Why?

It takes time to build up collection of tools used in ctf and remember them all. This repo helps to keep all these scattered tools at one place.


### Contents

- [Awesome CTF](#awesome-ctf)
  - [Create](#create)
    - [Forensics](#forensics)
    - [Web](#web)
  - [Solve](#solve)
    - [Attacks](#attacks)
    - [Bruteforcers](#bruteforcers)
    - [Cryptography](#crypto)
    - [Exploits](#exploits)
    - [Forensics](#forensics-1)
    - [Miscellaneous](#misc)
    - [Reversing](#reversing)
    - [Services](#services)
    - [Steganography](#stegano)
    - [Web](#web-1)

- [Resources](#resources)
  - [Tutorials](#tutorials)
  - [Wargames](#wargames)
  - [Websites](#websites)
  - [Wikis](#wikis)
  - [Writeups Collections](#writeups)

# Create

*Tools used for creating CTF challenges*

## Forensics

*Tools used for creating Forensics challenges*

- [Registry Dumper](http://www.kahusecurity.com/tools/RegistryDumper_v0.1.zip) - Dump your registry

## Web

*Tools used for creating Web challenges*

*JavaScript Obfustcators*

- [Metasploit JavaScript Obfustcator](https://github.com/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit)
- [Uglify](http://marijnhaverbeke.nl//uglifyjs)


# Solve

*Tools used for solving CTF challenges*

## Attacks

*Tools used for performing various kinds of attacks*

- [Layer 2 attacks](https://github.com/tomac/yersinia) - Attack various protocols on layer 2

## Crypto

*Tools used for solving Crypto challenges*

- [RSATool](https://github.com/ius/rsatool) - Generate private key with knowledge of p and q
- [XORTool](https://github.com/hellman/xortool) - A tool to analyze multi-byte xor cipher

## Bruteforcers

*Tools used for various kind of bruteforcing (passwords etc.)*

- [John The Jumbo](https://github.com/magnumripper/JohnTheRipper) - Community enhanced version of John the Ripper
- [John The Ripper](http://www.openwall.com/john/) - Password Cracker
- [Ophcrack](http://ophcrack.sourceforge.net/) - Windows password cracker based on rainbow tables.

## Exploits

*Tools used for solving Exploits challenges*

- [binjitsu](https://github.com/binjitsu/binjitsu/) - CTF framework and exploit development library
- [Metasploit](http://www.metasploit.com/) - Penetration testing software
- [pwntools](https://github.com/Gallopsled/pwntools) - CTF Framework for writing exploits

## Forensics

*Tools used for solving Forensics challenges*

- [Aircrack-Ng](http://www.aircrack-ng.org/) - Crack 802.11 WEP and WPA-PSK keys
  - `apt-get install aircrack-ng`
- [Audacity](http://sourceforge.net/projects/audacity/) - Analyze sound files (mp3, m4a, whatever)
  - `apt-get install audacity`
- [bkhive and samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/) - Dump SYSTEM and SAM files
  - `apt-get install samdump2 bkhive`
- [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE Editor
- [creddump](https://code.google.com/p/creddump/) - Dump windows credentials
- [extundelete](http://extundelete.sourceforge.net/) - Used for recovering lost data from mountable images
- [Foremost](http://foremost.sourceforge.net/) - Extract particular kind of files using headers
  - `apt-get install foremost`
- [fsck.ext4](http://linux.die.net/man/8/fsck.ext3) - Used to fix corrupt filesystems
- [Malzilla](http://malzilla.sourceforge.net/) - Malware hunting tool
- [PDF Streams Inflater](http://malzilla.sourceforge.net/downloads.html) - Find and extract zlib files compressed in PDF files
- [ResourcesExtract](http://www.nirsoft.net/utils/resources_extract.html) - Extract various filetypes from exes
- [Shellbags](https://github.com/williballenthin/shellbags) - Investigate NT\_USER.dat files
- [UsbForensics](http://www.forensicswiki.org/wiki/USB_History_Viewing) - Contains many tools for usb forensics
- [Volatility](https://github.com/volatilityfoundation/volatility) - To investigate memory dumps
- [Wireshark](https://www.wireshark.org/) - Analyze the network dumps
  - `apt-get install wireshark`

*Registry Viewers*
- [RegistryViewer](http://www.gaijin.at/en/getitpage.php?id=regview) - Used to view windows registries
- [Windows Registry Viewers](http://www.forensicswiki.org/wiki/Windows_Registry) - More registry viewers

## Reversing

*Tools used for solving Reversing challenges*

- [Androguard](https://github.com/androguard/androguard) - Reverse engineer Android applications
- [Apk2Gold](https://github.com/lxdvs/apk2gold) - Yet another Android decompiler
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - Android Decompiler
- [BinUtils](http://www.gnu.org/software/binutils/binutils.html) - Collection of binary tools
- [BinWalk](https://github.com/devttys0/binwalk) - Analyze, reverse engineer, and extract firmware images.
- [Boomerang](https://github.com/nemerle/boomerang) - Decompile x86 binaries to C
- [IDA Pro](https://www.hex-rays.com/products/ida/) - Most used Reversing software
- [Jadx](https://github.com/skylot/jadx) - Decompile Android files
- [Krakatau](https://github.com/Storyyeller/Krakatau) - Java decompiler and disassembler
- [Uncompyle](https://github.com/gstarnberger/uncompyle) - Decompile Python 2.7 binaries (.pyc)

*JavaScript Deobfustcators*

- [Detox](http://relentless-coding.org/projects/jsdetox/install) - A Javascript malware analysis tool
- [Revelo](http://www.kahusecurity.com/tools/Revelo_v0.6.zip) - Analyze obfuscated Javascript code

## Services

*Various kind of useful services available around the internet*

- [CSWSH](http://ironwasp.org/cswsh.html) - Cross-Site WebSocket Hijacking Tester
- [Request Bin](http://requestb.in/) - Lets you inspect http requests to a particular url

## Stegano

*Tools used for solving Steganography challenges*

- [pngtools](http://www.stillhq.com/pngtools/) - For various analysis related to PNGs
  - `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) - Used to deblur and fix defocused images
- [Steganabara](https://www.openhub.net/p/steganabara) -  Tool for stegano analysis written in Java
- [Steghide](http://steghide.sourceforge.net/) - Hide data in various kind of images
- [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - Apply various steganography techniques to images

## Web

*Tools used for solving Web challenges*

- [SQLMap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection and database takeover tooli
- [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor


# Resources

*Where to discover about CTF*

## Tutorials

*Tutorials to learn how to play CTFs*

- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Field Guide by Trails of Bits
- [CTF Resources](http://ctfs.github.io/resources/) -  Start Guide maintained by community

## Wargames

*Always online CTFs*

- [Backdoor](https://backdoor.sdslabs.co/) - Security Platform by SDSLabs
- [Exploit Exercises](https://exploit-exercises.com/) - Variety of VMs to learn variety of computer security issues
- [Hack This Site](https://www.hackthissite.org/) - Training ground for hackers.
- [Over The Wire](http://overthewire.org/wargames/) - Wargame maintained by OvertheWire Community
- [WeChall](https://www.wechall.net/) - Always online challenge site

## Websites

*Various general websites about and on ctf*

- [CTF Time](https://ctftime.org/) - General information on CTF occuring around the worlds
- [Reddit Security CTF](http://www.reddit.com/r/securityctf) - Reddit CTF category

## Wikis

*Various Wikis available for learning about CTFs*

- [ISIS Lab](https://github.com/isislab/Project-Ideas/wiki) - CTF Wiki by Isis lab

## Writeups Collections

*Collections of CTF write-ups*

- [CTF write-ups (community)](https://github.com/ctfs/) - CTF challenges + write-ups archive maintained by the community
- [pwntools writeups](https://github.com/Gallopsled/pwntools-write-ups) - A collection of CTF write-ups all using pwntools
- [Shell Storm](shell-storm.org/repo/CTF/) - CTF challenge archive maintained by Jonathan Salwan
- [Smoke Leet Everyday](https://github.com/smokeleeteveryday/CTF_WRITEUPS) - CTF write-ups repo maintained by SmokeLeetEveryday team.


### LICENSE

MIT :)
