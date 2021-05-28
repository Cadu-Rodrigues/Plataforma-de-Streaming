const SpotifyWebApi = require("spotify-web-api-node");
const fs = require("fs");

let spotifyApi = new SpotifyWebApi();
spotifyApi.setAccessToken(
  "BQDyeeAni2DOTalV5eTfuSCzES4_2Q3O9g_6jkf6i5lqjleylxqSxcSg0hmgq2dpf2TdwCmI5qCxA5t0PRHyrUPgdco3Sqd9L98LZeAV7zShDvFaSr0MqNMi9olEwMgO3lOPuqDJdJiS57v__1CKZaKZSxvR-1gxSiyUz5p7mu6t9pSdvaw91gv44KHvQI_CGC0s3HkQzMhEGzwDsTXbZSD2ruMbkGs_yd1R4o6QoC9sKafDAUEuEsGYouwGePywEZW_hZ63tcFdObBihhjw2MlUyUPyoNo"
);

let playlists = {};
let musicas = {};
let albuns = {};
let artistas = {};

async function main() {
  console.log("gustavo");
  await getData("12177373955");
  console.log("lorena");
  await getData("lorenabraghinim");
  console.log("bia");
  await getData("beatrizgnovais");
  console.log("playlists", Object.keys(playlists));
  console.log("musicas", Object.keys(musicas));
  console.log("albuns", Object.keys(albuns));
  console.log("artistas", Object.keys(artistas));
  fs.writeFileSync(
    "data.json",
    JSON.stringify({ playlists, musicas, albuns, artistas })
  );
}
async function getData(user) {
  let user_playlists = await spotifyApi.getUserPlaylists(user);
  for (let playlist of user_playlists.body.items) {
    playlists[playlist.name] = {};
    playlists[playlist.name].descricao = playlist.description;
    playlists[playlist.name].autor = playlist.owner.id;
    const tracks = await spotifyApi.getPlaylistTracks(playlist.id);
    for (let track of tracks.body.items) {
      if (!musicas[track.track.id]) {
        const album = await spotifyApi.getAlbum(track.track.album.id);
        console.log(track.track.name);
        musicas[track.track.id] = {};
        musicas[track.track.id].nome = track.track.name;
        musicas[track.track.id].fonte = track.track.preview_url;
        musicas[track.track.id].duracao = track.track.duration_ms;
        musicas[track.track.id].popularidade = track.track.popularity;
        musicas[track.track.id].genero = album.body.genres[0];
        albuns[album.body.name] = {};
        albuns[album.body.name].data = album.body.release_date;
        albuns[album.body.name].qtdMusicas = album.body.tracks.total;
        albuns[album.body.name].genero = album.body.genres[0];
        albuns[album.body.name].imagem = album.body.images[1].url;
        for (let artist of album.body.artists) {
          let artistInfos = await spotifyApi.getArtist(artist.id);
          artistas[artistInfos.body.id] = {};
          artistas[artistInfos.body.id].nome = artistInfos.body.name;
          artistas[artistInfos.body.id].seguidores = artistInfos.body.followers;
          artistas[artistInfos.body.id].ouvintes = artistInfos.body.popularity;
          artistas[artistInfos.body.id].imagem = artistInfos.body.images[1].url;
          artistas[artistInfos.body.id].genero = artistInfos.body.genres[0];
        }
      }
    }
  }
}

main();