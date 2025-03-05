import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def domov():
    api_key = '+LcMuDEStfvEBwQHERSVZw==2SL5YKr6JHShJRru'
    url = 'https://api.api-ninjas.com/v1/quotes/'
    headers = {'X-Api-Key': api_key}

    response = requests.get(url, headers=headers)



    # Preverimo, ali je zahtevek uspešen
    if response.status_code == 200:
        data = response.json()  # Pretvorimo odgovor v JSON
        citat = data[0]['quote']  # Dostopamo do prvega citata v seznamu
        avtor = data[0]['author']
        print(citat)
        print(avtor)
    else:
        print(f"Napaka: {response.status_code} - {response.text}")
    return render_template('index.html', citat=citat, avtor=avtor)

    # Osnovni primer Flask aplikacije






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)