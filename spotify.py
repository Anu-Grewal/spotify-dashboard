import requests
import pandas as pd
import base64

# Spotify API credentials
CLIENT_ID = 'b1355480d56446febb658c8e2dcae347'  # Replace with your actual Client ID
CLIENT_SECRET = '20fa923ad25f4a7794087da376216b2a'  # Replace with your actual Client Secret

# Base64 encode the client ID and client secret
auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_bytes = auth_str.encode('utf-8')
auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')

# Request access token
response = requests.post(
    'https://accounts.spotify.com/api/token',
    headers={
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data={
        'grant_type': 'client_credentials'
    }
)

# Check for errors in the response
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

# Load the CSV file with ISO-8859-1 encoding
df = pd.read_csv(r'C:\Users\AnuPuneetKomal\Downloads\sportify\spotify-2023.csv', encoding='ISO-8859-1')

# Add a new column for Album Cover URL if it doesn't exist
if 'Album Cover URL' not in df.columns:
    df['Album Cover URL'] = ''

# Function to get album cover URL
def get_album_cover_url(track_name, artist_name):
    query = f'{track_name} {artist_name}'
    search_url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': query, 'type': 'track', 'limit': 1}
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    if 'tracks' in data and data['tracks']['items']:
        album_cover_url = data['tracks']['items'][0]['album']['images'][0]['url']  # Get the largest album cover image
        return album_cover_url
    return 'Not Found'

# Iterate through rows and update Album Cover URLs
for index, row in df.iterrows():
    album_cover_url = get_album_cover_url(row['track_name'], row['artist(s)_name'])
    df.at[index, 'Album Cover URL'] = album_cover_url
    print(f"Processed {index + 1}/{len(df)}: Album Cover URL - {album_cover_url}")

# Save the updated CSV file
df.to_csv(r'C:\Users\AnuPuneetKomal\Downloads\sportify\spotify_tracks_with_cover_urls.csv', index=False)
print("Updated file saved as 'spotify_tracks_with_cover_urls.csv'")