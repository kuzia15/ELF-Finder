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
>    pip install lief  
>    ```  
> 3. Run the script:  
>    ```bash  
>    python elf_finder.py  
>    ```  
> 4. Follow interactive prompts:  
>    - Enter path to main `.so` library  
>    - Enter paths to other `.so` libraries (comma separated) for comparison  
>    - Enter function offset (hex, e.g. `0x00541D34`) or function name  

# ᐳ Example



# ᐳ Credit's
kuzia15 — author, maintainer, code & ideas