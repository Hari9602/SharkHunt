# 🦈 SharkHunt – Forensics CTF Challenge

Welcome to **SharkHunt** – a CTF challenge designed for those who enjoy diving deep into packets using **Wireshark**! 🌊

Your mission is to inspect the network capture file and extract a **hidden hex-encoded flag** from noisy network traffic. Ready to hunt? 🎯

---

## 📁 Challenge Files

`forensic_ctf_complex.pcap` 

🎯 The PCAP file containing the hidden flag ├── generate_complex_pcap.py 

🛠️ Script used to generate the PCAP (educational use) └── README.md # 📘 You're here!


---

## 🎯 Challenge Objective

🔍 Analyze the provided `forensic_ctf_complex.pcap` file using **Wireshark** and recover the hidden flag.

The flag is encoded in **hex** and split across multiple **ICMP echo packets**.  
But beware – there's **plenty of noise** like DNS, TCP, and ARP traffic to throw you off. 😏

---

## 🧠 Difficulty

🟡 **Medium**  

- Wireshark filtering & payload analysis
- ICMP protocols
- Hex-to-ASCII decoding
- Spotting patterns in noisy captures

---

## 🧪 How to Solve

- Open `forensic_ctf_complex.pcap` in **Wireshark** 🦈
- Filter the capture to only view ICMP traffic: `icmp`
- Explore the **Echo (ping)** packets – some of them have a payload 👀
- Follow the trail of ASCII strings encoded in **hex format** 📦
- Reconstruct the full hex string and decode it to reveal the flag 🧩
- Format: `flag{***_***_*_****_*********_**_*********}`


---

## 🛠️ Recreate the Challenge (Optional)

If you're curious how this challenge was created, run the script:


`python3 generate_complex_pcap.py`

This will generate a new forensic_ctf_complex.pcap file with:
- Simulated traffic (ARP, DNS, HTTP, TCP, ICMP)
- Flag data split across ICMP packets
- IP source/destination: 192.168.216.128 

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. ⚖️

Happy Hacking! 🚀

