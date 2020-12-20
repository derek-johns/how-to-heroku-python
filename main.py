from flask import Flask

pagehtml = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The Schooner</title>
  <meta name="description" content="The Schooner">
  <meta name="author" content="Kristofer">

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #303030;
  max-width: 40rem;
  padding: 2rem;
  margin: auto;
  background: #FEF4FF;
}
img {
  max-width: 100%;
}
a {
  color: #2ECC40;
}
h1, h2, strong {
  color: #303030;
}
</style>
</head>

<body>
  <h2>The Schooner</h2>
  <p><img src="http://www.marinemodelartist.com/Mary_Taylor/Mary_Taylor_files/shapeimage_4.png"</p>
  <p>This is a schooner.</p>
  
  


  <h2>The Bluenose II</h2>
  <p><img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBluenose_II&psig=AOvVaw2C0EaT4wVx8raQ8VnpcG_i&ust=1608513078096000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPCntbaw2-0CFQAAAAAdAAAAABAD"</p>
  <p>This is a Bluenose.</p>


</body>
</html>
"""
app = Flask(__name__)

@app.route("/")
def hello():
    return pagehtml
