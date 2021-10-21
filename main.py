from moviepy.editor import *
movie = VideoFileClip("rena.mp4").subclip(0,10)
textLayer = TextClip("Maria Tereza", fontsize=80, color='red', font='Daydream')
textLayer = textLayer.set_position(('center', 160)).set_duration(10)

final = CompositeVideoClip([movie, textLayer])
final.write_videofile("rena.mp4")
final.write_gif("rena.gif", fps=25)