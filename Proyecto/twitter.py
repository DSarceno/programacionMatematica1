import tweepy

consumerKey = '179m3TFv4QaOZMBeggnegFzLE'
consumerSecret = 'Ubi29JSc55sO2q0HbyrOmT14uW8CU0V56Iu7mZJg95IlvEbDWE'
accessToken = '979050362970820608-bDXDGgD6xAxUbO1QBoFUdbinEGlBNrv'
accessSecret = '3uh2oUpw8g5fPAGzbHbc0yDzoVAARkiVwQRlZPHuUFfFU'


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# api.update_status('Enviado con Tweepy #Python #Tweepy #BienBrgonTwitteandoDesdeUnArchivoPython :)')


# dataImg = api.media_upload('asciiArt.png')
# print(dataImg)

# api.update_status('#ASCIIArtPM1',media_ids = ['1332124793454415873'])

file = 'asciiArt.png'
tweet = '#ASCIIArtPM1'
api.update_with_media(file, status = tweet)
