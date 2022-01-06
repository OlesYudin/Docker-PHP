from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-superJumbo.jpg?quality=75&auto=webp",
    "https://static01.nyt.com/images/2021/08/17/science/28cats1/28cats1-superJumbo.jpg?quality=75&auto=webp",
    "https://static01.nyt.com/images/2019/10/01/science/00SCI-CATS1/merlin_102054072_34962289-a2a4-4c52-9969-4b2719347e76-superJumbo.jpg?quality=75&auto=webp",
    "https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg",
    "https://th-thumbnailer.cdn-si-edu.com/bZAar59Bdm95b057iESytYmmAjI=/1400x1050/filters:focal(594x274:595x275)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/95/db/95db799b-fddf-4fde-91f3-77024442b92d/egypt_kitty_social.jpg",
    "https://static.scientificamerican.com/sciam/cache/file/92E141F8-36E4-4331-BB2EE42AC8674DD3.jpg",
    "https://cdn.vox-cdn.com/thumbor/jQTaYiRCAwpJsR6y4nI8Iwr0_DI=/0x0:4758x3569/1400x788/filters:focal(0x0:4758x3569):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/42021742/8536633928_62a8d4fb3b_o.0.0.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")