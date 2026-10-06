Checkpoint ka jawab (isko apne shabdon me likhna)

Jab GET /hello/Richa aata hai:

Browser/curl, VM ke port 8000 par HTTP request bhejta hai.
Uvicorn use receive karke FastAPI ko deta hai.
FastAPI route list me match dhoondhta hai: /hello/{name} match hota hai aur name = "Richa" ban jata hai.
Type hint (name: str) se value validate hoti hai.
Aapka function chalta hai aur Python dict return karta hai.
FastAPI dict ko JSON me badalta hai, status 200 OK lagata hai aur response wapas bhej deta hai.
