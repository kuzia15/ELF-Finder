"""
ELF Function Finder

This script parses ELF shared libraries (.so) and allows searching for functions
either by offset (address) or by function name. It compares the found function
across multiple libraries (e.g., different versions or architectures).
"""

import lief
import sys
from pathlib import Path


def normalize_address(addr: int) -> int:
    return addr & ~1


def find_function_by_offset(elf: lief.ELF.Binary, offset: int):
    offset = normalize_address(offset)
    closest = (None, None)
    min_diff = sys.maxsize

    for sym in elf.symbols:
        if sym.value == 0 or sym.size == 0:
            continue

        addr = normalize_address(sym.value)
        if addr <= offset < addr + sym.size:
            return sym.name, addr

        diff = offset - addr
        if 0 <= diff < min_diff:
            min_diff = diff
            closest = (sym.name, addr)

    return closest


def find_function_by_name(elf: lief.ELF.Binary, query_name: str):
    # exact match
    for sym in elf.symbols:
        if query_name == sym.name:
            return sym.name, normalize_address(sym.value)
    for sym in elf.symbols:
        if query_name in sym.name:
            return sym.name, normalize_address(sym.value)

    return None, None


def process_library(lib_path: str, func_name: str = None, target_offset: int = None):
    lib_path = Path(lib_path)
    if not lib_path.exists():
        print(f"[DEBUG] [!] Library not found: {lib_path}")
        return

    print(f"[DEBUG] Processing library: {lib_path.name}")
    try:
        elf = lief.parse(str(lib_path))
    except Exception as e:
        print(f"[DEBUG] [!] Failed to parse ELF: {e}")
        return

    if func_name:
        name, addr = find_function_by_name(elf, func_name)
    else:
        name, addr = find_function_by_offset(elf, target_offset)

    if name:
        print(f"[+] {lib_path.name}: Function '{name}' found at 0x{addr:08X}")
    else:
        print(f"[-] {lib_path.name}: Function not found")


def main():
    main_lib_path = input("Enter path to main library (.so): ").strip()
    other_libs_input = input("Enter paths to other libraries (comma-separated): ").strip()
    other_libs = [p.strip() for p in other_libs_input.split(",") if p.strip()]
    query = input("Enter offset (0x...) or function name: ").strip()

    try:
        main_lib = lief.parse(main_lib_path)
    except Exception as e:
        print(f"[DEBUG] [!] Failed to parse main library: {e}")
        return

    if query.startswith("0x"):
        offset = int(query, 16)
        func_name, func_addr = find_function_by_offset(main_lib, offset)
    else:
        func_name, func_addr = find_function_by_name(main_lib, query)

    if func_name:
        print(f"[+] Main library: Function '{func_name}' starts at 0x{func_addr:08X}")
        for lib in other_libs:
            process_library(lib, func_name=func_name)
    else:
        print("[-] Function not found in the main library.")


if __name__ == "__main__":
    main()