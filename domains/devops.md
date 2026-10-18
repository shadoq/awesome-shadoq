# Self-hosting, servers and monitoring

[Back to the index](../README.md)

## In short

For a small team, operations means owning as little infrastructure as possible while still owning your data.

- **Self-hosting starts with the list:** awesome-selfhosted catalogues hundreds of services. The self-hosted AI starter kit bundles n8n, Ollama, Qdrant and Postgres in one Docker Compose file.
- **Hosting:** Vercel for front ends, a VPS (Akamai/Linode) when you need control, PythonAnywhere for a quick Python app.
- **Monitoring:** Zabbix is the long-lived open-source standard for servers and networks.
- **Networking:** MikroTik's official docs are the reference for VPN tunnels and RouterOS.
- **Security tooling:** CyberChef decodes almost anything; Exploit-DB and Parrot Security for research; Zaufana Trzecia Strona for Polish security news.
- **Handy tricks:** WebVM runs Linux in the browser; dockur/macos runs macOS in a container for testing.

**Where to start:** awesome-selfhosted, then Docker Compose for everything you run.

## Contents

- [Linux and networking](#linux-and-networking)
- [Self-hosting](#self-hosting)
- [Cloud and hosting](#cloud-and-hosting)
- [Security](#security)
- [Monitoring](#monitoring)

## Linux and networking

- [MikroTik IPsec docs](https://help.mikrotik.com/docs/display/ROS/IPsec) - Official MikroTik RouterOS documentation on configuring IPsec VPN tunnels.
- [WebVM](https://github.com/leaningtech/webvm) - x86 Linux virtual machine running in the browser via WebAssembly.
- [Android-x86](http://www.android-x86.org/) - Open-source project porting Android to x86 PCs and devices.
- [DroidDesk](https://github.com/orailnoor/DroidDesk) - Turns an Android phone into a Linux desktop using Termux, Termux X11 and proot.
- [MikroTik RouterOS WebFig manual](https://wiki.mikrotik.com/Manual:Webfig) - RouterOS manual page on the WebFig web management interface.
- [OpenVPN on MikroTik CHR](https://nsix.pl/kb/serwer-openvpn-na-mikrotik-chr) - Knowledge base guide to setting up an OpenVPN server on a MikroTik CHR router.
- [Server World](https://www.server-world.info/en/) - Step-by-step Linux server configuration notes, including Ubuntu 22.04 installation media.
- [Ultra Monkey](http://www.ultramonkey.org/) - Linux load balancing and high-availability project based on LVS.

## Self-hosting

- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) ⭐ - Curated list of free software network services and web apps that can be self-hosted.
- [dockur/macos](https://github.com/dockur/macos) - macOS running inside a Docker container.
- [self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) - Docker Compose template running n8n, Ollama, Qdrant and Postgres together for local AI.
- [Docs (suitenumerique)](https://github.com/suitenumerique/docs) - Open-source collaborative note-taking, wiki and documentation platform with real-time editing.
- [noobs](https://github.com/unkn0w/noobs) - Collection of scripts for quickly setting up services on Mikrus servers (Polish VPS hosting).
- [Olares](https://github.com/beclab/Olares) - Open-source personal cloud OS for self-hosting apps and running always-on agents.
- [Puter](https://github.com/HeyPuter/puter) - Open-source, self-hostable web desktop that runs in the browser.

## Cloud and hosting

- [Akamai Cloud (Linode)](https://www.linode.com/) - Cloud computing and VPS hosting with edge services.
- [Vercel](https://vercel.com/home) - Frontend cloud platform for deploying web apps and AI agents.
- [floci](https://github.com/floci-io/floci) - Lightweight local AWS emulator, an alternative for development and testing.
- [Hyperbolic](https://hyperbolic.xyz/) - AI cloud offering on-demand H100, H200 and B200 GPUs and multi-node clusters for training.
- [Miget](https://miget.com/) - Platform as a service with one fixed compute plan for apps, databases and workers.
- [PythonAnywhere](https://www.pythonanywhere.com/) - Browser-based hosting and coding environment for Python web apps.

## Security

- [CyberChef](https://gchq.github.io/CyberChef) ⭐ - Browser-based tool for encoding, decoding and analyzing data, from GCHQ.
- [Exploit-DB](https://www.exploit-db.com/) - Archive of public exploits and security research for penetration testers.
- [Parrot Security](https://parrotsec.org/) - Linux distribution for security testing, penetration testing and privacy.
- [Triage](https://tria.ge/) - Malware analysis sandbox for triaging suspicious files and URLs.
- [Zaufana Trzecia Strona](http://zaufanatrzeciastrona.pl/) - Polish independent news site on IT security.

## Monitoring

- [Zabbix](https://www.zabbix.com/) - Open-source enterprise monitoring solution for networks and applications.
- [Apache DevLake](https://devlake.apache.org/) - Open-source platform that collects DevOps tool data to measure engineering productivity.
- [gpuFire](https://github.com/Nondzu/gpuFire) - Terminal monitor for NVIDIA GPUs with GDDR6 memory temperature readout.
