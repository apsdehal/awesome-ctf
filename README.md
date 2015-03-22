#CTF Tools

Since I lost my laptop a month back, with that I lost all the collection of my important CTF solving softwares and tools. It takes time to build up the collection. So I am adding them all here, just in case.

_If you know a tool that isn't present here, feel free to open a pull request._

In case of tools/repos with huge code, I will add tool title and description to readme only.

# Requirements

- java
- python

## List

- Stegano
  - Stegsolve
  - Steganabara
  - [Steghide](http://steghide.sourceforge.net/)
  - pngtools - For various analysis related to PNGs
    - `apt-get install pngtools`
  - [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) Used to deblur and fix defocused images

- Crypto
  - XORTool

- Forensics
  - [Volatility](https://github.com/volatilityfoundation/volatility) - To investigate memory dumps
  - [Shellbags](https://github.com/williballenthin/shellbags) - Investigate NT\_USER.dat files
  - Foremost - Extract particular kind of files using headers
    - `apt-get install foremost
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

- Bruteforcers
  - John The Ripper
  - John The Jumbo
  - Ophcrack

- Reversing
  - [Krakatau](https://github.com/Storyyeller/Krakatau) - Java decompiler and disassembler
  - IDA Pro - Ultimate solution to reversing needs
  - [Uncompyle](https://github.com/williballenthin/shellbags) - Decompile Python 2.7 binaries (.pyc)
  - JavaScript Deobfustcators
	- [Detox](http://relentless-coding.org/projects/jsdetox/install)
	- [Malzilla](http://malzilla.sourceforge.net/downloads.html)
	- [Revelo](http://www.kahusecurity.com/tools/Revelo_v0.6.zip)
	- Further you can put a breakpoint before return statement in debuggers to find the final code to be executed

- Web
  - [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor
### Tools used for creation

- JavaScript Obfustcators
	- Metasploit JavaScript Obfustcator
	- Uglify

- [Registry Dumper](http://www.kahusecurity.com/tools/RegistryDumper_v0.1.zip) - Dump your registry
