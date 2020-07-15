# Note: File is called ptext because
# https://github.com/pyinstaller/pyinstaller/issues/4626

from PyInstaller.compat import is_win
from PyInstaller.utils.hooks import collect_dynamic_libs

if is_win:
    skip_libs = (
        "libffi-7.dll",
        "libcrypto-1_1.dll"
        "libssl-1_1.dll",
        "libjpeg-9.dll",
        "sdl2.dll",
        "libpng16-16.dll",
        "sdl2_image.dll",
        "sdl2_mixer.dll",
        "sdl2_ttf.dll",
        "libfreetype-6.dll",
        "zlib1.dll"
    )
    collected_binaries = collect_dynamic_libs("pygame", ".")

    l = []
    for fname, dest in collected_binaries:
        if fname.lower().endswith(skip_libs):
            continue
        l.append((fname, dest))

    binaries = l