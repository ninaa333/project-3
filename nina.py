def ke_fahrenheit(c): return (c * 9/5) + 32
print("30C ke F:", ke_fahrenheit(30))

def ke_fahrenheit(c): return (c * 9/5) + 32
def ke_reamur(c): return c * 4/5
print("30C ke R:", ke_reamur(30))

def ke_fahrenheit(c): return (c * 9/5) + 32
def ke_reamur(c): return c * 4/5
def ke_kelvin(c): return c + 273.15
print("30C ke K:", ke_kelvin(30))

def semua(c):
    print(f"F: {(c * 9/5) + 32}, R: {c * 4/5}, K: {c + 273.15}")
semua(30)

try:
    c = float(input("Masukkan suhu Celsius: "))
    print(f"F: {(c * 9/5) + 32}, R: {c * 4/5}, K: {c + 273.15}")
except:
    print("Gunakan angka!")