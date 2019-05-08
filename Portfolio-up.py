import webbrowser
#=================================html_file=====================================
html_file = open("Portfolio-index.html","w+")

divs={"head":"<div class=\"head\">",
      "middle": "<div class=\"middle\">",
      "left": "<div class=\"left\">",
      "right": "<div class=\"right\">",
      "fullname": "<div class=\"fullname\">",
      "profile_pic": "<div class=\"profile_pic\">",
      "job_name": "<div class=\"job_name\">",
      "media": "<div class=\"media\">",
      "content": "<div class=\"content\">",
      "rightbox": "<div class=\"right box\">"
     }
nav_bar=["<a href=\"#\">Home</a>",
         "<a href=\"#\">About</a>",
         "<a href=\"#\">Skills</a>",
         "<a href=\"#\">Experiences</a>",
         "<a href=\"#\">Education</a>",
         "<a href=\"#\">Portfolio</a>",
         "<a href=\"#\">clients</a>",
         "<a href=\"#\">Contact</a>"
        ]
media=["<img src=\"images/twitter.png\" alt=\"twitter\">",
       "<img src=\"images/facebook.png\" alt=\"facebook\">",
       "<img src=\"images/googleplus.png\" alt=\"google plus\">",
       "<img src=\"images/linkedin.png\" alt=\"linkedin\">",
       "<img src=\"images/github.png\" alt=\"github\">"
      ]
images={"pc":"<img src=\"images/full-stack.jpeg\" alt=\"full stack\">",
        "profile_pic":"<img src=\"images/profile_pic.png\" alt=\"profile picture\">",
        "logo":"<img src=\"images/full-stack-dev.jpg\" alt=\"full stack dev\">"
       }
headings=["<h2>Full Name</h2>",
          "<h2>Full Stack Developer</h2>",
          "<h2>Who am I?</h2>"
         ]
paragraph="""<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
          quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
          nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
          deserunt mollit anim id est laborum.</p>"""
tab1="\t" + "\t"
tab2="\t" + "\t" + "\t"
tab3="\t" + "\t" + "\t" + "\t"
tab4="\t" + "\t" + "\t" + "\t" + "\t"
newLine1= "\n"
newLine2= "\n" + "\n"

html = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">

    <link rel="stylesheet" href="Portfolio-style.css">
    <title>Portfolio Template</title>
  </head>
  <body>
"""
html += newLine1
html += tab1 + divs["head"] + newLine1
for a in nav_bar:
    html += tab2 + a + newLine1
html += tab1 + "</div>" + newLine2

html += tab1 + divs["middle"] + newLine1
html += tab2 + divs["left"] + newLine1
html += tab3 + images["pc"] + newLine1
html += tab2 + "</div>" + newLine2

html += tab2 + divs["right"] + newLine1
html += tab3 + divs["fullname"] + newLine1
html += tab4 + headings[0] + newLine1
html += tab3 + "</div>" + newLine1

html += tab3 + divs["profile_pic"] + newLine1
html += tab4 + images["profile_pic"] + newLine1
html += tab3 + "</div>" + newLine1

html += tab3 + divs["job_name"] + newLine1
html += tab4 + headings[1] + newLine1
html += tab3 + "</div>" + newLine1

html += tab3 + divs["media"] + newLine1
for m in media:
    html += tab4 + m + newLine1
html += tab3 + "</div>" + newLine1
html += tab2 + "</div>" + newLine1
html += tab1 + "</div>" + newLine2

html += tab1 + divs["content"] + newLine1
html += tab2 + divs["left"] + newLine1
html += tab3 + images["logo"] + newLine1
html += tab2 + "</div>" + newLine2

html += tab2 + divs["rightbox"] + newLine1
html += tab3 + headings[2] + newLine1
html += tab3 + paragraph + newLine1
html += tab2 + "</div>" + newLine1
html += tab1 + "</div>" + newLine1

html +="""
 </body>
</html>"""

html_file.write(html)
html_file.close()
#=================================css_file======================================
css_file = open('Portfolio-style.css','w+')
css = """
* {
 padding: 0;
 margin: 0;
 box-sizing: border-box;
 font-family: Helvetica;
}
body{
background-color: #2c3e50;
}
.head {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 60px;
  background-color: #34495e;
  padding: 5px 15px;
  border-bottom: 5px solid tomato;
}
.head a {
  display: inline-block;
  background-color: #2c3e50;
  border-radius: 5px;
  min-width: 100px;
  min-height: 30px;
  text-align: center;
  padding-top: 5px;
  margin-top: 10px;
  color: white;
  text-decoration: none;
}
.head a:hover {
  background-color: #34495e;
  color: lightblue;
}

.middle {
  background-color: turquoise;
  text-align: center;
  display: flex;
  flex-direction: row;
}
.left {
  flex: 35%;
}
.left img {
  width: 100%;
  height: 100%;
}
.right {
  flex: 65%;
  padding: 25px;
  border-left: 5px solid tomato;
}

.media {
  margin-top:20px;
}
.media img {
  width: 25px;
  height: 25px;
  opacity: 0.5;
  cursor: pointer;
}
.media img:hover {
  opacity: 1;
}

.content {
  display: flex;
  flex-direction: row;
  margin-top: 25px;
  background-color: #dcdde1;
}

.box h2 {
  margin-bottom: 15px;
}
.box p {
  text-align: justify;
  font-size: 20px;
}
"""
css_file.write(css)
css_file.close()
#===========================open in the browser=================================
webbrowser.open_new_tab('Portfolio-index.html')
