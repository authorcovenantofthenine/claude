"""Turn a tuning name into the ID The Sims 4 expects (FNV-64 of the lowercase name, high bit set).

Usage:  python hash_name.py "YourName_FirstMod_XmlInjectorSnippet"
Prints the decimal ID (for s="...") and the hex instance (for your package tool).
Checked against XML Injector's docs: "Scumbumbo_XmlInjector_AddInteractionTest" -> 13197251937291617972.
"""
import sys

def fnv64(name: str) -> int:
    h = 0xCBF29CE484222325
    for b in name.lower().encode("utf-8"):
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
        h ^= b
    return h | (1 << 63)

if __name__ == "__main__":
    for n in sys.argv[1:] or ["Scumbumbo_XmlInjector_AddInteractionTest"]:
        v = fnv64(n)
        print(f"{n}\n  s=\"{v}\"\n  Instance: 0x{v:016X}")
