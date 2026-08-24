# 🚀 Prompt-to-Binary Engine V4 (Self-Healing AI)
<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)
![TCC](https://img.shields.io/badge/Compiler-Tiny_C_Compiler-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**No Cloud. No API Costs. Just Pure Offline Automation.**

</div>
An advanced, offline AI automation tool that converts natural language English prompts directly into fully functional, compiled C executables (`.exe`). 

Powered by local LLMs (Ollama) and featuring a **Multi-Agent Auto-Fixing Loop**, this engine doesn't just write code—it self-corrects its own compiler errors.

## ✨ Core Features
* **100% Offline Execution:** Runs completely locally without needing expensive Cloud API keys.
* **Auto-Fixing Engine (V4):** If the generated C code fails to compile, the engine captures the `stderr` from the compiler, feeds it back to the AI, and forces it to fix the bug (up to 3 retries).
* **Magic Cleaner:** Automatically strips markdown formatting and extracts raw C code.
* **Direct to Binary:** Bypasses intermediate steps and delivers a ready-to-use `.exe` file.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **AI Model:** `qwen2.5-coder:1.5b` (via Ollama)
* **Compiler:** Tiny C Compiler (TCC)

## ⚙️ How to Use
1. Install [Ollama](https://ollama.com/) and pull the model: `ollama run qwen2.5-coder:1.5b`
2. Install Tiny C Compiler (TCC) and add it to your PATH.
3. Run the engine:
   ```bash
   python magic.py