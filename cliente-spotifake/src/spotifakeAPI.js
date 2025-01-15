const API_URL = 'http://127.0.0.1:8000/api';

export async function fetchArtists() {
    const response = await fetch(`${API_URL}/artists/`);
    return response.json();
}

export async function fetchAlbums() {
    const response = await fetch(`${API_URL}/albums/`);
    return response.json();
}

export async function fetchSongs() {
    const response = await fetch(`${API_URL}/songs/`);
    return response.json();
}

export async function createArtist(artist) {
    const response = await fetch(`${API_URL}/artists/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(artist),
    });
    return response.json();
}