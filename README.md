<p align="center">
  <a href="https://quoteflix.deta.dev/"><img src="https://fontmeme.com/permalink/211219/ead94ebfa0b155c0fc0da100c901d58f.png" /></a>
</p>

# Tech stack
<div>
  
<a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="150" height="150"></a>
<a href="https://fastapi.tiangolo.com/"><img src="https://camo.githubusercontent.com/86d9ca3437f5034da052cf0fd398299292aab0e4479b58c20f2fc37dd8ccbe05/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67" width="300" height="200"></a>
<a href="https://v3.vuejs.org/guide/introduction.html"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1200px-Vue.js_Logo_2.svg.png" width="150" height="150"></a>
<a href="https://getbootstrap.com/docs/5.1/getting-started/introduction/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/1280px-Bootstrap_logo.svg.png" width="150" height="150"></a>
<a href="https://docs.deta.sh/docs/home/"><img src="https://docs.deta.sh/img/logo.svg" width="150" height="150"></a>

</div>

# What it does?

- Get quotes from this [API](https://type.fit/api/quotes) using requests module.
- Fetch quote author image from wikipedia, if available.
- [grequests](https://github.com/spyoungtech/grequests) is used to fetch images asynchronously and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to parse the image links.
- A simple backend API is created using FastAPI. The following endpoints are available:
  - [Homepage](https://quoteflix.deta.dev/)
  - [Quotes With Author Images](https://quoteflix.deta.dev/api)
  - [Quotes](https://quoteflix.deta.dev/api/quotes)
  - [Author images](https://quoteflix.deta.dev/api/images)
- A simple frontend to serve the quotes along with the author image is created using Vue and styled using Bootstrap.
- The app is deployed on deta.sh.

# Screenshots

## Homepage

![homepage](images/homepage.png)

## Terminal

![terminal](images/terminal.png)

- The first time the script is run, the quotes are extacted from the quotes api and author image is fetched from wikipedia.
- The fetched quotes and images data is cached as a JSON file
- For subsequent runs of the script, the data is served from the JSON file.

## Docs

![docs](images/docs.png)

## References

- [Full Stack Python/Vue.js Web App Tutorial - Flask, Web Scraping & More](https://www.youtube.com/watch?v=zmylAaDsdiw)
