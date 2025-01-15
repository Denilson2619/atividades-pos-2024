import React, { useEffect, useState } from 'react';
import { fetchArtists } from '../api/spotifakeAPI';

function ArtistList() {
    const [artists, setArtists] = useState([]);

    useEffect(() => {
        fetchArtists().then(setArtists);
    }, []);

    return (
        <div>
            <h1>Artists</h1>
            <ul>
                {artists.map((artist) => (
                    <li key={artist.id}>{artist.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default ArtistList;