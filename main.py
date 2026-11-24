#!/usr/bin/env python3
"""Entri make.fun: One Word, One Username, One Reward.

Menulis username make.fun akun sendiri ke /output/entry.txt,
satu kata tanpa newline akhir, lalu memverifikasi hasil tulisannya.
"""

import os

USERNAME = "silvlaia"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 30


def tulis(teks, path=OUTPUT_PATH):
    """Tulis teks ke path sebagai UTF-8, tanpa newline akhir."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(teks)
    return path


def validasi(teks):
    """Periksa teks: 1-30 karakter, satu kata tanpa whitespace apa pun.

    Mengembalikan (ok, alasan): ok True bila lolos, alasan berisi
    penjelasan singkat bila gagal.
    """
    if not teks.strip():
        return False, "teks kosong atau hanya whitespace"
    if not (MIN_LEN <= len(teks) <= MAX_LEN):
        return False, "panjang harus 1-30 karakter"
    if teks != teks.strip():
        return False, "ada whitespace di awal atau akhir"
    if any(ch.isspace() for ch in teks):
        return False, "mengandung whitespace di tengah"
    if len(teks.encode("utf-8")) > MAX_LEN:
        return False, "panjang byte UTF-8 melebihi 30"
    return True, "valid"


def verifikasi(path=OUTPUT_PATH, diharapkan=USERNAME):
    """Baca balik berkas dan pastikan isinya persis sama dengan yang diharapkan."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        isi = f.read()
    return isi == diharapkan


def main():
    ok, alasan = validasi(USERNAME)
    if not ok:
        raise SystemExit("Username tidak valid: " + alasan)
    tulis(USERNAME)
    if not verifikasi():
        raise SystemExit("Verifikasi baca-balik gagal.")
    print("Entry ditulis ke", OUTPUT_PATH)
    print("Isi terverifikasi:", repr(USERNAME))
    print("Panjang:", len(USERNAME), "karakter /",
          len(USERNAME.encode("utf-8")), "byte")


if __name__ == "__main__":
    main()
