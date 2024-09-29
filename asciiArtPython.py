"""
This library includes the following functions:/Cette bibliothèque comprend les fonctions suivantes :
    - fromImages
    - toImages
    - fromAndToImages
    - fromAndToVideos
    - toTxt
    - printInTerminal
    - liveFromWebcam
    
"""
#-----------------internal functions-----------------
def _importImageWB(path:str):
    #importing modules
    from PIL import Image
    
    #return the imported image and set it to black and white
    return Image.open(path).convert("L")

def _reduceImageQuality(image,size:int=10000):
    #pre-execution checks
    assert type(size)==int, "size must be an integer"
    
    #image size calculations
    n1=image.size[0]
    n2=image.size[1]
    size=n1*n2/size
    n1=n1/(size**0.5)
    n2=n2/(size**0.5)
    
    #return the resized image
    return image.resize((int(n1), int(n2)))

def _captureWebcam(cap):
    import cv2
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)
    return pil_image.convert("L")

def _image2Numpy(image):
    #importing modules
    from numpy import asarray
    
    #return the numpy table
    return asarray(image)

def _numpy2Array(numpyTab,nb:int=12)->list:
    #pre-execution checks
    assert type(nb)==int, "nb must be an integer"
    
    #conversion
    tab = []
    for i in range(len(numpyTab)):
        liste = []
        for j in numpyTab[i]:
            liste.append(int(j/256*nb))
        tab.append(liste)
    
    #return the array
    return tab

def _array2Ascii(array:list,liste:list=0)->list:
    #pre-execution checks
    assert type(array)==list, "array must be a list"
    if type(liste) != list:
        liste=["#","@","&","$","{","(","=","*",";",":","."," "]
    
    #conversion to ASCII Art
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]=liste[array[i][j]]
    
    #return the ASCII array
    return array

def _characterList(tableau:list,coef:int=1,depart:int=0)->list:
    liste=[]
    for i in range(len(tableau)):
        caracInter=""
        for j in range(depart,len(tableau[i])*coef-depart,coef):
            caracInter=caracInter+tableau[i][j]
        liste.append(caracInter)
    return liste

def _video2Pics(link:str)->(int,int):
    #importing modules
    import cv2
    
    #convert video to full frames
    vidcap = cv2.VideoCapture(link)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps / 10)
    success, image = vidcap.read()
    count = 0
    frame_count = 0
    while success:
        if frame_count % frame_interval == 0:
            cv2.imwrite("./data/frame%d.jpg" % count, image)
            count = count+1
        success, image = vidcap.read()
        frame_count=frame_count+1
    TMP=vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    vidcap.release()
    return count,round(round(TMP)/round(fps))

def _pics2Video(pics:list,fpsvid:int=10,path:str="mika_export"):
    #importing modules
    try:
        from tqdm import tqdm
    except ModuleNotFoundError:
        pass
    import cv2
    
    frame = cv2.imread(pics[0])
    height, width, layers = frame.shape
    size = (width, height)
    out = cv2.VideoWriter("mika_export_inter.avi", cv2.VideoWriter_fourcc(*'DIVX'), fpsvid, size)
    try:
        for image in tqdm(pics):
            img = cv2.imread(image)
            out.write(img)
    except NameError:
        for image in pics:
            img = cv2.imread(image)
            out.write(img)
    out.release()

def _combineVideoWithAudio(name:str,to:str="mika_export_final.mp4"):
    from moviepy.editor import VideoFileClip
    # Chemin vers vos fichiers
    video_path = "mika_export_inter.avi"
    audio_path = name
    output_path = to
    
    # Charger la vidéo et l'audio
    video = VideoFileClip(video_path)
    audio = VideoFileClip(audio_path).audio
    
    # Assigner l'audio à la vidéo
    video = video.set_audio(audio)
    
    # Exporter la vidéo finale avec compression
    video.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        bitrate='15M',  # Ajustez le bitrate pour la vidéo
        audio_bitrate='128k'  # Ajustez le bitrate pour l'audio
        )
    
    # Fermer les clips
    video.close()
    audio.close()
#-----------------internal functions-----------------


#-----------------main functions-----------------
def fromImages(path:str,size:int=250000)->list:
    """
    Parameters
    ----------
    path : str
        this parameter must be the path to the source image to be transformed into Ascii.
    size : int, optional
        this parameter defines the number of characters searched for. the default is 250000.

    Returns
    -------
    list
        this function returns a list of character strings corresponding to the various lines.
    """
    #importing modules
    import os
    
    #pre-execution checks
    assert type(path)==str,"image path must be in string format"
    assert os.path.isfile(path), "the specified image does not exist"
    assert type(size)==int, "image size must be in integer format"
    
    #execution of functions used for images
    return _characterList(_array2Ascii(_numpy2Array(_image2Numpy(_reduceImageQuality(_importImageWB(path),size)))))

def toImages(liste:list,num:str="",path:str="mika_export"):
    #importing modules
    from PIL import Image,ImageFont,ImageDraw
    
    assert type(liste)==list and all(type(liste[i])==str for i in range(len[liste]))

    #exportation
    font = ImageFont.truetype("FUTRFW.TTF", 20)
    img = Image.new("RGB", (len(liste[0])*20,len(liste)*20), color = "white")
    draw = ImageDraw.Draw(img)
    
    for i in range(len(liste)):
        draw.text((0, i*20),liste[i],(0,0,0),font=font)
    img.save(path+str(num)+".png")
    
def fromAndToVideos(path:str):
    """
    Parameters
    ----------
    path : str
        this function takes the path to a video as input.
    
    Returns
    -------
    None.
    """
    #importing modules
    import os
    try:
        from tqdm import tqdm
    except ModuleNotFoundError:
        pass
    
    #pre-execution checks
    assert type(path)==str, "image path must be in string format"
    assert os.path.isfile(path), "the specified video does not exist"
    if not(os.path.isdir("data")):
        os.mkdir("data")
    
    #execution of functions used for videos
    nb,duration=_video2Pics(path)
    listPath=[]
    try:
        for i in tqdm(range(nb)):
            toImages(fromImages("./data/frame"+str(i)+".jpg",10000),str(i),"./data/frame_export")
            listPath.append("./data/frame_export"+str(i)+".png")
    except NameError:
        for i in range(nb):
            toImages(fromImages("./data/frame"+str(i)+".jpg",10000),str(i),"./data/frame_export")
            listPath.append("./data/frame_export"+str(i)+".png")
    _pics2Video(listPath)
    _combineVideoWithAudio(path,path[:-4]+"_mika.mp4")

def toTxt(liste:list,path:str="file.txt"):
    """
    Parameters
    ----------
    liste : list
        this function takes a list of character strings as input and writes each element of the list to a different line in a .txt file.
    path : str: optional
        this parameter defines the name of the file to which the list is to be exported. the default is "file.txt".
    
    Returns
    -------
    None.
    """
    assert type(liste)==list and all(type(liste[i])==str for i in range(len[liste]))
    file=open(path,"w")
    for i in range(len(liste)):
        file.write("\n"+liste[i])
    file.close()

def fromAndToImages(path:str,size:int=250000):
    toImages(fromImages(path,size))

def printInTerminal(liste:list):
    """
    Parameters
    ----------
    liste : list
        this function displays a list of character strings in a terminal in a single block.

    Returns
    -------
    None.

    """
    import sys
    var=""
    #var=liste[0]
    for i in range(0,len(liste)):
        if i%2==0:
            var=var+"\n"+liste[i]
    sys.stdout.write(var)
    sys.stdout.flush()

def liveFromWebcam():
    """
    To see you in direct time in ascii art !
    """
    import cv2
    from time import sleep
    cap = cv2.VideoCapture(0)
    while True:
        printInTerminal(_characterList(_array2Ascii(_numpy2Array(_image2Numpy(_reduceImageQuality(_captureWebcam(cap),15000))),[" ",".",":",";","*","=","(","{","$","&","@","#"]),-1,-1))
        sleep(0.1)
#-----------------main functions-----------------
