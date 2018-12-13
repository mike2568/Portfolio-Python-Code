def print_list(items):
        for item in items:
                print(str(items))
name = input("whats your name?")
smile = input("Wanna see something that will make you smile " + name + "? [Yes,No]")
if smile =="yes":
        print("Hell yh, here is a free smile")
        smilers = ["1. Some random image","2. Some random video"]
        smilers.sort()
        print_list(smilers)
        ask = input("[1,2]")
        if smilers == "1":
          f = open('meme.jpg', 'r+')
          jpgdata = f.read()
          f.close()
        
        if smilers == "2":
                        print("here you go...")
                        import cv2
                        cap = cv2.videoCapture("video.mp4")
                        ret, frame = Cap.read()
                        while(1):
                                ret, frame = cap.read()
                                cv2.imshow('frame',frame)
if smile =="no":
        print("Why not whats  the harm ¯\_(ツ)_/¯? Oh well naybe another time")
