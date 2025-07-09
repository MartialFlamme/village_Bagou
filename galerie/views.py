from django.shortcuts import render

def photos(request):
    photos = [
        {'src': 'images/galerie/fete1.jpg', 'alt': 'Fête traditionnelle'},
        {'src': 'images/galerie/grotte.jpg', 'alt': 'Grottes sacrées'},
        {'src': 'images/galerie/danse.jpg', 'alt': 'Danse Kessou'},
        {'src': 'images/galerie/roi.jpg', 'alt': 'Roi au palais'},
    ]
    return render(request, 'galerie/photos.html', {'photos': photos})

def videos(request):
    videos = [
        {'titre': 'Cérémonie d’intronisation', 'youtube_id': 'dQw4w9WgXcQ'},
        {'titre': 'Danses Mangambeu en live', 'youtube_id': 'YbJOTdZBX1g'},
    ]
    return render(request, 'galerie/videos.html', {'videos': videos})
