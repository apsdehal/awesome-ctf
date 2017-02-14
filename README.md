# Awesome CTF [![Build Status](https://travis-ci.org/apsdehal/awesome-ctf.svg?branch=master)](https://travis-ci.org/apsdehal/awesome-ctf) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of [Capture The Flag](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) (CTF) frameworks, libraries, resources, softwares and tutorials. This list aims to help starters as well as seasoned CTF players to find everything related to CTFs at one place.

### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md) first.

#### _If you know a tool that isn't present here, feel free to open a pull request._

### Why?

It takes time to build up collection of tools used in ctf and remember them all. This repo helps to keep all these scattered tools at one place.


### Contents

- [Awesome CTF](#awesome-ctf)
  - [Create](#create)
    - [Forensics](#forensics)
    - [Platforms](#platforms)
    - [Steganography](#steganography)
    - [Web](#web)
  - [Solve](#solve)
    - [Attacks](#attacks)
    - [Bruteforcers](#bruteforcers)
    - [Cryptography](#crypto)
    - [Exploits](#exploits)
    - [Forensics](#forensics-1)
    - [Networking](#networking)
    - [Reversing](#reversing)
    - [Services](#services)
    - [Steganography](#steganography-1)
    - [Web](#web-1)

- [Resources](#resources)
  - [Operating Systems](#operating-systems)
  - [Starter Packs](#starter-packs)
  - [Tutorials](#tutorials)
  - [Wargames](#wargames)
  - [Websites](#websites)
  - [Wikis](#wikis)
  - [Writeups Collections](#writeups-collections)

# Create

*Tools used for creating CTF challenges*

## Forensics

*Tools used for creating Forensics challenges*

- [Dnscat](https://wiki.skullsecurity.org/Dnscat) - Hosts communication through DNS
- [Registry Dumper](http://www.kahusecurity.com/tools/RegistryDumper_v0.1.zip) - Dump your registry

## Platforms

*Projects that can be used to host a CTF*

- [CTFd](https://github.com/isislab/CTFd) - Platform to host jeopardy style CTFs from ISISLab, NYU Tandon
- [FBCTF](https://github.com/facebook/fbctf) - Platform to host Capture the Flag competitions from Facebook
- [Mellivora](https://github.com/Nakiami/mellivora) - A CTF engine written in PHP
- [NightShade](https://github.com/UnrealAkama/NightShade) - A simple security CTF framework
- [Scorebot](https://github.com/legitbs/scorebot) - Platform for CTFs by Legitbs (Defcon)


## Steganography

*Tools used to create stego challenges*

Check solve section for steganography.


## Web

*Tools used for creating Web challenges*

*JavaScript Obfustcators*

- [Metasploit JavaScript Obfustcator](https://github.com/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit)
- [Uglify](http://marijnhaverbeke.nl//uglifyjs)


# Solve

*Tools used for solving CTF challenges*

## Attacks

*Tools used for performing various kinds of attacks*

- [Bettercap](https://github.com/evilsocket/bettercap) - Framework to perform MITM (Man in the Middle) attacks.
- [Layer 2 attacks](https://github.com/tomac/yersinia) - Attack various protocols on layer 2

## Crypto

*Tools used for solving Crypto challenges*

- [FeatherDuster](https://github.com/nccgroup/featherduster) - An automated, modular cryptanalysis tool
- [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) - A tool for Breaking PkZip-encryption
- [RSATool](https://github.com/ius/rsatool) - Generate private key with knowledge of p and q
- [XORTool](https://github.com/hellman/xortool) - A tool to analyze multi-byte xor cipher

## Bruteforcers

*Tools used for various kind of bruteforcing (passwords etc.)*

- [John The Jumbo](https://github.com/magnumripper/JohnTheRipper) - Community enhanced version of John the Ripper
- [John The Ripper](http://www.openwall.com/john/) - Password Cracker
- [Ophcrack](http://ophcrack.sourceforge.net/) - Windows password cracker based on rainbow tables.

## Exploits

*Tools used for solving Exploits challenges*

- [DLLInjector](https://github.com/OpenSecurityResearch/dllinjector) - Inject dlls in processes
- [Metasploit](http://www.metasploit.com/) - Penetration testing software
- [Pwntools](https://github.com/Gallopsled/pwntools) - CTF Framework for writing exploits
- [Qira](https://github.com/BinaryAnalysisPlatform/qira) - QEMU Interactive Runtime Analyser
- [ROP Gadget](https://github.com/JonathanSalwan/ROPgadget) - Framework for ROP exploitation
- [V0lt](https://github.com/P1kachu/v0lt) - Security CTF Toolkit

## Forensics

*Tools used for solving Forensics challenges*

- [Aircrack-Ng](http://www.aircrack-ng.org/) - Crack 802.11 WEP and WPA-PSK keys
  - `apt-get install aircrack-ng`
- [Audacity](http://sourceforge.net/projects/audacity/) - Analyze sound files (mp3, m4a, whatever)
  - `apt-get install audacity`
- [Bkhive and Samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/) - Dump SYSTEM and SAM files
  - `apt-get install samdump2 bkhive`
- [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE Editor
- [Creddump](https://github.com/moyix/creddump) - Dump windows credentials
- [DVCS Ripper](https://github.com/kost/dvcs-ripper) - Rips web accessible (distributed) version control systems
- [Exif Tool](http://www.sno.phy.queensu.ca/~phil/exiftool/) - Read, write and edit file metadata
- [Extundelete](http://extundelete.sourceforge.net/) - Used for recovering lost data from mountable images
- [Fibratus](https://github.com/rabbitstack/fibratus) - Tool for exploration and tracing of the Windows kernel
- [Foremost](http://foremost.sourceforge.net/) - Extract particular kind of files using headers
  - `apt-get install foremost`
- [Fsck.ext4](http://linux.die.net/man/8/fsck.ext3) - Used to fix corrupt filesystems
- [Malzilla](http://malzilla.sourceforge.net/) - Malware hunting tool
- [NetworkMiner](http://www.netresec.com/?page=NetworkMiner) - Network Forensic Analysis Tool
- [PDF Streams Inflater](http://malzilla.sourceforge.net/downloads.html) - Find and extract zlib files compressed in PDF files
- [ResourcesExtract](http://www.nirsoft.net/utils/resources_extract.html) - Extract various filetypes from exes
- [Shellbags](https://github.com/williballenthin/shellbags) - Investigate NT\_USER.dat files
- [UsbForensics](http://www.forensicswiki.org/wiki/USB_History_Viewing) - Contains many tools for usb forensics
- [Volatility](https://github.com/volatilityfoundation/volatility) - To investigate memory dumps


*Registry Viewers*
- [RegistryViewer](http://www.gaijin.at/en/getitpage.php?id=regview) - Used to view windows registries
- [Windows Registry Viewers](http://www.forensicswiki.org/wiki/Windows_Registry) - More registry viewers


## Networking

*Tools used for solving Networking challenges*

- [Masscan](https://github.com/robertdavidgraham/masscan) - Mass IP port scanner, TCP port scanner
- [Nipe](https://github.com/GouveaHeitor/nipe) - Nipe is a script to make Tor Network your default gateway.
- [Nmap](https://nmap.org/) - open source utility for network discovery and security auditing
- [Wireshark](https://www.wireshark.org/) - Analyze the network dumps
  - `apt-get install wireshark`
- [Zmap](https://zmap.io/) - an open-source network scanner

## Reversing

*Tools used for solving Reversing challenges*

- [Androguard](https://github.com/androguard/androguard) - Reverse engineer Android applications
- [Angr](https://github.com/angr/angr) - platform-agnostic binary analysis framework
- [Apk2Gold](https://github.com/lxdvs/apk2gold) - Yet another Android decompiler
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - Android Decompiler
- [Barf](https://github.com/programa-stic/barf-project) - Binary Analysis and Reverse engineering Framework
- [Binary Ninja](https://binary.ninja/) - Binary analysis framework
- [BinUtils](http://www.gnu.org/software/binutils/binutils.html) - Collection of binary tools
- [BinWalk](https://github.com/devttys0/binwalk) - Analyze, reverse engineer, and extract firmware images.
- [Boomerang](https://github.com/nemerle/boomerang) - Decompile x86 binaries to C
- [ctf_import](https://github.com/docileninja/ctf_import) – run basic functions from stripped binaries cross platform
- [GDB](https://www.gnu.org/software/gdb/) - The GNU project debugger
- [GEF](https://github.com/hugsy/gef) - GDB plugin
- [Hopper](http://www.hopperapp.com/) - Reverse engineering tool (disassembler) for OSX and Linux
- [IDA Pro](https://www.hex-rays.com/products/ida/) - Most used Reversing software
- [Jadx](https://github.com/skylot/jadx) - Decompile Android files
- [Java Decompilers](http://www.javadecompilers.com) - An online decompiler for Java and Android APKs
- [Krakatau](https://github.com/Storyyeller/Krakatau) - Java decompiler and disassembler
- [PEDA](https://github.com/longld/peda) - GDB plugin (only python2.7)
- [Plasma](https://github.com/joelpx/plasma) - An interactive disassembler for x86/ARM/MIPS which can generate indented pseudo-code with colored syntax.
- [Pwndbg](https://github.com/pwndbg/pwndbg) - A GDB plugin that provides a suite of utilities to hack around GDB easily. 
- [radare2](https://github.com/radare/radare2) - A portable reversing framework
- [Uncompyle](https://github.com/gstarnberger/uncompyle) - Decompile Python 2.7 binaries (.pyc)
- [WinDbg](http://www.windbg.org/) - Windows debugger distributed by Microsoft
- [Z3](https://github.com/Z3Prover/z3) - a theorem prover from Microsoft Research

*JavaScript Deobfustcators*

- [Detox](http://relentless-coding.org/projects/jsdetox/install) - A Javascript malware analysis tool
- [Revelo](http://www.kahusecurity.com/tools/Revelo_v0.6.zip) - Analyze obfuscated Javascript code

*SWF Analyzers*
- [RABCDAsm](https://github.com/CyberShadow/RABCDAsm) - Collection of utilities including an ActionScript 3 assembler/disassembler.
- [Swftools](http://www.swftools.org/) - Collection of utilities to work with SWF files
- [Xxxswf](https://bitbucket.org/Alexander_Hanel/xxxswf) -  A Python script for analyzing Flash files.

## Services

*Various kind of useful services available around the internet*

- [CSWSH](http://ironwasp.org/cswsh.html) - Cross-Site WebSocket Hijacking Tester
- [Request Bin](http://requestb.in/) - Lets you inspect http requests to a particular url

## Steganography

*Tools used for solving Steganography challenges*

- [Convert](http://www.imagemagick.org/script/convert.php) - Convert images b/w formats and apply filters
- [Exif](http://manpages.ubuntu.com/manpages/trusty/man1/exif.1.html) - Shows EXIF information in JPEG files
- [Exiftool](https://linux.die.net/man/1/exiftool) - Read and write meta information in files
- [Exiv2](http://www.exiv2.org/manpage.html) - Image metadata manipulation tool
- [ImageMagick](http://www.imagemagick.org/script/index.php) - Tool for manipulating images
- [Outguess](https://www.freebsd.org/cgi/man.cgi?query=outguess+&apropos=0&sektion=0&manpath=FreeBSD+Ports+5.1-RELEASE&format=html) - Universal steganographic tool
- [Pngtools](http://www.stillhq.com/pngtools/) - For various analysis related to PNGs
  - `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) - Used to deblur and fix defocused images
- [Steganabara](https://www.openhub.net/p/steganabara) -  Tool for stegano analysis written in Java
- [Stegbreak](https://linux.die.net/man/1/stegbreak) - Launches brute-force dictionary attacks on JPG image
- [Steghide](http://steghide.sourceforge.net/) - Hide data in various kind of images
- [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - Apply various steganography techniques to images

## Web

*Tools used for solving Web challenges*
- [Commix](https://github.com/commixproject/commix) - Automated All-in-One OS Command Injection and Exploitation Tool.
- [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbar/) - Firefox addon for easy web exploitation
- [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) - Add on for chrome for debugging network requests
- [SQLMap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection and database takeover tooli
- [W3af](https://github.com/andresriancho/w3af) -  Web Application Attack and Audit Framework.
- [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor


# Resources

*Where to discover about CTF*

## Operating Systems

*Penetration testing and security lab Operating Systems*

- [BackBox](https://backbox.org/) - Based on Ubuntu
- [BlackArch Linux](https://blackarch.org/) - Based on Arch Linux
- [Fedora Security Lab](https://labs.fedoraproject.org/security/) - Based on Fedora
- [Kali Linux](https://www.kali.org/) - Based on Debian
- [Parrot Security OS](https://www.parrotsec.org/) - Based on Debian
- [Pentoo](http://www.pentoo.ch/) - Based on Gentoo
- [URIX OS](http://urix.us/) - Based on openSUSE
- [Wifislax](http://www.wifislax.com/) - Based on Slackware

*Malware analysts and reverse-engineering*

- [REMnux](https://remnux.org/) - Based on Debian

## Starter Packs

*Collections of installer scripts, useful tools*

- [CTF Tools](https://github.com/zardus/ctf-tools) - Collection of setup scripts to install various security research tools.
- [LazyKali](https://github.com/jlevitsk/lazykali) - A 2016 refresh of LazyKali which simplifies install of tools and configuration.

## Tutorials

*Tutorials to learn how to play CTFs*

- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Field Guide by Trails of Bits
- [CTF Resources](http://ctfs.github.io/resources/) -  Start Guide maintained by community
- [Damn Vulnerable Web Application](http://www.dvwa.co.uk/) PHP/MySQL web application that is damn vulnerable
- [How to Get Started in CTF](https://www.endgame.com/blog/how-get-started-ctf) - Short guideline for CTF beginners by Endgame
- [MIPT CTF](https://github.com/xairy/mipt-ctf) - A small course for beginners in CTFs (in Russian)

## Wargames

*Always online CTFs*

- [Backdoor](https://backdoor.sdslabs.co/) - Security Platform by SDSLabs.
- [Ctfs.me](http://ctfs.me) - CTF All the time
- [Exploit Exercises](https://exploit-exercises.com/) - Variety of VMs to learn variety of computer security issues.
- [Gracker](http://gracker.org) - Binary challenges having a slow learning curve, and write-ups for each level.
- [Hack This Site](https://www.hackthissite.org/) - Training ground for hackers.
- [IO](http://io.netgarage.org/) - Wargame for binary challenges.
- [Over The Wire](http://overthewire.org/wargames/) - Wargame maintained by OvertheWire Community
- [PicoCTF](https://picoctf.com/) - While picoCTF 2014 is now over, you may still play through the competition.
- [Pwnable.kr](https://pwnable.kr/) - Pwn Game
- [Ringzer0Team](https://ringzer0team.com/) - Ringzer0 Team Online CTF
- [SmashTheStack](http://smashthestack.org/) - A variety of wargames maintained by the SmashTheStack Community.
- [VulnHub](https://www.vulnhub.com/) - VM-based for practical in digital security, computer application & network administration.
- [WebHacking](http://webhacking.kr) - Hacking challenges for web.
- [WeChall](https://www.wechall.net/) - Always online challenge site.

*Self-hosted CTFs*

- [Juice Shop CTF](https://github.com/bkimminich/juice-shop-ctf) - Scripts and tools for hosting a CTF on [OWASP Juice Shop](https://www.owasp.org/index.php/OWASP_Juice_Shop_Project) easily.

## Websites

*Various general websites about and on ctf*

- [CTF Time](https://ctftime.org/) - General information on CTF occuring around the worlds
- [Reddit Security CTF](http://www.reddit.com/r/securityctf) - Reddit CTF category

## Wikis

*Various Wikis available for learning about CTFs*

- [Bamboofox](https://bamboofox.torchpad.com/) - Chinese resources to learn CTF
- [ISIS Lab](https://github.com/isislab/Project-Ideas/wiki) - CTF Wiki by Isis lab
- [OpenToAll](http://wiki.opentoallctf.com/) - Open To All Knowledge Base

## Writeups Collections

*Collections of CTF write-ups*

- [Captf](http://captf.com/) - Dumped CTF challenges and materials by psifertex
- [CTF write-ups (community)](https://github.com/ctfs/) - CTF challenges + write-ups archive maintained by the community
- [pwntools writeups](https://github.com/Gallopsled/pwntools-write-ups) - A collection of CTF write-ups all using pwntools
- [Shell Storm](shell-storm.org/repo/CTF/) - CTF challenge archive maintained by Jonathan Salwan
- [Smoke Leet Everyday](https://github.com/smokeleeteveryday/CTF_WRITEUPS) - CTF write-ups repo maintained by SmokeLeetEveryday team.


### LICENSE

CC0 :)
