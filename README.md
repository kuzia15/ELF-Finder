# ᐳ ELF-Finder - Universal ELF Function Finder

# ᐳ Description  
> * Language: `Python 3`  
> * Purpose: `Search functions by offset or name in ELF shared libs (.so)`  
> * Dependencies: `lief`  
> * Status: `Stable, tested on multiple ELF libraries`  

# ᐳ Features
> * Search functions by **offset** or **mangled/unmangled name**
> * Supports exact and partial function name matching
> * Cross-library comparison of function offsets
> * Works with ARM/Thumb addresses (normalization)

# ᐳ Usage
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

# ᐳ Example

<img width="577" height="93" alt="image" src="https://github.com/user-attachments/assets/66f1900c-326b-4286-816e-1c8e8217bcc9" />
<img width="577" height="93" alt="image" src="https://github.com/user-attachments/assets/58409311-01a3-486f-8e19-402a722eb4a1" />


# ᐳ Credit's
kuzia15 — author, maintainer, code & ideas

![license](https://imgur.com/QQlcEVT.png)
