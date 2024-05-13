def konversi_suhu(suhu, satuan):
    if satuan == "C":
        reamur = suhu * 4 / 5
        fahrenheit = (suhu * 9 / 5) + 32
        kelvin = suhu + 273.15
        return (reamur, fahrenheit, kelvin)
    elif satuan == "R":
        celcius = suhu * 5 / 4
        fahrenheit = (celcius * 9 / 5) + 32
        kelvin = celcius + 273.15
        return (celcius, fahrenheit, kelvin)
    elif satuan == "F":
        celcius = (suhu - 32) * 5 / 9
        reamur = celcius * 4 / 5
        kelvin = celcius + 273.15
        return (celcius, reamur, kelvin)
    elif satuan == "K":
        celcius = suhu - 273.15
        reamur = celcius * 4 / 5
        fahrenheit = (celcius * 9 / 5) + 32
        return (celcius, reamur, fahrenheit)
    else:
        return "Suhu yang Anda inputkan tidak sesuai"


def main():
    suhu = float(input("Masukkan suhu dalam derajat: "))
    satuan = input("Masukkan satuan suhu (C/F/R/K): ").upper()
    hasil_konversi = konversi_suhu(suhu, satuan)
    if type(hasil_konversi) == tuple:
        print(f"Suhu {suhu} derajat {satuan} dapat dikonversi menjadi:")
        print("=====================================")
        print(f"Celcius      | {hasil_konversi[0]} °C")
        print(f"Reaumur      | {hasil_konversi[1]} °R")
        print(f"Fahrenheit   | {hasil_konversi[2]} °F")
    else:
        print(hasil_konversi)

if __name__ == "__main__":
    main()
