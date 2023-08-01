from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# extra packackes
import os
import aspose.slides as slides
import aspose.pydrawing as drawing


def home(request):
    Ppt(request)
    all_thumb= {
        "thumb":[
            os.path.join(
        os.getcwd(), "projectapp","src","ppt", i) for i in os.listdir(os.path.join(os.getcwd(), "projectapp","src","ppt"))
        ],
        "name":["name1"]
        }
    return render(request, 'slide.html', context=all_thumb)


# def navbar(request):
#     return render(request, 'navbar.html', context=context)

def slide(request):
    thumb_files = Ppt(request)
    return HttpResponse("<h1>{} </h1>".format(str(thumb_files.get_thumbnil))) 
    

# def punce(request):
#     return render(request, 'text.html')

# def remove_punce(request):
#     djtext = request.GET.get('text','')
#     print(djtext)
#     punce_char = '''!()-[]{};:'"\,<>./?@#$^&*_~'''''
#     analyzed_text = ''
#     for char in djtext:
#         if char not in punce_char:
#             analyzed_text = analyzed_text + char
#     analyzed_text_dict = {'purpose':'ANALYZED TEXT IS THERE', 'new_text': 'analyzed_text'}

#     print(analyzed_text)
    
#     return render(request, 'analyze.html', analyzed_text_dict)
    
class Ppt():
    def __init__(self, request):
        # self.all_file = os.listdir(os.path.join(os.getcwd(), "projectapp","src","ppt"))
        self.thumbnil = []
        self.get_thumbnil()
    
    def get_thumbnil(self):
        file_list = os.path.join(
                                os.getcwd(),
                                "projectapp","src","ppt"
                                )
        for files in os.listdir(os.path.join(os.getcwd(), "projectapp","src","ppt")):
            if ".ppt" in files:
                with slides.Presentation("projectapp/src/ppt/ab.pptx") as pres:
                    for slide in pres.slides:
                        bmp = slide.get_thumbnail(1, 1)
                        # bmp.save("Thumbnail.jpg", drawing.imaging.ImageFormat.jpeg)
                        bmp.save(
                            os.path.join(
                                os.getcwd(),
                                "projectapp","src","ppt","{}.jpg".format(files.split(".")[0]
                                        )
                                ), 
                            drawing.imaging.ImageFormat.jpeg
                            )
                        self.thumbnil.append("{}.jpg".format(files.split(".")[0]))
        print(">>>>>>>>>>>>>>>>..", self.thumbnil)


def home1(request):
    Ppt(request)
    all_thumb= {
        "thumb":"projectapp/src/ppt/ab.jpg"
        }
    return render(request, 'test1.html', {"thumb":"projectapp/src/ppt/ab.jpg"})