# ᐳ ELF-Finder - Universal ELF Function Finder

## ᐳ Description  
> * Language: `Python 3`  
> * Purpose: `Parse and analyze ELF shared libraries (.so) of various architectures to search for functions by offset or name, enabling comparison of symbols across multiple ELF binaries.`  
> * Dependencies: `lief`  
> * Status: `Stable, tested on multiple ELF libraries`  

## ᐳ Features  
> * Search functions by **offset** or **mangled/unmangled name**  
> * Supports exact and partial function name matching  
> * Cross-library comparison of function offsets  
> * Works with ARM/Thumb addresses (normalization)  

## ᐳ Supported Architectures  
> This tool works with ELF shared libraries of various architectures, including but not limited to:  
> - ARM (armeabi-v7a, arm64-v8a)  
> - x86 and x86_64  
> - MIPS  
> - Other ELF-compatible architectures  

> The tool relies on the presence of symbol tables within the ELF files.

## ᐳ Known Limitations  
> * Requires ELF binaries to contain symbol tables (not stripped).  
> * Function offset accuracy may vary depending on the compiler, linking, and architecture specifics.  
> * Partial name matching may produce multiple matches; user discretion advised.  
> * Currently focuses on shared libraries (.so) and may not fully support executable ELF files or static libraries.  

## ᐳ Usage  
> 1. Clone or download the repo  
> 2. Install dependencies:  
>    ```bash  
>    pip install -r requirements.txt  
>    ```  
> 3. Run the script:  
>    ```bash  
>    python main.py  
>    ```  
> 4. Follow interactive prompts:  
>    - Enter path to main `.so` library  
>    - Enter paths to other `.so` libraries (comma separated) for comparison  
>    - Enter function offset (hex, e.g. `0x00541D34`) or function name  

## ᐳ Example  

<img width="577" height="93" alt="image" src="https://github.com/user-attachments/assets/66f1900c-326b-4286-816e-1c8e8217bcc9" />
<img width="577" height="93" alt="image" src="https://github.com/user-attachments/assets/58409311-01a3-486f-8e19-402a722eb4a1" />

## ᐳ Credits  
kuzia15 — author, maintainer, code & ideas  

![license](https://imgur.com/QQlcEVT.png)  
