import google.generativeai as genai
import os

# Mengambil API Key dari environment variable GitHub
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY tidak ditemukan di Secrets GitHub!")
    exit(1)

genai.configure(api_key=api_key)

print("=== DAFTAR MODEL GEMINI TERSEDIA ===")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"ID: {m.name}")
            print(f"Display: {m.display_name}")
            print("-" * 30)
except Exception as e:
    print(f"Gagal akses API: {e}")
