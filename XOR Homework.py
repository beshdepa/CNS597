import base64
import re

ciphertext = "MQQECVsADQAcOlMaVBUcHCoFAzpfVRoEBl0NAg4QWwMNCk4rG0kXAAIff08bOhYbQx8aCQcCEkZSfiMXATJUHRwEBwF/EwAoFgdPSwcVAxVBBBoaRRYLOlQAAEEPHzNHRysWEA1LBxQSDQ8UWl1vMgY6GkkACQsBOkAcfxYDCgdTEghMFQ8eVAQRGj4XAn44AQZ/BA4xUwcGGAddDQIOEBIaAkUaNxEQVAYBB38eACoBVQEKEBZsLwASCBFFEgY6GkkACQtTKAgdMxdVDQ4WGRVMCQIJGwAWTjAaSQQAGgEwC2ULFhANSwcUEg0PFFdUAgpPVSAMEQ9OBzYTDjEAWUMMHFxsOwgTE1QRDQs2BkkHFB4WLUcfMAQQERhfXRIEBB5bAQsMGjpUQQAECx1/EwYrEhsQSlp3KAkXAglUCAAafxVJAggCHz4OAX8HHQIfUwkOCRhHFx0OAAp/XB0RBABTKw4bPh0GQkJ5KQ4JGEccGxFFGjcRSRYAClM4EhYsUxoNSwcVA0wTEhV+MQ0LJlQHERcLAX8UGzADVRYFBxQKTBUPHlQPCgx/EwwAEk4XMAkKVTAUFhgWXREEBAlbAA0ATigbGxgFThosRwMwABwNDFMcCgBBBBQaERcBM349EQQAUysOGz4dBk9LFBJHZjUCHhpFEQcrFQcHTU4UMEZlFhVVGgQGD0YEBAYJAEUMHX8WBRUCBV9/HgAqUxcGHwcYFEwWBg8XDUUBKgBjLQ4bUzwGATEcAUMOAB4HHARHDxwARRo6FQR+NgYWMUcbNxYMQwgSCQUEQR4UAUlFGjcRGxFBGRwxQBt/ERBDCh0ERggOEhkAbzwBKlMfEUEMFjoJTz0WFBcOHV0EFUETExFFEQs6Ghp+IwsSKwIBfxEMQx8bGEYYBAIVB28xQzpZDFkPT1MrSiZyB1gCRh1QFU1BEx4RC0UaNgAIGhJPUzMCG3gAVQQEUncyQQRKHlkLRE4rWSBZFUMScglCLFJVFw4WE0YYCBMaGhZETjMRHVMSThQwRmULXhBODl4TR0wVSjJZEUgPchpEB0BOBzoCAX8HHBcKHQ5HTA0CD1MWRQkwVWMgTAteOkoBflMBTiJeCUsNTAlWB0RFGjoRB1QVBwc+CRx+UxkGH1QORgsORnEjDQAAfwABERMLVCxHCikaGUMEHV0SBARHGgARBA00fjAbFE4QPglPLRYGF0sYEwkbCAkcVBENCyZUDhsVTgowEh1/ERQAAHk+BxkSAlsDDQAAfwABEUEZHC0LC38dEAYPAF0OCRMIHgdFCgB/BAgAEwEfVTMKOh1VFwIHHAgfTUccG0RvOjoRB1QVBwc+CRxzUxIMSnkyCAlNRw8DCklOKxwbEQRCUzkIGi1fVQQEUncyCQQJWwAMEQ8xB0g="
ciphertextD = base64.b64decode(ciphertext)
known = "When they catch you, there won't be any doubt"




def xorFxn(text, key):
    result = str()
    for i in range(len(text)):
        text_decimal = text[i]
        key_decimal = ord(key[i%len(key)])
        new_decimal = text_decimal^key_decimal
        new_character = chr(new_decimal)
        result += new_character
    return result

def bruteXorce(): #lol
    matches = list()
    pattern = re.compile("flag{\w{20}}", re.IGNORECASE)
    sample = str()
    for i in range(0,len(ciphertextD)):
        sample = xorFxn(ciphertextD[i:-1],known)
        if pattern.search(sample):
            matches.append(pattern.search(sample))
            break
    print("The key/flag is:")
    print(matches[0][0])
    print("Proof:")
    print(xorFxn(ciphertextD, matches[0][0]))

bruteXorce()
