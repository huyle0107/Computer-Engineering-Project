import requests

print("Bắt đầu")
url = "http://18.205.244.197:4000/api/v1/supabase/sensors"
res = requests.get(url)
print("End")