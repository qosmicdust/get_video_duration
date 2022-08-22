from subprocess import CalledProcessError, check_output


def get_duration(src):

    try:
        a = check_output(
            f'ffprobe -v error -show_entries format=duration '
            f'-of default=noprint_wrappers=1:nokey=1 -sexagesimal "{src}"',
            shell=True)
        return a.decode().strip()

    except CalledProcessError as e:
        print(e.output)
        a = None
        return a


if __name__ == '__main__':

    src = 'your/video/path.mp4'
    print(get_duration(src))
