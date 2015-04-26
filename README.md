# CTF Tools

A curated list of awesome CTF frameworks, libraries, resources and softwares.

### Contributing

Please take a quick gander at the [contribution guidelines](https://github.com/apsdehal/ctf-tools/CONTRIBUTING.md) first.

#### _If you know a tool that isn't present here, feel free to open a pull request._

### Contents

- [CTF Tools](#ctf-tools)
  - [Create](#create)
    - [Web](#create-web)
    - [Forensics](#create-forensics)
  - [Solve](#solve)
    - [Attacks](#solve-attacks)
    - [Bruteforcers](#solve-bruteforcers)
    - [Creation Tools](#solve-create)
    - [Cryptography](#solve-crypto)
    - [Exploits](#solve-exploits)
    - [Forensics](#solve-forensics)
    - [Miscellaneous](#solve-misc)
    - [Reversing](#solve-reversing)
    - [Services](#solve-services)
    - [Steganography](#solve-stegano)
    - [Web](#solve-web)

- [Resources](#resources)
  - [Websites](#resources-websites)
    - [Tutorials](#resources-tutorials)


# Create

*Tools used for creating CTF challenges*

## Forensics

*Tools used for creating Forensics challenges*

- [Registry Dumper](http://www.kahusecurity.com/tools/RegistryDumper_v0.1.zip) - Dump your registry

## Web

*Tools used for creating Web challenges*

*JavaScript Obfustcators*

- Metasploit JavaScript Obfustcator
- Uglify


# Solve

*Tools used for solving CTF challenges*

## Stegano

*Tools used for solving Steganography challenges*

- Stegsolve
- Steganabara
- [Steghide](http://steghide.sourceforge.net/)
- pngtools - For various analysis related to PNGs
  - `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) Used to deblur and fix defocused images

## Crypto

*Tools used for solving Crypto challenges*

- XORTool
- [RSATool](https://github.com/ius/rsatool) - Generate private key with knowledge of p and q

## Forensics

*Tools used for solving Forensics challenges*

- [Volatility](https://github.com/volatilityfoundation/volatility) - To investigate memory dumps
- [Shellbags](https://github.com/williballenthin/shellbags) - Investigate NT\_USER.dat files
- Foremost - Extract particular kind of files using headers
  - `apt-get install foremost`
- Wireshark - Analyze the network dumps
  - `apt-get install wireshark`
- Audacity - Analyze sound files (mp3, m4a, whatever)
  - `apt-get install audacity`
- extundelete - Used for recovering lost data from mountable images
- fsck.ext4 - Used to fix corrupt filesystems
- [RegistryViewer](http://www.gaijin.at/en/getitpage.php?id=regview) - Used to view windows registries
  - [More registry viewers](http://www.forensicswiki.org/wiki/Windows_Registry)
- bkhive and samdump2 - Dump SYSTEM and SAM files
- [creddump](https://code.google.com/p/creddump/) - Dump windows credentials
- [UsbForensics](http://www.forensicswiki.org/wiki/USB_History_Viewing) - Contains many tools for usb forensics
- [ResourcesExtract] - Extract various filetypes from exes
- [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE Editor

## Bruteforcers

*Tools used for various kind of bruteforcing (passwords etc.)*

- John The Ripper
- John The Jumbo
- Ophcrack

## Reversing

*Tools used for solving Reversing challenges*

- [Krakatau](https://github.com/Storyyeller/Krakatau) - Java decompiler and disassembler
- IDA Pro - Ultimate solution to reversing needs
- [Uncompyle](https://github.com/williballenthin/shellbags) - Decompile Python 2.7 binaries (.pyc)
- JavaScript Deobfustcators
- [Detox](http://relentless-coding.org/projects/jsdetox/install)
- [Malzilla](http://malzilla.sourceforge.net/downloads.html)
- [Revelo](http://www.kahusecurity.com/tools/Revelo_v0.6.zip)
- Further you can put a breakpoint before return statement in debuggers to find the final code to be executed

- [BinWalk](https://github.com/devttys0/binwalk) - Analyze, reverse engineer, and extract firmware images.
- [Jadx](https://github.com/skylot/jadx) - Decompile Android files
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - Android Decompiler
- [apk2Gold](https://github.com/lxdvs/apk2gold) - Yet another Android decompiler
- [Boomerang](https://github.com/nemerle/boomerang) - Decompile x86 binaries to C


## Web

*Tools used for solving Web challenges*

- [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor
- [SQLMap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection and database takeover tooli

## Exploits

*Tools used for solving Exploits challenges*

- [Metasploit](http://www.metasploit.com/) - Most used penetration testing software
- [pwntools](https://github.com/Gallopsled/pwntools) - CTF Framework for writing exploits


## Attacks

*Tools used for performing various kinds of attacks*

- [Layer 2 attacks](https://github.com/tomac/yersinia) - Attack various protocols on layer 2

## Services

*Various kind of useful services available around the internet*

- [Request Bin](http://requestb.in/) - Lets you inspect http requests to a particular url
- [CSWSH](http://ironwasp.org/cswsh.html) - Cross-Site WebSocket Hijacking Tester


# Resources

## Websites

*Various learning resources available on internet*

## Tutorials

