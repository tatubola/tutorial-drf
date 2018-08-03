from rest_framework import serializers
from music.models import Album, Artist, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'tracks', 'year')


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = (
            'albums',
            'birthday',
            'email',
            'marital_status',
            'name',
            'gender',
            'fullname',
        )

    def create(self, validated_data):
        albums_data = validated_data.pop('albums')
        artist = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            tracks_data = album_data.pop('tracks')
            album = Album.objects.create(artist=artist, **album_data)
            for track_data in tracks_data:
                Track.objects.create(album=album, **track_data)
        return artist
