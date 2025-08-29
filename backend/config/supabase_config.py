from supabase import create_client

SUPABASE_URL = "https://pldaffgvtjgyptahsqvo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsZGFmZmd2dGpneXB0YWhzcXZvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY1MDE4NTEsImV4cCI6MjA3MjA3Nzg1MX0.E7x-ZFUW5Np8i9qm1TUnRRAbhAgJEf7IY4fBfseTek4"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
data = supabase.table("sensor_readings").select("*").execute()
print(data)

