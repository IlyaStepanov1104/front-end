from django.shortcuts import render


def index(request):
    text = "Если ты не голубой, нарисуй вагон другой: "
    image = "http://img2.reactor.cc/pics/post/full/anon-1483595.png"
    alt = "ПОЕЗД"
    return render(request, "index.html", {"post_text": text, "post_image": image, "post_image_alt": alt})
