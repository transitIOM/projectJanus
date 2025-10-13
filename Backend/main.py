import json
from ai_processing import AiProcessing
from scraper import Scraper
import shutil

processor = AiProcessing()
output = processor.analyze_document("https://temp-ocr-data-storage.s3.eu-west-2.amazonaws.com/plsplsplsplsplsplsv3.tiff?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCWV1LXdlc3QtMiJIMEYCIQDjZ41e%2FjpbfLAEY2q4jXip%2BVHK8ZMzsxEK7SAjfVR2pAIhAKFOqbVyimpruNjVLn99%2B%2FFM69IEIE7sGlNd07BCn9uPKsIDCNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMODk3NzI5MTI3MzM0IgxXfmc95KNKyg0Exz0qlgPQN7WAt637eJIhUceViGrFD%2Bp3GK%2F8p0xnUji6hl7dVHGLW2ptX2bOEw6Ho8OlKqX5U2BmrOjzX0aeKMG5YcJADVq83nMoFZ1UCIir74PXHksx5SRd5hSJHFy4TZNZoyA8vUoSz36%2F21ZIjncOxPb1jiL6MgUOJUaQ%2BiumP3v6%2Bzhd5jT6n6W5pXQMaxozaJi2Cbv9KSwaDHMIB1%2BXsWz2nsHVYOfRXh4%2FWyQFstkY%2BSr8I5UVill8kEaSiKYR5MXpnnfU4yz5Esv%2FRbplsNkivmIoNek2wl4llSizcZ9aJYmjvctqvam64eUdEkzzlIkDb01dNnrJ78qwri%2FOGekv%2FR7eD0ssAfjPPnTnBcnE4WeeSlETg20DFdwTrnlzQ5oiDfi9El5UBwGJ2XspKSDMm4vg7%2Bu%2BWrpW%2FYBArgi2LJRAig4xr8mcn7Ou059SNE5uPg6f9Glee1UHTeAmBp7OyiJHLO4dgdJlVsdDgS4Y1nLOrcMbJAoQkNlvgTo2nKk3MPoW9ntWz1xKpu%2FxPFT6ykvNv8dgMLjCn8cGOt0C4QVaGSCUVzpEYX5K1ltxmNEd7Y%2BnX0%2FREas0nyJR1BetDcynGxg%2B7Bn9gQmlLkoxKAtLukaO8Wp%2BXhCl2RnpsAFtYE%2FSHRy3jDuikky9vBvj7J0RIQv19hZT7Ze%2BMOZXQJd1tffVlAC4IZ32dnPBgXzfXb7QWyHxv8MFE2l6e1NdqLIAhmLOKuJdXsMmu0ssS2jQ8YqC2P9EQsoqG7QjctFbEEfcNMpImV61qmym1hIszvLCqpUbRcQKfs4Gm%2FltCibueCAbA%2FG4hyx2ay2V0Lbwx7B32M1Sl82woZOu1e3Jm1vcPBawk2%2FE45u3GRvMCDgocvcWDEA2CopiINJP5okD0oZbVTTKAmgBiVWYgepAUof6AmWGT5m9gJvWD0P350cXiUStPQUfZ7Ttryc7uX2aH0FuBkwWPwNIxiZg5ibwaLX2hxH%2FUa%2BFWFu0p8ZYQbO2rsf2HKWUDjN4NQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5CBGTMOTCBCWIFBW%2F20251009%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251009T162302Z&X-Amz-Expires=10800&X-Amz-SignedHeaders=host&X-Amz-Signature=d09a83cbf2a3c0d99000f48e067273eb0acad0ffbd8b976e5a8fe1aa55944cff")

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# scraper = Scraper()
# scraper.scrape()
# print("Scraping complete, press key to delete temporary files")
# input()
# shutil.rmtree("./tempdata/")
# print("Temporary files deleted")