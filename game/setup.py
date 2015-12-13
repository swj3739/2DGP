mygame = Target(
script="mygame.py",
dest_base = "MyGame",
icon_resources=[(1, r"pico2d.ico")],
other_resources = [(RT_MANIFEST, 1, (manifest_template %
dict(prog="mygame", level="asInvoker")).encode("utf-8"))],
)
res_etc = './resource/etc/'
res_back = './resource/background/'
res_char = './resource/character/'
res_sound = './resource/sound/'

if platform.architecture()[0] == '32bit':
    sdl_folder = './SDL2/x86/'
else:
    sdl_folder = './SDL2/x64/'

sdl_dlls = [sdl_folder + file_name for file_name in os.listdir(sdl_folder)]

etc_dlls = [res_etc  + file_name for file_name in os.listdir(res_etc )]
back_dlls = [res_back  + file_name for file_name in os.listdir(res_back )]
char_dlls = [res_char + file_name for file_name in os.listdir(res_char)]
sound_dlls = [res_sound + file_name for file_name in os.listdir(res_sound)]

setup(name="name",
      windows=[mygame],
      data_files=[(res_etc , etc_dlls),(res_back , back_dlls),(res_char , char_dlls),(res_sound , sound_dlls),(sdl_folder, sdl_dlls) ],
      zipfile=None,
      options={"py2exe": py2exe_options},
      )