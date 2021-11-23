from django.shortcuts import render,redirect
import bs4
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.contrib.auth.decorators import login_required
import random

#MOVIE_DATA_SCRAPER
def get_movie_data(url_category):
    url = requests.get(url_category)
    sad_soup = bs4.BeautifulSoup(url.text, "lxml")
    full_movie_details = []
    movie_titles = sad_soup.select('.lister-item-header a')
    movie_years = sad_soup.select('.lister-item-year')
    movie_ratings = sad_soup.select(".ratings-imdb-rating strong")
    movie_time = sad_soup.select(".runtime")
    movie_genre = sad_soup.select(".genre")
    no_of_movies = len(movie_titles)
    for movie in range(no_of_movies):
        movie_details = {}
        movie_details["title"] = movie_titles[movie].getText()
        movie_details["year"] = movie_years[movie].getText()
        movie_details["genre"] = movie_genre[movie].getText()
        movie_details["imdb_link"] = "https://www.imdb.com/" + movie_titles[movie].get('href')
        title = movie_details["title"].replace(' ', '+') + '+trailer'
        start_url = "https://www.youtube.com/results?search_query=" + title
        try:
            movie_details["rating"] = movie_ratings[movie].getText()
        except IndexError:
            movie_details["rating"] = "null"
        try:
            movie_details["time"] = movie_time[movie].getText()
        except IndexError:
            movie_details["time"] = "null"
        youtube_search_soup = requests.get(start_url)
        test_str = youtube_search_soup.text
        test_sub = "videoId"
        res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]
        # print("The start indices of the substrings are : " + str(res))
        videoId = test_str[res[0]:res[0] + 22]
        movie_details["trailer"] = "https://www.youtube.com/embed/" + videoId.split(':')[1].replace('"', '')
        full_movie_details.append(movie_details)
    full_movie_details = random.sample(full_movie_details, len(full_movie_details))
    return full_movie_details
#MUSIC_DATA_SCRAPER
def get_music_data(playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="1fe7707b45a745998b029e66de3803de",
                                                               client_secret="b011319c06f5422b8816f5c947edb3ed"))
    playlists = sp.playlist(playlist_id, fields='tracks(items)', market='IN')
    full_song_details = []
    for item in playlists['tracks']['items']:
        song_detials = {
            'title': item['track']['name'],
            'image': item['track']['album']['images'][0]['url'],
            'url': item['track']['external_urls']['spotify'],
            'length': round(((item['track']['duration_ms'])/(1000*60))%60,2),
            'artist_url': item['track']['artists'][0]['external_urls']['spotify'],
            'artist_name': item['track']['artists'][0]['name'],
            'album_name': item['track']['album']['name'],
            'album_link': item['track']['album']['external_urls']['spotify']
        }
        full_song_details.append(song_detials)
    full_song_details = random.sample(full_song_details, len(full_song_details))
    return full_song_details
#CHECK USER IS LOGGED IN
@login_required(login_url='/accounts/signin/',redirect_field_name=None)
#MOOD AND CONTENT SELECTION CATEGORY PAGE
def detection(request):
    if request.method == 'POST':
        request.session['mood_sel']= request.POST['mood_sel']
        request.session['content_sel']= request.POST['content_sel']
        mood_sel = request.session.get('mood_sel')
        content_sel = request.session.get('content_sel')
        if mood_sel == 'Angry':
            if content_sel == 'Movie':
                return redirect('angry_movie')
            elif content_sel == 'Music':
                return redirect('angry_music')
            elif content_sel == 'Motivational Videos':
                return redirect('angry_motivation')
            elif content_sel == 'Games':
                return redirect('angry_games')
            elif content_sel == 'Books':
                return redirect('angry_books')

        elif mood_sel == 'Sad':

            if content_sel == 'Movie':
                return redirect('sad_movie')
            elif content_sel == 'Music':
                return redirect('sad_music')
            elif content_sel == 'Motivational Videos':
                return redirect('sad_motivation')
            elif content_sel == 'Games':
                return redirect('sad_games')
            elif content_sel == 'Books':
                return redirect('sad_books')

        elif mood_sel == 'Happy':
            if content_sel == 'Movie':
                return redirect('happy_movie')
            elif content_sel == 'Music':
                return redirect('happy_music')
            elif content_sel == 'Motivational Videos':
                return redirect('happy_motivation')
            elif content_sel == 'Games':
                return redirect('happy_games')
            elif content_sel == 'Books':
                return redirect('happy_books')

        elif mood_sel == 'Surprise':
            if content_sel == 'Movie':
                return redirect('surprise_movie')
            elif content_sel == 'Music':
                return redirect('surprise_music')
            elif content_sel == 'Motivational Videos':
                return redirect('surprise_motivation')
            elif content_sel == 'Games':
                return redirect('surprise_games')
            elif content_sel == 'Books':
                return redirect('surprise_books')

        elif mood_sel == 'Neutral':
            if content_sel == 'Movie':
                return redirect('neutral_movie')
            elif content_sel == 'Music':
                return redirect('neutral_music')
            elif content_sel == 'Motivational Videos':
                return redirect('neutral_motivation')
            elif content_sel == 'Games':
                return redirect('neutral_games')
            elif content_sel == 'Books':
                return redirect('neutral_books')
        else:
            return render(request, 'detection.html')
    else:
        return render(request,'detection.html')
#ANGRY_MOVIE_FUCTION
@login_required(login_url='/accounts/signin/')
def angry_movie(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_movie_data(
        "http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter")
    return render(request, 'content.html', {'mood_sel': mood_sel, 'content_sel': content_sel, 'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def angry_music(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_music_data('37i9dQZF1DX3rxVfibe1L0')
    return render(request, 'content_song.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def angry_motivation(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def angry_games(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def angry_books(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def happy_movie(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_movie_data(
        "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter")
    return render(request, 'content.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def happy_music(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_music_data('37i9dQZF1DWTwbZHrJRIgD')
    return render(request, 'content_song.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def happy_motivation(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def happy_games(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def happy_books(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def sad_movie(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_movie_data(
        "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter")
    return render(request, 'content.html', {'mood_sel': mood_sel, 'content_sel': content_sel, 'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def sad_music(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_music_data('37i9dQZF1DWZKuerrwoAGz')
    return render(request, 'content_song.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def sad_motivation(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def sad_games(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def sad_books(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def surprise_movie(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_movie_data(
        "http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter")
    return render(request, 'content.html', {'mood_sel': mood_sel, 'content_sel': content_sel, 'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def surprise_music(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_music_data('4oGJbaDcFJ8YAQhvZZY9JS')
    return render(request, 'content_song.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def surprise_motivation(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def surprise_games(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def surprise_books(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def neutral_movie(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_movie_data(
        "http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter")
    return render(request, 'content.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def neutral_music(request):
    mood_sel = request.session.get('mood_sel')
    content_sel = request.session.get('content_sel')
    full_details = get_music_data('37i9dQZF1DWWQRwui0ExPn')
    return render(request, 'content_song.html', {'mood_sel': mood_sel, 'content_sel': content_sel,'full_details': full_details})
@login_required(login_url='/accounts/signin/')
def neutral_motivation(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def neutral_games(request):
    return render(request, 'coming_soon.html')
@login_required(login_url='/accounts/signin/')
def neutral_books(request):
    return render(request, 'coming_soon.html')






